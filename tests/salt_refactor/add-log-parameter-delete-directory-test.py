import unittest
import os
import ast

class TestSaltUtilsSMB(unittest.TestCase):

    def test_delete_directory_has_log_parameter(self):
        file_path = '../salt/utils/smb.py'
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        delete_directory_function = None
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef) and node.name == 'delete_directory':
                delete_directory_function = node
                break

        self.assertIsNotNone(delete_directory_function, f"'delete_directory' function not found in {file_path}")
        
        log_param_found = False
        log_param_default_is_false = False
        for i, arg in enumerate(delete_directory_function.args.args):
            if arg.arg == 'log':
                log_param_found = True
                # Ensure the corresponding default value is False
                if i >= len(delete_directory_function.args.args) - len(delete_directory_function.args.defaults):
                    default_index = i - (len(delete_directory_function.args.args) - len(delete_directory_function.args.defaults))
                    log_param_default_is_false = isinstance(delete_directory_function.args.defaults[default_index], ast.Constant) and delete_directory_function.args.defaults[default_index].value is False
                break

        self.assertTrue(log_param_found, f"'log' parameter not found in 'delete_directory' function in {file_path}")
        self.assertTrue(log_param_default_is_false, f"'log' parameter in 'delete_directory' function does not default to False in {file_path}")

    def test_delete_directory_usage_has_log_true(self):
        file_path = '../salt/utils/cloud.py'
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        delete_directory_calls = []

        # Walk through all nodes in the AST tree
        for node in ast.walk(tree):
            if isinstance(node, ast.Call):
                func = node.func
                if isinstance(func, ast.Attribute):
                    # Handle cases like salt.utils.smb.delete_directory()
                    if func.attr == 'delete_directory':
                        # Traverse the chain of attributes (e.g., salt.utils.smb)
                        current_node = func.value
                        full_name = []
                        while isinstance(current_node, ast.Attribute):
                            full_name.insert(0, current_node.attr)
                            current_node = current_node.value
                        if isinstance(current_node, ast.Name):
                            full_name.insert(0, current_node.id)
                        # Check if the full name matches 'salt.utils.smb'
                        if full_name == ['salt', 'utils', 'smb']:
                            delete_directory_calls.append(node)

        self.assertGreater(len(delete_directory_calls), 0, f"No calls to 'salt.utils.smb.delete_directory()' found in {file_path}")

        for call in delete_directory_calls:
            log_argument = any(
                isinstance(arg, ast.keyword) and arg.arg == 'log' and isinstance(arg.value, ast.Constant) and arg.value.value is True
                for arg in call.keywords
            )
            self.assertTrue(
                log_argument,
                f"Call to 'salt.utils.smb.delete_directory()' without 'log=True' found in {file_path}: {ast.dump(call)}"
            )
       
    def test_delete_directory_calls_integration_tests(self):
        file_path = '../tests/integration/utils/test_smb.py'
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        delete_directory_calls = []

        # Walk through all nodes in the AST tree
        for node in ast.walk(tree):
            if isinstance(node, ast.Call):
                func = node.func
                if isinstance(func, ast.Attribute):
                    # Handle cases like salt.utils.smb.delete_directory()
                    if func.attr == 'delete_directory':
                        # Traverse the chain of attributes (e.g., salt.utils.smb)
                        current_node = func.value
                        full_name = []
                        while isinstance(current_node, ast.Attribute):
                            full_name.insert(0, current_node.attr)
                            current_node = current_node.value
                        if isinstance(current_node, ast.Name):
                            full_name.insert(0, current_node.id)
                        # Check if the full name matches 'salt.utils.smb'
                        if full_name == ['salt', 'utils', 'smb']:
                            delete_directory_calls.append(node)

        self.assertGreater(len(delete_directory_calls), 0, f"No calls to 'salt.utils.smb.delete_directory()' found in {file_path}")

        for call in delete_directory_calls:
            log_argument = None
            for arg in call.keywords:
                if arg.arg == 'log':
                    log_argument = arg.value
                    break

            # Ensure log is False or not provided
            if log_argument is not None:
                self.assertIsInstance(log_argument, ast.Constant, f"Unexpected 'log' argument in call: {ast.dump(call)}")
                self.assertFalse(log_argument.value, f"Call to 'salt.utils.smb.delete_directory()' has 'log=True' in {file_path}: {ast.dump(call)}")
    
    def test_smb_py_has_delete_directory(self):
        file_path = '../salt/utils/smb.py'
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        delete_directory_function = None
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef) and node.name == 'delete_directory':
                delete_directory_function = node
                break

        self.assertIsNotNone(delete_directory_function, f"'delete_directory' function not found in {file_path}")
     
            
if __name__ == '__main__':
    unittest.main()
