import unittest
import os
import ast

class TestClassRenaming(unittest.TestCase):

    def test_class_renamed_to_DictLookup(self):
        # Path to the file where the class should be located
        file_path = '../src/requests/structures.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Parse the file to check the class definition
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        class_found = False

        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef) and node.name == 'DictLookup':
                class_found = True
                break

        self.assertTrue(class_found, "Class 'DictLookup' not found in the file")
    
    def test_no_LookupDict_class(self):
        # Path to the file where the class should have been located
        file_path = '../src/requests/structures.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Parse the file to ensure LookupDict class no longer exists
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        class_found = False

        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef) and node.name == 'LookupDict':
                class_found = True
                break

        self.assertFalse(class_found, "Class 'LookupDict' should not be present in the file")

    def test_usage_of_DictLookup(self):
        # Path to the file where the class usage should be located
        usage_file_path = '../src/requests/status_codes.py'  

        # Check if the file exists
        self.assertTrue(os.path.exists(usage_file_path), f"{usage_file_path} does not exist")

        # Parse the file to check the usage of the class
        with open(usage_file_path, 'r') as file:
            tree = ast.parse(file.read())

        class_used = False

        for node in ast.walk(tree):
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == 'DictLookup':
                class_used = True
                break

        self.assertTrue(class_used, "Class 'DictLookup' is not used where it should be")
    
    def test_DictLookup_imported_in_status_codes(self):
        # Path to the file where DictLookup should be imported
        file_path = '../src/requests/status_codes.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Parse the file to check the import statement
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        dictlookup_imported = False

        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom) and node.module == 'structures':
                for alias in node.names:
                    if alias.name == 'DictLookup':
                        dictlookup_imported = True
                        break
                if dictlookup_imported:
                    break

        self.assertTrue(dictlookup_imported, "'DictLookup' is not imported from 'structures' in status_codes.py")
    
    def test_specific_import_in_test_structures(self):
        # Path to the test file
        test_file_path = '../tests/test_structures.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(test_file_path), f"{test_file_path} does not exist")

        # Parse the file to check the specific import statement
        with open(test_file_path, 'r') as file:
            tree = ast.parse(file.read())

        specific_import_found = False

        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom) and node.module == 'requests.structures':
                imported_names = {alias.name for alias in node.names}
                if 'CaseInsensitiveDict' in imported_names and 'DictLookup' in imported_names:
                    specific_import_found = True
                    break

        self.assertTrue(specific_import_found, "The specific import 'from requests.structures import CaseInsensitiveDict, DictLookup' is not found in test_structures.py")
    
    def test_DictLookup_used_in_status_codes(self):
        # Path to the status_codes file
        status_codes_file_path = '../src/requests/status_codes.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(status_codes_file_path), f"{status_codes_file_path} does not exist")

        # Parse the file to check if DictLookup is used
        with open(status_codes_file_path, 'r') as file:
            tree = ast.parse(file.read())

        dictlookup_used = False

        for node in ast.walk(tree):
            if isinstance(node, ast.Name) and node.id == 'DictLookup':
                dictlookup_used = True
                break

        self.assertTrue(dictlookup_used, "'DictLookup' is not used in status_codes.py")
    
    def test_DictLookup_used_in_test_structures(self):
        # Path to the test_structures file
        test_structures_file_path = '../tests/test_structures.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(test_structures_file_path), f"{test_structures_file_path} does not exist")

        # Parse the file to check if DictLookup is used
        with open(test_structures_file_path, 'r') as file:
            tree = ast.parse(file.read())

        dictlookup_used = False

        for node in ast.walk(tree):
            if isinstance(node, ast.Name) and node.id == 'DictLookup':
                dictlookup_used = True
                break

        self.assertTrue(dictlookup_used, "'DictLookup' is not used in test_structures.py")

if __name__ == '__main__':
    unittest.main()
