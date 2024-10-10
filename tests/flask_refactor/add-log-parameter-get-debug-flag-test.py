import unittest
import os
import ast

class TestHelpersFunctions(unittest.TestCase):

    def setUp(self):
        # Path to the helpers.py file
        self.file_path = '../src/flask/helpers.py'
        self.assertTrue(os.path.exists(self.file_path), f"{self.file_path} does not exist")

        # Parse the helpers.py file into an AST tree
        with open(self.file_path, 'r') as file:
            self.tree = ast.parse(file.read())

    def test_logging_import_in_helpers(self):
        """Test if logging is imported in helpers.py."""
        import_found = False
        for node in ast.walk(self.tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    if alias.name == 'logging':
                        import_found = True
                        break
            if import_found:
                break

        self.assertTrue(import_found, "'logging' not imported in helpers.py")

    def test_get_debug_flag_has_log_parameter(self):
        """Test if get_debug_flag function has a log parameter."""
        function_found = False
        log_parameter_found = False

        for node in ast.walk(self.tree):
            if isinstance(node, ast.FunctionDef) and node.name == 'get_debug_flag':
                function_found = True
                for arg in node.args.args:
                    if arg.arg == 'log':
                        log_parameter_found = True
                        break
                break

        self.assertTrue(function_found, "Function 'get_debug_flag' not found in helpers.py")
        self.assertTrue(log_parameter_found, "'log' parameter not found in get_debug_flag function")

    def test_get_debug_flag_log_default_false(self):
        """Test if the log parameter in get_debug_flag function is set to False by default."""
        function_found = False
        log_default_false = False

        for node in ast.walk(self.tree):
            if isinstance(node, ast.FunctionDef) and node.name == 'get_debug_flag':
                function_found = True
                for arg in node.args.defaults:
                    if isinstance(arg, ast.Constant) and arg.value is False:
                        log_default_false = True
                        break
                break

        self.assertTrue(function_found, "Function 'get_debug_flag' not found in helpers.py")
        self.assertTrue(log_default_false, "'log' parameter in get_debug_flag function is not set to False by default")

    def test_get_debug_flag_in_app(self):
        file_path = '../src/flask/app.py'
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        log_true_found = False
        for node in ast.walk(tree):
            if isinstance(node, ast.Call):
                if isinstance(node.func, ast.Name) and node.func.id == 'get_debug_flag':
                    for keyword in node.keywords:
                        if keyword.arg == 'log' and isinstance(keyword.value, ast.Constant) and keyword.value.value is True:
                            log_true_found = True
                            break
                if log_true_found:
                    break

        self.assertTrue(log_true_found, "get_debug_flag call with log=True not found in app.py")

    def test_get_debug_flag_in_cli(self):
        file_path = '../src/flask/cli.py'
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        log_true_found = False
        for node in ast.walk(tree):
            if isinstance(node, ast.Call):
                if isinstance(node.func, ast.Name) and node.func.id == 'get_debug_flag':
                    for keyword in node.keywords:
                        if keyword.arg == 'log' and isinstance(keyword.value, ast.Constant) and keyword.value.value is True:
                            log_true_found = True
                            break
                if log_true_found:
                    break

        self.assertTrue(log_true_found, "get_debug_flag call with log=True not found in cli.py")

    def test_get_debug_flag_in_sansio_app(self):
        file_path = '../src/flask/sansio/app.py'
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        log_true_found = False
        for node in ast.walk(tree):
            if isinstance(node, ast.Call):
                if isinstance(node.func, ast.Name) and node.func.id == 'get_debug_flag':
                    for keyword in node.keywords:
                        if keyword.arg == 'log' and isinstance(keyword.value, ast.Constant) and keyword.value.value is True:
                            log_true_found = True
                            break
                if log_true_found:
                    break

        self.assertTrue(log_true_found, "get_debug_flag call with log=True not found in sansio/app.py")

    def test_get_debug_flag_calls_in_test_helpers(self):
        file_path = '../tests/test_helpers.py'
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        all_calls_valid = True
        for node in ast.walk(tree):
            if isinstance(node, ast.Call):
                if isinstance(node.func, ast.Name) and node.func.id == 'get_debug_flag':
                    log_keyword = None
                    for keyword in node.keywords:
                        if keyword.arg == 'log':
                            log_keyword = keyword
                            break
                    if log_keyword is not None:
                        if not (isinstance(log_keyword.value, ast.Constant) and log_keyword.value.value is False):
                            all_calls_valid = False
                            break

        self.assertTrue(all_calls_valid, "Not all get_debug_flag calls have log=False or omit the log argument in test_helpers.py")

    
if __name__ == '__main__':
    unittest.main()
