import unittest
import os
import ast
import hashlib

class TestScrapyMigration(unittest.TestCase):

    def test_disconnect_all_has_log_param(self):
        # Path to the file where the function is defined
        file_path = '../scrapy/utils/signal.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Check if the function is defined in signal.py and has a boolean parameter 'log'
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        function_found = False
        log_param_found = False
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef) and node.name == 'disconnect_all':
                function_found = True
                # Check if 'log' is a parameter and if its default value is boolean
                for arg in node.args.args:
                    if arg.arg == 'log':
                        log_param_found = True
                        # Check if 'log' has a default value and if it's boolean
                        if node.args.defaults:
                            log_default_value = node.args.defaults[-1]
                            if isinstance(log_default_value, ast.Constant) and isinstance(log_default_value.value, bool):
                                log_param_found = True
                                break

        self.assertTrue(function_found, "Function 'disconnect_all' not found in signal.py")
        self.assertTrue(log_param_found, "Function 'disconnect_all' does not have a boolean parameter 'log'")

    def test_test_engine_imports_disconnect_all(self):
        # Path to the test_engine file
        tests_file_path = '../tests/test_engine.py' 

        # Check if the test file exists
        self.assertTrue(os.path.exists(tests_file_path), f"Test file {tests_file_path} does not exist")

        # Check if the import statement for disconnect_all is present
        with open(tests_file_path, 'r') as file:
            tree = ast.parse(file.read())

        import_found = False
        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom):
                if node.module == 'scrapy.utils.signal' and \
                   any(alias.name == 'disconnect_all' for alias in node.names):
                    import_found = True
                    break

        self.assertTrue(import_found, "Import 'from scrapy.utils.signal import disconnect_all' not found in test_engine.py")

    def test_test_pipeline_media_imports_disconnect_all(self):
        # Path to the test_pipeline_media file
        tests_file_path = '../tests/test_pipeline_media.py' 

        # Check if the test file exists
        self.assertTrue(os.path.exists(tests_file_path), f"Test file {tests_file_path} does not exist")

        # Check if the import statement for disconnect_all is present
        with open(tests_file_path, 'r') as file:
            tree = ast.parse(file.read())

        import_found = False
        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom):
                if node.module == 'scrapy.utils.signal' and \
                   any(alias.name == 'disconnect_all' for alias in node.names):
                    import_found = True
                    break

        self.assertTrue(import_found, "Import 'from scrapy.utils.signal import disconnect_all' not found in test_pipeline_media.py")

    def test_signalmanager_file_unchanged(self):
        # Path to the signalmanager.py file
        file_path = '../scrapy/signalmanager.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Calculate the hash of the file
        with open(file_path, 'rb') as file:
            file_content = file.read()
            file_hash = hashlib.sha256(file_content).hexdigest()

        # The expected hash for the unchanged file
        expected_hash = '5f8681de29fccd22e2b0aa50a6255ab22d81e5abdddb43c46ef059cb2cc4532c'  # Replace with the actual hash value

        # Check if the file hash matches the expected hash
        self.assertEqual(file_hash, expected_hash, "The signalmanager.py file has been modified")

    def test_disconnect_all_log_param_in_test_engine(self):
        # Path to the test_engine file
        tests_file_path = '../tests/test_engine.py'

        # Check if the test file exists
        self.assertTrue(os.path.exists(tests_file_path), f"Test file {tests_file_path} does not exist")

        # Check if the disconnect_all function is called with the 'log' parameter
        with open(tests_file_path, 'r') as file:
            tree = ast.parse(file.read())

        log_param_found = False
        for node in ast.walk(tree):
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == 'disconnect_all':
                for keyword in node.keywords:
                    if keyword.arg == 'log':
                        log_param_found = True
                        break

        self.assertTrue(log_param_found, "The 'disconnect_all' function is not called with the 'log' parameter in test_engine.py")

    def test_disconnect_all_log_param_in_test_pipeline_media(self):
        # Path to the test_pipeline_media file
        tests_file_path = '../tests/test_pipeline_media.py'

        # Check if the test file exists
        self.assertTrue(os.path.exists(tests_file_path), f"Test file {tests_file_path} does not exist")

        # Check if the disconnect_all function is called with the 'log' parameter
        with open(tests_file_path, 'r') as file:
            tree = ast.parse(file.read())

        log_param_found = False
        for node in ast.walk(tree):
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == 'disconnect_all':
                for keyword in node.keywords:
                    if keyword.arg == 'log':
                        log_param_found = True
                        break

        self.assertTrue(log_param_found, "The 'disconnect_all' function is not called with the 'log' parameter in test_pipeline_media.py")


if __name__ == '__main__':
    unittest.main()
