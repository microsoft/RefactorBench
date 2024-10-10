import unittest
import os
import ast

class TestFunctionParameter(unittest.TestCase):

    def test_get_encoding_from_headers_log_param(self):
        # Path to the file where the function should be located
        file_path = '../src/requests/utils.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Parse the file to check the function's parameters
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        function_found = False
        param_is_boolean = False

        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef) and node.name == 'get_encoding_from_headers':
                function_found = True
                # Check parameters for the 'log' argument
                for arg in node.args.args:
                    if arg.arg == 'log':
                        param_is_boolean = True  # Assume it's boolean, detailed type checks require running code or a type checker
                        break
                break

        self.assertTrue(function_found, "Function 'get_encoding_from_headers' not found in the file")
        self.assertTrue(param_is_boolean, "Function 'get_encoding_from_headers' does not have a 'log' parameter or it is not a boolean")

    def test_log_param_in_function_call(self):
        # Path to the file where the function call should be located
        call_file_path = '../src/requests/adapters.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(call_file_path), f"{call_file_path} does not exist")

        # Parse the file to check the function call's arguments
        with open(call_file_path, 'r') as file:
            tree = ast.parse(file.read())

        log_param_set_to_true = False

        for node in ast.walk(tree):
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == 'get_encoding_from_headers':
                # Check if 'log' parameter is set to True in the function call
                for keyword in node.keywords:
                    if keyword.arg == 'log' and isinstance(keyword.value, ast.Constant) and keyword.value.value is True:
                        log_param_set_to_true = True
                        break
                if log_param_set_to_true:
                    break

        self.assertTrue(log_param_set_to_true, "Function 'get_encoding_from_headers' is called without 'log=True' in the function call")


    def test_log_param_in_function_call_false(self):
        # Path to the file where the function call should be located
        call_file_path = '../tests/test_utils.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(call_file_path), f"{call_file_path} does not exist")

        # Parse the file to check the function call's arguments
        with open(call_file_path, 'r') as file:
            tree = ast.parse(file.read())

        log_param_set_to_true = False

        for node in ast.walk(tree):
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == 'get_encoding_from_headers':
                # Check if 'log' parameter is set to True in the function call
                for keyword in node.keywords:
                    if keyword.arg == 'log' and isinstance(keyword.value, ast.Constant) and keyword.value.value is False:
                        log_param_set_to_true = True
                        break
                if log_param_set_to_true:
                    break

        self.assertTrue(log_param_set_to_true, "Function 'get_encoding_from_headers' is called without 'log=False' in the function call in tests")

if __name__ == '__main__':
    unittest.main()
