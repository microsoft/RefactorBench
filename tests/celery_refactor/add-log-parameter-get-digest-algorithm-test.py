import unittest
import os
import ast

class TestCelerySecurityUtils(unittest.TestCase):

    def test_get_digest_algorithm_function_exists(self):
        # Path to the file where the get_digest_algorithm function should be defined
        file_path = '../celery/security/utils.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Check if get_digest_algorithm function is defined in utils.py
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        get_digest_algorithm_function = None

        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef) and node.name == 'get_digest_algorithm':
                get_digest_algorithm_function = node
                break

        self.assertIsNotNone(get_digest_algorithm_function, "Function 'get_digest_algorithm' not found in utils.py")

    def test_get_digest_algorithm_has_log_parameter(self):
        # Path to the file where the get_digest_algorithm function should be defined
        file_path = '../celery/security/utils.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Check if get_digest_algorithm function has a log boolean parameter in utils.py
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        get_digest_algorithm_function = None
        log_param_found = False

        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef) and node.name == 'get_digest_algorithm':
                get_digest_algorithm_function = node
                for arg in get_digest_algorithm_function.args.args:
                    if arg.arg == 'log':
                        log_param_found = True
                        break
                break

        self.assertIsNotNone(get_digest_algorithm_function, "Function 'get_digest_algorithm' not found in utils.py")
        self.assertTrue(log_param_found, "'log' parameter not found in 'get_digest_algorithm' function")

    def test_log_parameter_is_false(self):
        # Path to the file where the get_digest_algorithm function should be defined
        file_path = '../celery/security/utils.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Check if log parameter is set to False by default in get_digest_algorithm function in utils.py
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        get_digest_algorithm_function = None
        log_param_is_false = False

        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef) and node.name == 'get_digest_algorithm':
                get_digest_algorithm_function = node
                for arg, default in zip(get_digest_algorithm_function.args.args, get_digest_algorithm_function.args.defaults):
                    if arg.arg == 'log':
                        if isinstance(default, ast.Constant) and default.value is False:
                            log_param_is_false = True
                        break
                break

        self.assertIsNotNone(get_digest_algorithm_function, "Function 'get_digest_algorithm' not found in utils.py")
        self.assertTrue(log_param_is_false, "'log' parameter does not have a default value of 'False' in 'get_digest_algorithm' function")

    def test_get_digest_algorithm_calls_have_log_true(self):
        # Path to the file where the get_digest_algorithm calls should be checked
        file_path = '../celery/security/serialization.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Parse the serialization.py file to find all calls to get_digest_algorithm
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        log_true_for_all_calls = True

        for node in ast.walk(tree):
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == 'get_digest_algorithm':
                log_arg_found = False
                for keyword in node.keywords:
                    if keyword.arg == 'log' and isinstance(keyword.value, ast.Constant) and keyword.value.value is True:
                        log_arg_found = True
                        break
                if not log_arg_found:
                    log_true_for_all_calls = False
                    break

        self.assertTrue(log_true_for_all_calls, "Not all calls to 'get_digest_algorithm' have 'log=True' in serialization.py")

    def test_get_digest_algorithm_calls_log_false_or_not_passed(self):
        # Path to the file where the get_digest_algorithm calls should be checked
        file_path = '../t/unit/security/test_key.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Parse the test_key.py file to find all calls to get_digest_algorithm
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        log_valid_for_all_calls = True

        for node in ast.walk(tree):
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == 'get_digest_algorithm':
                log_arg_found = False
                log_arg_is_false = False
                for keyword in node.keywords:
                    if keyword.arg == 'log':
                        log_arg_found = True
                        if isinstance(keyword.value, ast.Constant) and keyword.value.value is False:
                            log_arg_is_false = True
                        break
                if log_arg_found and not log_arg_is_false:
                    log_valid_for_all_calls = False
                    break

        self.assertTrue(log_valid_for_all_calls, "Not all calls to 'get_digest_algorithm' have 'log=False' or no 'log' argument in test_key.py")

if __name__ == '__main__':
    unittest.main()
