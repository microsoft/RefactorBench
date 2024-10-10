import unittest
import os
import ast

class TestAnsibleImports(unittest.TestCase):

    def test_get_group_vars_has_log_parameter(self):
        # Path to the file where the get_group_vars function should be defined
        file_path = '../lib/ansible/inventory/helpers.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Check if get_group_vars function has a 'log' parameter
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        get_group_vars_function = None
        log_parameter_found = False

        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef) and node.name == 'get_group_vars':
                get_group_vars_function = node
                for arg in get_group_vars_function.args.args:
                    if arg.arg == 'log':
                        log_parameter_found = True

        self.assertIsNotNone(get_group_vars_function, "Function 'get_group_vars' not found in helpers.py")
        self.assertTrue(log_parameter_found, "Parameter 'log' not found in 'get_group_vars' function")
        
    def test_log_false_in_variable_manager_get_vars(self):
        # Path to the file where VariableManager and get_vars should be defined
        file_path = '../lib/ansible/vars/manager.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Check if log=False is passed to get_group_vars in get_vars method of VariableManager class
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        variable_manager_class = None
        get_vars_function = None
        log_false_passed_in_get_vars = False

        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef) and node.name == 'VariableManager':
                variable_manager_class = node
                for inner_node in ast.walk(variable_manager_class):
                    if isinstance(inner_node, ast.FunctionDef) and inner_node.name == 'get_vars':
                        get_vars_function = inner_node
                        for def_node in ast.walk(get_vars_function):
                            if isinstance(def_node, ast.FunctionDef) and def_node.name == 'groups_inventory':
                                for call_node in ast.walk(def_node):
                                    if isinstance(call_node, ast.Call) and isinstance(call_node.func, ast.Name) and call_node.func.id == 'get_group_vars':
                                        for keyword in call_node.keywords:
                                            if keyword.arg == 'log' and isinstance(keyword.value, ast.Constant) and keyword.value.value is False:
                                                log_false_passed_in_get_vars = True

        self.assertIsNotNone(variable_manager_class, "Class 'VariableManager' not found in manager.py")
        self.assertIsNotNone(get_vars_function, "Function 'get_vars' not found in VariableManager class in manager.py")
        self.assertTrue(log_false_passed_in_get_vars, "Parameter 'log=False' not passed to 'get_group_vars' in 'groups_inventory' function of 'get_vars' method")

    def test_vars_plugin_structure(self):
        # Path to the file to be checked
        file_path = '../test/integration/targets/old_style_vars_plugins/deprecation_warning/v2_vars_plugin.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Read and parse the file
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        # Check for future import
        future_import_found = False
        for node in tree.body:
            if isinstance(node, ast.ImportFrom) and node.module == '__future__' and any(alias.name == 'annotations' for alias in node.names):
                future_import_found = True

        self.assertTrue(future_import_found, "Missing 'from __future__ import annotations' in v2_vars_plugin.py")

        # Check for VarsModule class definition
        vars_module_class = None
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef) and node.name == 'VarsModule':
                vars_module_class = node
                break

        self.assertIsNotNone(vars_module_class, "Class 'VarsModule' not found in v2_vars_plugin.py")

        # Check methods get_host_vars and get_group_vars in VarsModule class
        required_methods = {'get_host_vars', 'get_group_vars'}
        found_methods = {node.name for node in vars_module_class.body if isinstance(node, ast.FunctionDef)}

        self.assertTrue(required_methods.issubset(found_methods), f"Methods {required_methods - found_methods} not found in VarsModule class")

        # Check that both methods return empty dicts
        for method_name in required_methods:
            method_node = next((node for node in vars_module_class.body if isinstance(node, ast.FunctionDef) and node.name == method_name), None)
            self.assertIsNotNone(method_node, f"Method {method_name} not found in VarsModule class")
            returns_empty_dict = any(isinstance(stmt, ast.Return) and isinstance(stmt.value, ast.Dict) and not stmt.value.keys for stmt in method_node.body)
            self.assertTrue(returns_empty_dict, f"Method {method_name} does not return an empty dictionary")
            
    def test_plugin_get_group_vars_no_log_in_plugins(self):
        # Path to the file to be checked
        file_path = '../lib/ansible/vars/plugins.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Read and parse the file
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        # Check that no calls to plugin.get_group_vars have the 'log' parameter
        for node in ast.walk(tree):
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute):
                if node.func.attr == 'get_group_vars' and isinstance(node.func.value, ast.Name) and node.func.value.id == 'plugin':
                    for keyword in node.keywords:
                        self.assertNotEqual(keyword.arg, 'log', f"'log' parameter should not be passed in {file_path}")

    def test_plugin_get_group_vars_no_log_in_manager(self):
        # Path to the file to be checked
        file_path = '../lib/ansible/vars/manager.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Read and parse the file
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        # Check that no calls to plugin.get_group_vars have the 'log' parameter
        for node in ast.walk(tree):
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute):
                if node.func.attr == 'get_group_vars' and isinstance(node.func.value, ast.Name) and node.func.value.id == 'plugin':
                    for keyword in node.keywords:
                        self.assertNotEqual(keyword.arg, 'log', f"'log' parameter should not be passed in {file_path}")




if __name__ == '__main__':
    unittest.main()
