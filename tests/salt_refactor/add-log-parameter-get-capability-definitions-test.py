import unittest
import os
import ast

class TestSaltUtilsPBM(unittest.TestCase):

    def test_get_capability_definitions_has_log_parameter(self):
        file_path = '../salt/utils/pbm.py'
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        get_capability_definitions_function = None
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef) and node.name == 'get_capability_definitions':
                get_capability_definitions_function = node
                break

        self.assertIsNotNone(get_capability_definitions_function, f"'get_capability_definitions' function not found in {file_path}")
        
        log_param_found = False
        log_param_default_is_false = False
        for i, arg in enumerate(get_capability_definitions_function.args.args):
            if arg.arg == 'log':
                log_param_found = True
                # Ensure the corresponding default value is False
                if i >= len(get_capability_definitions_function.args.args) - len(get_capability_definitions_function.args.defaults):
                    default_index = i - (len(get_capability_definitions_function.args.args) - len(get_capability_definitions_function.args.defaults))
                    log_param_default_is_false = isinstance(get_capability_definitions_function.args.defaults[default_index], ast.Constant) and get_capability_definitions_function.args.defaults[default_index].value is False
                break

        self.assertTrue(log_param_found, f"'log' parameter not found in 'get_capability_definitions' function in {file_path}")
        self.assertTrue(log_param_default_is_false, f"'log' parameter in 'get_capability_definitions' function does not default to False in {file_path}")

    def test_get_capability_definitions_usage_has_log_true(self):
        file_path = '../salt/modules/vsphere.py'
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        get_capability_definitions_calls = []

        # Walk through all nodes in the AST tree
        for node in ast.walk(tree):
            if isinstance(node, ast.Call):
                func = node.func
                if isinstance(func, ast.Attribute):
                    # Handle cases like salt.utils.pbm.get_capability_definitions()
                    if func.attr == 'get_capability_definitions':
                        # Traverse the chain of attributes (e.g., salt.utils.pbm)
                        current_node = func.value
                        full_name = []
                        while isinstance(current_node, ast.Attribute):
                            full_name.insert(0, current_node.attr)
                            current_node = current_node.value
                        if isinstance(current_node, ast.Name):
                            full_name.insert(0, current_node.id)
                        # Check if the full name matches 'salt.utils.pbm'
                        if full_name == ['salt', 'utils', 'pbm']:
                            get_capability_definitions_calls.append(node)

        self.assertGreater(len(get_capability_definitions_calls), 0, f"No calls to 'salt.utils.pbm.get_capability_definitions()' found in {file_path}")

        for call in get_capability_definitions_calls:
            log_argument = any(
                isinstance(arg, ast.keyword) and arg.arg == 'log' and isinstance(arg.value, ast.Constant) and arg.value.value is True
                for arg in call.keywords
            )
            self.assertTrue(
                log_argument,
                f"Call to 'salt.utils.pbm.get_capability_definitions()' without 'log=True' found in {file_path}: {ast.dump(call)}"
            )
    def test_get_capability_definitions_usage_has_log_false_or_no_log(self):
        file_path = '../tests/unit/utils/test_pbm.py'
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        get_capability_definitions_calls = []

        # Walk through all nodes in the AST tree
        for node in ast.walk(tree):
            if isinstance(node, ast.Call):
                func = node.func
                if isinstance(func, ast.Attribute):
                    # Handle cases like salt.utils.pbm.get_capability_definitions()
                    if func.attr == 'get_capability_definitions':
                        # Traverse the chain of attributes (e.g., salt.utils.pbm)
                        current_node = func.value
                        full_name = []
                        while isinstance(current_node, ast.Attribute):
                            full_name.insert(0, current_node.attr)
                            current_node = current_node.value
                        if isinstance(current_node, ast.Name):
                            full_name.insert(0, current_node.id)
                        # Check if the full name matches 'salt.utils.pbm'
                        if full_name == ['salt', 'utils', 'pbm']:
                            get_capability_definitions_calls.append(node)

        self.assertGreater(len(get_capability_definitions_calls), 0, f"No calls to 'salt.utils.pbm.get_capability_definitions()' found in {file_path}")

        for call in get_capability_definitions_calls:
            log_argument = None
            for arg in call.keywords:
                if arg.arg == 'log':
                    log_argument = arg.value
                    break

            # Ensure log is False or not provided
            if log_argument is not None:
                self.assertIsInstance(log_argument, ast.Constant, f"Unexpected 'log' argument in call: {ast.dump(call)}")
                self.assertFalse(log_argument.value, f"Call to 'salt.utils.pbm.get_capability_definitions()' has 'log=True' in {file_path}: {ast.dump(call)}")
    
            
if __name__ == '__main__':
    unittest.main()
