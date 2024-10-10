import unittest
import os
import ast

class TestAnsibleImports(unittest.TestCase):

    def test_group_sort_imported_in_manager(self):
        # Path to the file where the imports should be defined
        file_path = '../lib/ansible/vars/manager.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Check if group_sort and get_group_vars are imported from ansible.inventory.helpers
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        group_sort_found = False
        get_group_vars_found = False

        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom):
                if node.module == 'ansible.inventory.helpers':
                    for alias in node.names:
                        if alias.name == 'group_sort':
                            group_sort_found = True
                        if alias.name == 'get_group_vars':
                            get_group_vars_found = True

        self.assertTrue(group_sort_found, "Import 'group_sort' not found in manager.py")
        self.assertTrue(get_group_vars_found, "Import 'get_group_vars' not found in manager.py")
        
    def test_group_sort_function_exists(self):
        # Path to the file where the group_sort function should be defined
        file_path = '../lib/ansible/inventory/helpers.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Check if group_sort function is defined in helpers.py
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        group_sort_function_found = False
        correct_lambda_found = False

        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef) and node.name == 'group_sort':
                group_sort_function_found = True
                # Check if the function has the correct lambda expression
                for inner_node in ast.walk(node):
                    if isinstance(inner_node, ast.Call) and isinstance(inner_node.func, ast.Name) and inner_node.func.id == 'sorted':
                        for keyword in inner_node.keywords:
                            if keyword.arg == 'key' and isinstance(keyword.value, ast.Lambda):
                                lambda_node = keyword.value
                                if isinstance(lambda_node.body, ast.Tuple) and len(lambda_node.body.elts) == 3:
                                    elements = [elt.attr for elt in lambda_node.body.elts if isinstance(elt, ast.Attribute)]
                                    if elements == ['depth', 'priority', 'name']:
                                        correct_lambda_found = True

        self.assertTrue(group_sort_function_found, "Function 'group_sort' not found in helpers.py")
        self.assertTrue(correct_lambda_found, "Lambda expression in 'group_sort' function does not match the expected structure")

    def test_get_group_vars_calls_group_sort(self):
        # Path to the file where the get_group_vars function should be defined
        file_path = '../lib/ansible/inventory/helpers.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Check if get_group_vars function calls group_sort(groups)
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        get_group_vars_function = None
        group_sort_call_found = False

        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef) and node.name == 'get_group_vars':
                get_group_vars_function = node
                for inner_node in ast.walk(get_group_vars_function):
                    if isinstance(inner_node, ast.Call) and isinstance(inner_node.func, ast.Name) and inner_node.func.id == 'group_sort':
                        group_sort_call_found = True
                        break

        self.assertIsNotNone(get_group_vars_function, "Function 'get_group_vars' not found in helpers.py")
        self.assertTrue(group_sort_call_found, "Call to 'group_sort(groups)' not found in 'get_group_vars' function")

    def test_group_sort_called_in_variable_manager_get_vars(self):
        # Path to the file where VariableManager and get_vars should be defined
        file_path = '../lib/ansible/vars/manager.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Check if group_sort is called in get_vars method of VariableManager class
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        variable_manager_class = None
        get_vars_function = None
        group_sort_call_found = False

        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef) and node.name == 'VariableManager':
                variable_manager_class = node
                for inner_node in ast.walk(variable_manager_class):
                    if isinstance(inner_node, ast.FunctionDef) and inner_node.name == 'get_vars':
                        get_vars_function = inner_node
                        for call_node in ast.walk(get_vars_function):
                            if isinstance(call_node, ast.Call) and isinstance(call_node.func, ast.Name) and call_node.func.id == 'group_sort':
                                group_sort_call_found = True
                                break

        self.assertIsNotNone(variable_manager_class, "Class 'VariableManager' not found in manager.py")
        self.assertIsNotNone(get_vars_function, "Function 'get_vars' not found in VariableManager class in manager.py")
        self.assertTrue(group_sort_call_found, "Call to 'group_sort(groups)' not found in 'get_vars' method of VariableManager class in manager.py")

if __name__ == '__main__':
    unittest.main()
