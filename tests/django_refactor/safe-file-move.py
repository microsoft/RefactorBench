import unittest
import ast
import os

class TestFileMoveSafeRenamed(unittest.TestCase):

    def test_function_renamed(self):
        # Path to the file containing the function definition
        file_path = '../django/core/files/move.py'

        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        # Check if the old function name exists
        old_function_name_exists = any(
            isinstance(node, ast.FunctionDef) and node.name == 'file_move_safe'
            for node in ast.walk(tree)
        )
        self.assertFalse(old_function_name_exists, "'file_move_safe' function still exists. It should be renamed.")

        # Check if the new function name exists
        new_function_name_exists = any(
            isinstance(node, ast.FunctionDef) and node.name == 'safe_file_move'
            for node in ast.walk(tree)
        )
        self.assertTrue(new_function_name_exists, "'safe_file_move' function not found.")

    def test_imports_updated(self):
        # List of files to check for updated imports
        files_to_check_imports = [
            '../django/core/cache/backends/filebased.py',
            '../django/core/files/storage/filesystem.py',
            '../tests/files/tests.py'
        ]

        for file_path in files_to_check_imports:
            with open(file_path, 'r') as f:
                tree = ast.parse(f.read())

            # Check if the old import exists
            old_import_exists = any(
                isinstance(node, ast.ImportFrom) and 
                any(alias.name == 'file_move_safe' for alias in node.names)
                for node in ast.walk(tree)
            )
            self.assertFalse(old_import_exists, f"Old import 'file_move_safe' found in {file_path}")

            # Check if the new import exists
            new_import_exists = any(
                isinstance(node, ast.ImportFrom) and 
                any(alias.name == 'safe_file_move' for alias in node.names)
                for node in ast.walk(tree)
            )
            self.assertTrue(new_import_exists, f"New import 'safe_file_move' not found in {file_path}")

    def test_function_calls_updated(self):
        # List of files to check for updated function calls
        files_to_check_calls = [
            '../django/core/cache/backends/filebased.py',
            '../django/core/files/storage/filesystem.py',
            '../tests/files/tests.py'
        ]

        for file_path in files_to_check_calls:
            with open(file_path, 'r') as f:
                tree = ast.parse(f.read())

            # Check if the old function name is called
            old_call_exists = any(
                isinstance(node, ast.Call) and 
                isinstance(node.func, ast.Name) and 
                node.func.id == 'file_move_safe'
                for node in ast.walk(tree)
            )
            self.assertFalse(old_call_exists, f"Old function call 'file_move_safe' found in {file_path}")

            # Check if the new function name is called
            new_call_exists = any(
                isinstance(node, ast.Call) and 
                isinstance(node.func, ast.Name) and 
                node.func.id == 'safe_file_move'
                for node in ast.walk(tree)
            )
            self.assertTrue(new_call_exists, f"New function call 'safe_file_move' not found in {file_path}")

    def test_documentation_updated(self):
        # Path to the documentation or release notes file
        docs_file_path = '../docs/releases/1.11.2.txt'

        with open(docs_file_path, 'r') as file:
            content = file.read()

        # Check if the term "safe_file_move" is mentioned in the file
        self.assertIn("safe_file_move", content, f"'safe_file_move' not mentioned in {docs_file_path}")

    def test_comments_updated(self):
        # Path to the file that should contain comments referencing 'safe_file_move'
        file_path = '../django/core/files/move.py'

        with open(file_path, 'r') as file:
            content = file.read()

        # Check if the comments contain the reference to 'safe_file_move'
        self.assertIn("safe_file_move", content, f"Comments do not reference 'safe_file_move' in {file_path}")

    def test_all_updated(self):
        # Path to the file that should contain '__all__' list with 'safe_file_move'
        file_path = '../django/core/files/move.py'

        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        # Check if '__all__' contains 'safe_file_move'
        all_node = next(
            (node for node in ast.walk(tree) if isinstance(node, ast.Assign) and any(target.id == '__all__' for target in node.targets)),
            None
        )
        if all_node:
            all_values = [elt.s for elt in all_node.value.elts if isinstance(elt, ast.Constant)]
            self.assertIn('safe_file_move', all_values, "'safe_file_move' not found in __all__")
        else:
            self.fail("__all__ not found in the file")

if __name__ == '__main__':
    unittest.main()
