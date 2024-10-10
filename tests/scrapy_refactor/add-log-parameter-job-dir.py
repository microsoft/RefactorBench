import unittest
import os
import ast

class TestScrapyMigration(unittest.TestCase):

    def test_job_dir_has_log_parameter(self):
        # Path to the file where the job_dir function is defined
        file_path = '../scrapy/utils/job.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Check if the job_dir function has a log parameter
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        job_dir_function = None
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef) and node.name == 'job_dir':
                job_dir_function = node
                break

        self.assertIsNotNone(job_dir_function, "Function 'job_dir' not found in job.py")

        log_param_found = False
        for arg in job_dir_function.args.args:
            if arg.arg == 'log':
                log_param_found = True
                break

        self.assertTrue(log_param_found, "Parameter 'log' not found in 'job_dir' function")

    def test_logging_imported_in_job(self):
        # Path to the file where logging should be imported
        file_path = '../scrapy/utils/job.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Check if logging is imported in job.py
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        logging_import_found = False
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    if alias.name == 'logging':
                        logging_import_found = True
                        break

        self.assertTrue(logging_import_found, "Import 'import logging' not found in job.py")

    def test_job_dir_call_in_dupefilters_has_log_false(self):
        # Path to the file where job_dir is called
        file_path = '../scrapy/dupefilters.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Check if job_dir is called with log=False in dupefilters.py
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        job_dir_call_found = False
        log_param_found = False

        for node in ast.walk(tree):
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == 'job_dir':
                job_dir_call_found = True
                for kw in node.keywords:
                    if kw.arg == 'log' and isinstance(kw.value, ast.Constant) and kw.value.value is False:
                        log_param_found = True
                        break

        self.assertTrue(job_dir_call_found, "Call to 'job_dir' not found in dupefilters.py")
        self.assertTrue(log_param_found, "Call to 'job_dir' in dupefilters.py does not have 'log=False'")

    def test_job_dir_call_in_spiderstate_has_log_false(self):
        # Path to the file where job_dir is called
        file_path = '../scrapy/extensions/spiderstate.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Check if job_dir is called with log=False in spiderstate.py
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        job_dir_call_found = False
        log_param_found = False

        for node in ast.walk(tree):
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == 'job_dir':
                job_dir_call_found = True
                for kw in node.keywords:
                    if kw.arg == 'log' and isinstance(kw.value, ast.Constant) and kw.value.value is False:
                        log_param_found = True
                        break

        self.assertTrue(job_dir_call_found, "Call to 'job_dir' not found in spiderstate.py")
        self.assertTrue(log_param_found, "Call to 'job_dir' in spiderstate.py does not have 'log=False'")

    def test_job_dir_call_in_scheduler_has_log_false(self):
        # Path to the file where job_dir is called
        file_path = '../scrapy/core/scheduler.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Check if job_dir is called with log=False in scheduler.py
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        job_dir_call_found = False
        log_param_found = False

        for node in ast.walk(tree):
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == 'job_dir':
                job_dir_call_found = True
                for kw in node.keywords:
                    if kw.arg == 'log' and isinstance(kw.value, ast.Constant) and kw.value.value is False:
                        log_param_found = True
                        break

        self.assertTrue(job_dir_call_found, "Call to 'job_dir' not found in scheduler.py")
        self.assertTrue(log_param_found, "Call to 'job_dir' in scheduler.py does not have 'log=False'")

if __name__ == '__main__':
    unittest.main()
