import unittest
import os
import ast
class TestAnsibleInventory(unittest.TestCase):

    def test_inventory_data_exists(self):
        # Path to the directory where inventory_data.py should be located
        directory_path = '../lib/ansible/inventory/'

        # Path to the specific files to be checked
        inventory_data_file = os.path.join(directory_path, 'inventory_data.py')
        data_file = os.path.join(directory_path, 'data.py')

        # Check if inventory_data.py exists
        self.assertTrue(os.path.exists(inventory_data_file), f"{inventory_data_file} does not exist")

    def test_data_py_does_not_exist(self):
        # Path to the directory where data.py should be checked
        directory_path = '../lib/ansible/inventory/'

        # Path to the specific file to be checked
        data_file = os.path.join(directory_path, 'data.py')

        # Check if data.py does not exist
        self.assertFalse(os.path.exists(data_file), f"{data_file} should not exist")

    def test_manager_py_imports_inventory_data(self):
        # Path to the manager.py file
        manager_file_path = '../lib/ansible/inventory/manager.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(manager_file_path), f"{manager_file_path} does not exist")

        # The line we expect to find in manager.py
        expected_import_line = 'from ansible.inventory.inventory_data import InventoryData'

        # Check if the expected import line is in the file
        with open(manager_file_path, 'r') as file:
            file_content = file.read()

        self.assertIn(expected_import_line, file_content, f"'{expected_import_line}' not found in {manager_file_path}")

    def test_inventory_data_has_inventorydata_class(self):
        # Path to the inventory_data.py file
        inventory_data_file_path = '../lib/ansible/inventory/inventory_data.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(inventory_data_file_path), f"{inventory_data_file_path} does not exist")

        # Parse the inventory_data.py file and check if it contains a class named InventoryData
        with open(inventory_data_file_path, 'r') as file:
            tree = ast.parse(file.read())

        class_found = False

        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef) and node.name == 'InventoryData':
                class_found = True
                break

        self.assertTrue(class_found, f"Class 'InventoryData' not found in {inventory_data_file_path}")

    def test_constructed_py_imports_inventory_data(self):
        # Path to the test_constructed.py file
        constructed_file_path = '../test/units/plugins/inventory/test_constructed.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(constructed_file_path), f"{constructed_file_path} does not exist")

        # The line we expect to find in test_constructed.py
        expected_import_line = 'from ansible.inventory.inventory_data import InventoryData'

        # Check if the expected import line is in the file
        with open(constructed_file_path, 'r') as file:
            file_content = file.read()

        self.assertIn(expected_import_line, file_content, f"'{expected_import_line}' not found in {constructed_file_path}")

if __name__ == '__main__':
    unittest.main()