import unittest
import os
import ast

class TestFastAPICompatUtils(unittest.TestCase):

    def test_compat_file_exists(self):
        # Path to the file where the functions should be defined
        file_path = '../fastapi/_compat.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

    def test_value_is_a_sequence_function_exists(self):
        # Path to the file where the value_is_a_sequence function should be defined
        file_path = '../fastapi/_compat.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Parse the _compat.py file to check for the value_is_a_sequence function
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        value_is_a_sequence_function = None

        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef) and node.name == 'value_is_a_sequence':
                value_is_a_sequence_function = node
                break

        self.assertIsNotNone(value_is_a_sequence_function, "Function 'value_is_a_sequence' not found in _compat.py")

    def test_value_is_sequence_function_does_not_exist(self):
        # Path to the file where the value_is_sequence function might have been defined
        file_path = '../fastapi/_compat.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Parse the _compat.py file to check that value_is_sequence is no longer present
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        value_is_sequence_function = None

        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef) and node.name == 'value_is_sequence':
                value_is_sequence_function = node
                break

        self.assertIsNone(value_is_sequence_function, "Function 'value_is_sequence' is still present in _compat.py, it should be renamed to 'value_is_a_sequence'")

    def test_import_value_is_a_sequence_in_utils(self):
        # Path to the file where the import should be checked
        file_path = '../fastapi/dependencies/utils.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Parse the utils.py file to check for the specific import
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        import_found = False

        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom):
                if node.module == 'fastapi._compat':
                    imported_names = {alias.name for alias in node.names}
                    if 'value_is_a_sequence' in imported_names:
                        import_found = True
                        break

        self.assertTrue(import_found, "'value_is_a_sequence' not imported from 'fastapi._compat' in dependencies/utils.py")

    def test_value_is_sequence_function_does_not_exist_in_utils(self):
        # Path to the file where the value_is_sequence function might have been defined
        file_path = '../fastapi/dependencies/utils.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Parse the utils.py file to check that value_is_sequence is no longer present
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        value_is_sequence_function = None

        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef) and node.name == 'value_is_sequence':
                value_is_sequence_function = node
                break

        self.assertIsNone(value_is_sequence_function, "Function 'value_is_sequence' is still present in utils.py, it should be renamed to 'value_is_a_sequence'")

if __name__ == '__main__':
    unittest.main()
