import unittest
import os
import ast

class TestSaltUtilsData(unittest.TestCase):

    def test_recursive_diff_has_log_parameter(self):
        file_path = '../salt/utils/data.py'
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        recursive_diff_function = None
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef) and node.name == 'recursive_diff':
                recursive_diff_function = node
                break

        self.assertIsNotNone(recursive_diff_function, f"'recursive_diff' function not found in {file_path}")
        log_param_found = any(arg.arg == 'log' for arg in recursive_diff_function.args.args)
        self.assertTrue(log_param_found, f"'log' parameter not found in 'recursive_diff' function in {file_path}")

    def test_recursive_diff_calls_have_log_argument(self):
        file_path = '../salt/utils/data.py'
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        calls_to_recursive_diff = [
            node for node in ast.walk(tree)
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == 'recursive_diff'
        ]

        self.assertGreater(len(calls_to_recursive_diff), 0, f"No calls to 'recursive_diff' found in {file_path}")

        for call in calls_to_recursive_diff:
            log_argument = any(
                isinstance(arg, ast.keyword) and arg.arg == 'log' for arg in call.keywords
            )
            self.assertTrue(
                log_argument,
                f"Call to 'recursive_diff' without 'log=log' found in {file_path}: {ast.dump(call)}"
            )
    
    def test_recursive_diff_does_not_have_log_parameter(self):
        file_path = '../salt/utils/dictdiffer.py'
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        recursive_diff_function = None
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef) and node.name == 'recursive_diff':
                recursive_diff_function = node
                break

        self.assertIsNotNone(recursive_diff_function, f"'recursive_diff' function not found in {file_path}")
        log_param_found = any(arg.arg == 'log' for arg in recursive_diff_function.args.args)
        self.assertFalse(log_param_found, f"'log' parameter should not be present in 'recursive_diff' function in {file_path}")

    def test_recursive_diff_calls_do_not_have_log_argument(self):
        file_path = '../salt/utils/listdiffer.py'
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        calls_to_recursive_diff = [
            node for node in ast.walk(tree)
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == 'recursive_diff'
        ]

        self.assertGreater(len(calls_to_recursive_diff), 0, f"No calls to 'recursive_diff' found in {file_path}")

        for call in calls_to_recursive_diff:
            log_argument = any(
                isinstance(arg, ast.keyword) and arg.arg == 'log' for arg in call.keywords
            )
            self.assertFalse(
                log_argument,
                f"Call to 'recursive_diff' with 'log' argument found in {file_path}: {ast.dump(call)}"
            )
            
    def test_recursive_diff_calls_have_log_true_argument(self):
        file_path = '../salt/states/win_lgpo_reg.py'
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        calls_to_recursive_diff = [
            node for node in ast.walk(tree)
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute)
            and node.func.attr == 'recursive_diff' and isinstance(node.func.value, ast.Attribute)
            and node.func.value.attr == 'data' and isinstance(node.func.value.value, ast.Attribute)
            and node.func.value.value.attr == 'utils' and isinstance(node.func.value.value.value, ast.Name)
            and node.func.value.value.value.id == 'salt'
        ]

        self.assertGreater(len(calls_to_recursive_diff), 0, f"No calls to 'salt.utils.data.recursive_diff' found in {file_path}")

        for call in calls_to_recursive_diff:
            log_argument_found = False
            for keyword in call.keywords:
                if keyword.arg == 'log' and isinstance(keyword.value, ast.Constant) and keyword.value.value is True:
                    log_argument_found = True
                    break

            self.assertTrue(
                log_argument_found,
                f"Call to 'salt.utils.data.recursive_diff' without 'log=True' found in {file_path}: {ast.dump(call)}"
            )
            
    def test_dictdiffer_recursive_diff_calls_do_not_have_log_argument(self):
        file_path = '../salt/states/file.py'
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        calls_to_recursive_diff = [
            node for node in ast.walk(tree)
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute)
            and node.func.attr == 'recursive_diff' and isinstance(node.func.value, ast.Attribute)
            and node.func.value.attr == 'dictdiffer' and isinstance(node.func.value.value, ast.Attribute)
            and node.func.value.value.attr == 'utils' and isinstance(node.func.value.value.value, ast.Name)
            and node.func.value.value.value.id == 'salt'
        ]

        self.assertGreater(len(calls_to_recursive_diff), 0, f"No calls to 'salt.utils.dictdiffer.recursive_diff' found in {file_path}")

        for call in calls_to_recursive_diff:
            log_argument = any(
                isinstance(arg, ast.keyword) and arg.arg == 'log' for arg in call.keywords
            )
            self.assertFalse(
                log_argument,
                f"Call to 'salt.utils.dictdiffer.recursive_diff' with 'log' argument found in {file_path}: {ast.dump(call)}"
            )

if __name__ == '__main__':
    unittest.main()
