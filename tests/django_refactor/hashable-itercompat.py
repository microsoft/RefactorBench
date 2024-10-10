import unittest
import ast
import os

class TestUtilsMigration(unittest.TestCase):

    def setUp(self):
        # Paths to the old and new files
        self.hashable_file_path = '../django/utils/hashable.py'
        self.itercompat_file_path = '../django/utils/itercompat.py'
        self.able_file_path = '../django/utils/able.py'

        self.files_to_check = [
            '../django/contrib/admin/utils.py',
            '../django/core/exceptions.py',
            '../django/db/models/base.py',
            '../django/db/models/expressions.py',
            '../django/db/models/fields/reverse_related.py',
            '../django/db/models/lookups.py',
            '../django/db/models/query_utils.py',
            '../django/db/models/sql/compiler.py',
            '../django/forms/models.py',
            '../django/utils/tree.py',
        ]

        self.combined_test_file_path = '../tests/utils_tests/test_able.py'

    def test_old_files_deleted(self):
        # Check if hashable.py, itercompat.py, test_hashable.py, and test_itercompat.py files have been deleted
        self.assertFalse(os.path.exists(self.hashable_file_path), "hashable.py should be deleted")
        self.assertFalse(os.path.exists(self.itercompat_file_path), "itercompat.py should be deleted")
        self.assertFalse(os.path.exists('../tests/utils_tests/test_hashable.py'), "test_hashable.py should be deleted")
        self.assertFalse(os.path.exists('../tests/utils_tests/test_itercompat.py'), "test_itercompat.py should be deleted")

    def test_functions_moved_to_able(self):
        with open(self.able_file_path, 'r') as file:
            able_tree = ast.parse(file.read())

        functions_in_able = {
            node.name
            for node in ast.walk(able_tree)
            if isinstance(node, ast.FunctionDef)
        }

        necessary_functions = [
            'make_hashable',
            'is_iterable'
        ]

        for func in necessary_functions:
            self.assertIn(func, functions_in_able, f"{func} not found in able.py")

    def test_make_hashable_imports_updated(self):
        for file_path in self.files_to_check:
            with self.subTest(file=file_path):
                with open(file_path, 'r') as file:
                    tree = ast.parse(file.read())

                imported_names = {
                    alias.name for node in ast.walk(tree)
                    if isinstance(node, ast.ImportFrom) and node.module == 'django.utils.able'
                    for alias in node.names
                }

                self.assertIn('make_hashable', imported_names, f"make_hashable not imported from able in {file_path}")

                # Ensure 'hashable' is not imported
                old_import_found = any(
                    isinstance(node, ast.ImportFrom) and node.module == 'django.utils.hashable'
                    for node in ast.walk(tree)
                )
                self.assertFalse(old_import_found, f"hashable should not be imported in {file_path}")

    def test_is_iterable_imports_updated(self):
        with open(self.combined_test_file_path, 'r') as file:
            tree = ast.parse(file.read())

        imported_names = {
            alias.name for node in ast.walk(tree)
            if isinstance(node, ast.ImportFrom) and node.module == 'django.utils.able'
            for alias in node.names
        }

        self.assertIn('is_iterable', imported_names, f"is_iterable not imported from able in {self.combined_test_file_path}")

        # Ensure 'itercompat' is not imported
        old_import_found = any(
            isinstance(node, ast.ImportFrom) and node.module == 'django.utils.itercompat'
            for node in ast.walk(tree)
        )
        self.assertFalse(old_import_found, f"itercompat should not be imported in {self.combined_test_file_path}")

if __name__ == '__main__':
    unittest.main()
