import unittest
import os
import ast

class TestCeleryUtils(unittest.TestCase):

    def test_node_format_has_log_parameter(self):
        # Path to the file where the node_format function should be defined
        file_path = '../celery/utils/nodenames.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Check if node_format function is defined in nodenames.py
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        node_format_function = None

        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef) and node.name == 'node_format':
                node_format_function = node
                break

        self.assertIsNotNone(node_format_function, "Function 'node_format' not found in nodenames.py")

        # Check if the log parameter exists with a default value of False
        log_param_found = False
        for arg in node_format_function.args.args:
            if arg.arg == 'log' and isinstance(arg.annotation, ast.Name) and arg.annotation.id == 'bool':
                default_index = node_format_function.args.args.index(arg) - len(node_format_function.args.args) + len(node_format_function.args.defaults)
                if default_index >= 0:
                    default_value = node_format_function.args.defaults[default_index]
                    if isinstance(default_value, ast.Constant) and default_value.value is False:
                        log_param_found = True
                        break

        self.assertTrue(log_param_found, "Parameter 'log: bool = False' not found in 'node_format' function")

    def test_node_format_calls_in_worker_have_log_true(self):
        # Path to the file where the node_format calls should be checked
        file_path = '../celery/bin/worker.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Parse the worker.py file to find all calls to node_format
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        node_format_calls_with_log_true = True

        for node in ast.walk(tree):
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == 'node_format':
                # Check if 'log=True' is among the arguments
                log_param_found = False
                for kw in node.keywords:
                    if kw.arg == 'log' and isinstance(kw.value, ast.Constant) and kw.value.value is True:
                        log_param_found = True
                        break
                if not log_param_found:
                    node_format_calls_with_log_true = False
                    break

        self.assertTrue(node_format_calls_with_log_true, "Not all 'node_format' calls in worker.py have 'log=True'")

    def test_node_format_calls_in_log_have_log_true(self):
        # Path to the file where the node_format calls should be checked
        file_path = '../celery/app/log.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Parse the log.py file to find all calls to node_format
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        node_format_calls_with_log_true = True

        for node in ast.walk(tree):
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == 'node_format':
                # Check if 'log=True' is among the arguments
                log_param_found = False
                for kw in node.keywords:
                    if kw.arg == 'log' and isinstance(kw.value, ast.Constant) and kw.value.value is True:
                        log_param_found = True
                        break
                if not log_param_found:
                    node_format_calls_with_log_true = False
                    break

        self.assertTrue(node_format_calls_with_log_true, "Not all 'node_format' calls in log.py have 'log=True'")

if __name__ == '__main__':
    unittest.main()
