import unittest
import os
import ast

class TestWorkerRequestImports(unittest.TestCase):

    def test_trace_imports_in_test_request(self):
        # Path to the file where the import should be checked
        file_path = '../t/unit/worker/test_request.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Parse the test_request.py file to check for the specific import
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        expected_imports = {'TraceInfo', 'build_tracer', 'fast_trace_task',
                            'reset_worker_optimizations', 'setup_worker_optimizations',
                            'trace_task', 'trace_task_ret'}
        actual_imports = set()

        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom):
                if node.module == 'celery.app.trace':
                    actual_imports.update({alias.name for alias in node.names})

        missing_imports = expected_imports - actual_imports
        self.assertFalse(missing_imports, f"Missing imports from 'celery.app.trace': {', '.join(missing_imports)}")

    def test_mro_lookup_import_in_test_request(self):
        # Path to the file where the import should be checked
        file_path = '../t/unit/worker/test_request.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Parse the test_request.py file to check for the specific import
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        import_found = False

        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom):
                if node.module == 'celery.utils.objects' and 'mro_lookup' in {alias.name for alias in node.names}:
                    import_found = True
                    break

        self.assertTrue(import_found, "'mro_lookup' not imported from 'celery.utils.objects' in test_request.py")

    
    def test_mro_lookup_import_in_trace(self):
        # Path to the file where the import should be checked
        file_path = '../celery/app/trace.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Parse the trace.py file to check for the specific import
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        import_found = False

        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom):
                if node.module == 'celery.utils.objects' and 'mro_lookup' in {alias.name for alias in node.names}:
                    import_found = True
                    break

        self.assertTrue(import_found, "'mro_lookup' not imported from 'celery.utils.objects' in trace.py")


if __name__ == '__main__':
    unittest.main()
