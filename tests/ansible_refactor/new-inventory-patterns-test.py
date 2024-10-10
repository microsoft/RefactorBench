import unittest
import os
import ast

class TestAnsibleImports(unittest.TestCase):

    def test_import_exists_in_manager(self):
        # Path to the file where the import should be checked
        file_path = '../lib/ansible/inventory/manager.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Check if the import from ansible.inventory.patterns exists
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        import_found = False

        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom):
                if node.module == 'ansible.inventory.patterns':
                    imported_names = {alias.name for alias in node.names}
                    if 'order_patterns' in imported_names and 'split_host_pattern' in imported_names:
                        import_found = True

        self.assertTrue(import_found, "Import 'from ansible.inventory.patterns import order_patterns, split_host_pattern' not found in manager.py")

    def test_functions_exist_in_patterns(self):
        # Path to the file where the functions should be defined
        file_path = '../lib/ansible/inventory/patterns.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Check if order_patterns and split_host_pattern functions are defined
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        order_patterns_found = False
        split_host_pattern_found = False

        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                if node.name == 'order_patterns':
                    order_patterns_found = True
                if node.name == 'split_host_pattern':
                    split_host_pattern_found = True

        self.assertTrue(order_patterns_found, "Function 'order_patterns' not found in patterns.py")
        self.assertTrue(split_host_pattern_found, "Function 'split_host_pattern' not found in patterns.py")
        
    def test_import_re_exists(self):
        # Path to the file where the import should be checked
        file_path = '../lib/ansible/inventory/patterns.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Check if the import 'import re' exists
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        import_found = False

        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    if alias.name == 're':
                        import_found = True

        self.assertTrue(import_found, "Import 'import re' not found in patterns.py")

    def test_import_itertools_exists(self):
        # Path to the file where the import should be checked
        file_path = '../lib/ansible/inventory/patterns.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Check if the import 'import itertools' exists
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        import_found = False

        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    if alias.name == 'itertools':
                        import_found = True

        self.assertTrue(import_found, "Import 'import itertools' not found in patterns.py")

    def test_import_string_types_exists(self):
        # Path to the file where the import should be checked
        file_path = '../lib/ansible/inventory/patterns.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Check if the import 'from ansible.module_utils.six import string_types' exists
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        import_found = False

        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom):
                if node.module == 'ansible.module_utils.six':
                    imported_names = {alias.name for alias in node.names}
                    if 'string_types' in imported_names:
                        import_found = True

        self.assertTrue(import_found, "Import 'from ansible.module_utils.six import string_types' not found in patterns.py")

    def test_import_parse_address_exists(self):
        # Path to the file where the import should be checked
        file_path = '../lib/ansible/inventory/patterns.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Check if the import 'from ansible.parsing.utils.addresses import parse_address' exists
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        import_found = False

        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom):
                if node.module == 'ansible.parsing.utils.addresses':
                    imported_names = {alias.name for alias in node.names}
                    if 'parse_address' in imported_names:
                        import_found = True

        self.assertTrue(import_found, "Import 'from ansible.parsing.utils.addresses import parse_address' not found in patterns.py")

    def test_import_to_text_exists(self):
        # Path to the file where the import should be checked
        file_path = '../lib/ansible/inventory/patterns.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Check if the import 'from ansible.module_utils.common.text.converters import to_text' exists
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        import_found = False

        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom):
                if node.module == 'ansible.module_utils.common.text.converters':
                    imported_names = {alias.name for alias in node.names}
                    if 'to_text' in imported_names:
                        import_found = True

        self.assertTrue(import_found, "Import 'from ansible.module_utils.common.text.converters import to_text' not found in patterns.py")
    
    def test_import_inventory_manager_exists(self):
        # Path to the file where the import should be checked
        file_path = '../test/units/plugins/inventory/test_inventory.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Check if the import 'from ansible.inventory.manager import InventoryManager' exists
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        import_found = False

        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom):
                if node.module == 'ansible.inventory.manager':
                    imported_names = {alias.name for alias in node.names}
                    if 'InventoryManager' in imported_names:
                        import_found = True

        self.assertTrue(import_found, "Import 'from ansible.inventory.manager import InventoryManager' not found in test_inventory.py")

    def test_import_split_host_pattern_exists(self):
        # Path to the file where the import should be checked
        file_path = '../test/units/plugins/inventory/test_inventory.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Check if the import 'from ansible.inventory.patterns import split_host_pattern' exists
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        import_found = False

        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom):
                if node.module == 'ansible.inventory.patterns':
                    imported_names = {alias.name for alias in node.names}
                    if 'split_host_pattern' in imported_names:
                        import_found = True

        self.assertTrue(import_found, "Import 'from ansible.inventory.patterns import split_host_pattern' not found in test_inventory.py")





if __name__ == '__main__':
    unittest.main()
