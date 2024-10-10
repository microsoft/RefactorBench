import unittest
import os
import ast

class TestTornadoImports(unittest.TestCase):

    def test_import_in_wsgi_py(self):
        # Path to the file where the import should be checked
        file_path = '../tornado/wsgi.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Read and parse the content of wsgi.py
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        # Check if 'from tornado._globals import dummy_executor' exists
        import_found = False
        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom) and node.module == 'tornado._globals':
                if any(alias.name == 'dummy_executor' for alias in node.names):
                    import_found = True
                    break

        self.assertTrue(import_found, "'from tornado._globals import dummy_executor' not found in wsgi.py")

    def test_imports_in_netutil_py(self):
        # Path to the file where the imports should be checked
        file_path = '../tornado/netutil.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Read and parse the content of netutil.py
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        # Check if 'from tornado._globals import dummy_executor' and 'from tornado.concurrent import run_on_executor' exist
        import_globals_found = False
        import_concurrent_found = False

        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom):
                if node.module == 'tornado._globals':
                    if any(alias.name == 'dummy_executor' for alias in node.names):
                        import_globals_found = True
                if node.module == 'tornado.concurrent':
                    if any(alias.name == 'run_on_executor' for alias in node.names):
                        import_concurrent_found = True

        self.assertTrue(import_globals_found, "'from tornado._globals import dummy_executor' not found in netutil.py")
        self.assertTrue(import_concurrent_found, "'from tornado.concurrent import run_on_executor' not found in netutil.py")

    def test_globals_py_exists_and_has_dummy_executor(self):
        # Path to the file where the existence and content should be checked
        file_path = '../tornado/_globals.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Read and parse the content of _globals.py
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        # Check if 'from tornado.concurrent import DummyExecutor' exists and dummy_executor is defined
        import_found = False
        dummy_executor_defined = False

        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom) and node.module == 'tornado.concurrent':
                if any(alias.name == 'DummyExecutor' for alias in node.names):
                    import_found = True
            if isinstance(node, ast.Assign):
                if (isinstance(node.targets[0], ast.Name) and
                        node.targets[0].id == 'dummy_executor' and
                        isinstance(node.value, ast.Call) and
                        isinstance(node.value.func, ast.Name) and
                        node.value.func.id == 'DummyExecutor'):
                    dummy_executor_defined = True

        self.assertTrue(import_found, "'from tornado.concurrent import DummyExecutor' not found in _globals.py")
        self.assertTrue(dummy_executor_defined, "'dummy_executor = DummyExecutor()' not found in _globals.py")

    def test_concurrent_py_does_not_have_dummy_executor(self):
        # Path to the file where we should ensure dummy_executor is not defined
        file_path = '../tornado/concurrent.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Read and parse the content of concurrent.py
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        # Ensure 'dummy_executor = DummyExecutor()' is not present
        dummy_executor_found = False
        for node in ast.walk(tree):
            if isinstance(node, ast.Assign):
                if (isinstance(node.targets[0], ast.Name) and
                        node.targets[0].id == 'dummy_executor' and
                        isinstance(node.value, ast.Call) and
                        isinstance(node.value.func, ast.Name) and
                        node.value.func.id == 'DummyExecutor'):
                    dummy_executor_found = True
                    break

        self.assertFalse(dummy_executor_found, "'dummy_executor = DummyExecutor()' should not be found in concurrent.py")


if __name__ == '__main__':
    unittest.main()