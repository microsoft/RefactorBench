import unittest
import os
import ast

class TestTornadoLogOptions(unittest.TestCase):

    def test_global_log_options_file_exists(self):
        # Path to the file that should be checked
        file_path = '../tornado/global_log_options.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

    def test_enable_pretty_logging_exists(self):
        # Path to the file where the function should be checked
        file_path = '../tornado/global_log_options.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Read and parse the content of global_log_options.py
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        # Check if function enable_pretty_logging exists
        function_found = False
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef) and node.name == 'enable_pretty_logging':
                function_found = True
                break

        self.assertTrue(function_found, "Function 'enable_pretty_logging' not found in global_log_options.py")

    def test_define_logging_options_exists(self):
        # Path to the file where the function should be checked
        file_path = '../tornado/global_log_options.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Read and parse the content of global_log_options.py
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        # Check if function define_logging_options exists with correct signature
        function_found = False
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef) and node.name == 'define_logging_options':
                # Check if it has the expected argument signature
                arg_names = [arg.arg for arg in node.args.args]
                if len(arg_names) == 1 and arg_names[0] == 'options':
                    function_found = True
                    break

        self.assertTrue(function_found, "Function 'define_logging_options' with expected signature not found in global_log_options.py")

    def test_log_file_does_not_have_functions(self):
        # Path to the file where the functions should not be present
        file_path = '../tornado/log.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Read and parse the content of log.py
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        # Check if 'enable_pretty_logging' or 'define_logging_options' exists
        forbidden_functions = {'enable_pretty_logging', 'define_logging_options'}
        functions_found = set()

        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef) and node.name in forbidden_functions:
                functions_found.add(node.name)

        # Ensure none of the forbidden functions are present
        self.assertFalse(functions_found, f"Functions {functions_found} found in log.py, but should not exist there")

    def test_import_in_options_py(self):
        # Path to the file where the import should be checked
        file_path = '../tornado/options.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Read and parse the content of options.py
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        # Check if 'from tornado.global_log_options import define_logging_options' exists
        import_found = False
        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom) and node.module == 'tornado.global_log_options':
                if any(alias.name == 'define_logging_options' for alias in node.names):
                    import_found = True
                    break

        self.assertTrue(import_found, "'from tornado.global_log_options import define_logging_options' not found in options.py")

    def test_imports_in_log_test_py(self):
        # Path to the file where the imports should be checked
        file_path = '../tornado/test/log_test.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Read and parse the content of log_test.py
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        # Check if 'from tornado.global_log_options import define_logging_options, enable_pretty_logging' exists
        import_global_log_options_found = False
        import_log_formatter_found = False

        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom):
                if node.module == 'tornado.global_log_options':
                    imported_names = {alias.name for alias in node.names}
                    if 'define_logging_options' in imported_names and 'enable_pretty_logging' in imported_names:
                        import_global_log_options_found = True

                if node.module == 'tornado.log':
                    if any(alias.name == 'LogFormatter' for alias in node.names):
                        import_log_formatter_found = True

        self.assertTrue(import_global_log_options_found, "'from tornado.global_log_options import define_logging_options, enable_pretty_logging' not found in log_test.py")
        self.assertTrue(import_log_formatter_found, "'from tornado.log import LogFormatter' not found in log_test.py")


    
if __name__ == '__main__':
    unittest.main()