import unittest
import os
import ast

class TestHelpersFunctions(unittest.TestCase):

    def test_get_flashed_messages_param_in_helpers(self):
        file_path = '../src/flask/helpers.py'
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        func_found = False
        log_param_found = False
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef) and node.name == 'get_flashed_messages':
                func_found = True
                for arg in node.args.args:
                    if arg.arg == 'log':
                        if isinstance(arg.annotation, ast.Name) and arg.annotation.id == 'bool':
                            log_param_found = True
                        break

        self.assertTrue(func_found, "Function 'get_flashed_messages' not found in helpers.py")
        self.assertTrue(log_param_found, "Parameter 'log: bool' not found in function 'get_flashed_messages'")

    def test_get_flashed_messages_param_default_value(self):
        file_path = '../src/flask/helpers.py'
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        func_found = False
        log_default_false = False
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef) and node.name == 'get_flashed_messages':
                func_found = True
                for default, arg in zip(reversed(node.args.defaults), reversed(node.args.args)):
                    if arg.arg == 'log':
                        if isinstance(default, ast.Constant) and default.value is False:
                            log_default_false = True
                        break

        self.assertTrue(func_found, "Function 'get_flashed_messages' not found in helpers.py")
        self.assertTrue(log_default_false, "Default value for parameter 'log' is not False in 'get_flashed_messages'")

    
    def test_get_flashed_messages_calls_in_test_basic(self):
        file_path = '../tests/test_basic.py'
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        call_log_true_found = True  # Assuming all are correct, set to False if any call fails
        for node in ast.walk(tree):
            if isinstance(node, ast.Call):
                # Check if it's a method call: flask.get_flashed_messages(...)
                if isinstance(node.func, ast.Attribute) and isinstance(node.func.value, ast.Name):
                    if node.func.value.id == 'flask' and node.func.attr == 'get_flashed_messages':
                        # Check if 'log=True' is in the keyword arguments
                        log_kwarg_found = False
                        for keyword in node.keywords:
                            if keyword.arg == 'log' and isinstance(keyword.value, ast.Constant) and keyword.value.value is True:
                                log_kwarg_found = True
                                break
                        if not log_kwarg_found:
                            call_log_true_found = False
                            break

        self.assertTrue(call_log_true_found, "Not all calls to 'flask.get_flashed_messages' have 'log=True' in test_basic.py")

    
if __name__ == '__main__':
    unittest.main()
