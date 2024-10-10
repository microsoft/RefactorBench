import unittest
import os
import ast

class TestAnsibleImports(unittest.TestCase):

    def test_is_systemd_managed_has_log_parameter(self):
        # Path to the file where the is_systemd_managed function should be defined
        file_path = '../lib/ansible/module_utils/service.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Check if is_systemd_managed function has a 'log' parameter
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        is_systemd_managed_function = None
        log_parameter_found = False

        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef) and node.name == 'is_systemd_managed':
                is_systemd_managed_function = node
                for arg in is_systemd_managed_function.args.args:
                    if arg.arg == 'log':
                        log_parameter_found = True

        self.assertIsNotNone(is_systemd_managed_function, "Function 'is_systemd_managed' not found in service.py")
        self.assertTrue(log_parameter_found, "Parameter 'log' not found in 'is_systemd_managed' function")
        
    def test_is_systemd_managed_called_with_log_true_in_service(self):
        # Path to the file where the service.py module should be checked
        file_path = '../lib/ansible/modules/service.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Check if is_systemd_managed is called with log=True
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        log_true_passed_in_is_systemd_managed = False

        for node in ast.walk(tree):
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == 'is_systemd_managed':
                for keyword in node.keywords:
                    if keyword.arg == 'log' and isinstance(keyword.value, ast.Constant) and keyword.value.value is True:
                        log_true_passed_in_is_systemd_managed = True

        self.assertTrue(log_true_passed_in_is_systemd_managed, "Parameter 'log=True' not passed to 'is_systemd_managed' in service.py")

    def test_is_systemd_managed_called_with_log_true_in_service_facts(self):
        # Path to the file where the service_facts.py module should be checked
        file_path = '../lib/ansible/modules/service_facts.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Check if is_systemd_managed is called with log=True
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        log_true_passed_in_is_systemd_managed = False

        for node in ast.walk(tree):
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == 'is_systemd_managed':
                for keyword in node.keywords:
                    if keyword.arg == 'log' and isinstance(keyword.value, ast.Constant) and keyword.value.value is True:
                        log_true_passed_in_is_systemd_managed = True

        self.assertTrue(log_true_passed_in_is_systemd_managed, "Parameter 'log=True' not passed to 'is_systemd_managed' in service_facts.py")
        
    def test_is_systemd_managed_unchanged_in_systemd_facts(self):
        # Path to the file where ServiceMgrFactCollector.is_systemd_managed(module) should be checked
        file_path = '../lib/ansible/module_utils/facts/system/systemd.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Read and parse the file
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        # Check if ServiceMgrFactCollector.is_systemd_managed(module) is present and unchanged
        is_systemd_managed_call_found = False
        log_parameter_found = False
        for node in ast.walk(tree):
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute):
                if (node.func.attr == 'is_systemd_managed' and
                        isinstance(node.func.value, ast.Name) and node.func.value.id == 'ServiceMgrFactCollector'):
                    is_systemd_managed_call_found = True
                    for keyword in node.keywords:
                        if keyword.arg == 'log':
                            log_parameter_found = True
                    break

        self.assertTrue(is_systemd_managed_call_found, "Call to ServiceMgrFactCollector.is_systemd_managed(module) not found or changed in systemd.py")
        self.assertFalse(log_parameter_found, "Parameter 'log' should not be passed to 'ServiceMgrFactCollector.is_systemd_managed(module)' in systemd.py")

    def test_is_systemd_managed_unchanged_in_hostname(self):
        # Path to the file where ServiceMgrFactCollector.is_systemd_managed(module) should be checked
        file_path = '../lib/ansible/modules/hostname.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Read and parse the file
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        # Check if ServiceMgrFactCollector.is_systemd_managed(module) is present and unchanged
        is_systemd_managed_call_found = False
        log_parameter_found = False
        for node in ast.walk(tree):
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute):
                if (node.func.attr == 'is_systemd_managed' and
                        isinstance(node.func.value, ast.Name) and node.func.value.id == 'ServiceMgrFactCollector'):
                    is_systemd_managed_call_found = True
                    for keyword in node.keywords:
                        if keyword.arg == 'log':
                            log_parameter_found = True
                    break

        self.assertTrue(is_systemd_managed_call_found, "Call to ServiceMgrFactCollector.is_systemd_managed(module) not found or changed in hostname.py")
        self.assertFalse(log_parameter_found, "Parameter 'log' should not be passed to 'ServiceMgrFactCollector.is_systemd_managed(module)' in hostname.py")


if __name__ == '__main__':
    unittest.main()
