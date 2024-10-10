import unittest
import os
import ast

class TestFunctionRenaming(unittest.TestCase):

    def test_super_len_renamed_to_complex_len(self):
        # List of files to check
        files_to_check = [
            '../src/requests/models.py',
            '../tests/test_utils.py',
        ]

        for file_path in files_to_check:
            # Check if the file exists
            self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

            # Check if the import has been updated
            with open(file_path, 'r') as file:
                tree = ast.parse(file.read())

            import_updated = False
            for node in ast.walk(tree):
                if isinstance(node, ast.ImportFrom):
                    # Check if there was an import of super_len and it got renamed to complex_len
                    if any(alias.name == 'complex_len' for alias in node.names):
                        import_updated = True
                        break

            self.assertTrue(import_updated, f"Import of 'complex_len' not found in {file_path}, it might still be using 'super_len'")

    def test_super_len_function_removed(self):
        # Path to the file where super_len was originally defined
        original_file_path = '../src/requests/utils.py'

        # Check if the function super_len is no longer defined in the file
        self.assertTrue(os.path.exists(original_file_path), f"{original_file_path} does not exist")

        with open(original_file_path, 'r') as file:
            tree = ast.parse(file.read())

        function_still_exists = False
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef) and node.name == 'super_len':
                function_still_exists = True
                break

        self.assertFalse(function_still_exists, "Function 'super_len' still exists, it should have been removed or renamed to 'complex_len'")

    def test_complex_len_function_exists(self):
        # Path to the file where complex_len should be defined
        new_file_path = '../src/requests/utils.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(new_file_path), f"{new_file_path} does not exist")

        # Check if the function complex_len is defined in the file
        with open(new_file_path, 'r') as file:
            tree = ast.parse(file.read())

        function_found = False
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef) and node.name == 'complex_len':
                function_found = True
                break

        self.assertTrue(function_found, "Function 'complex_len' not found in the expected file")

if __name__ == '__main__':
    unittest.main()
