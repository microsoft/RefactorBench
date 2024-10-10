import unittest
import os
import ast

class TestCacheMigration(unittest.TestCase):

    def test_utils_py_removed(self):
        # Check if the utils.py file has been removed
        file_path = '../django/core/cache/utils.py'
        self.assertFalse(os.path.exists(file_path), f"{file_path} should be removed but still exists")

    def test_make_template_fragment_key_moved(self):
        # Path to the file where the function should be moved
        file_path = '../django/templatetags/cache.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Check if the function is defined in cache.py
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        function_found = False
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef) and node.name == 'make_template_fragment_key':
                function_found = True
                break

        self.assertTrue(function_found, "Function 'make_template_fragment_key' not found in cache.py")

    def test_template_fragment_key_template_exists(self):
        # Path to the file where the constant should be present
        file_path = '../django/templatetags/cache.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Check if the TEMPLATE_FRAGMENT_KEY_TEMPLATE constant is defined in cache.py
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        constant_found = False
        for node in ast.walk(tree):
            if isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Name) and target.id == 'TEMPLATE_FRAGMENT_KEY_TEMPLATE':
                        if isinstance(node.value, ast.Constant) and node.value.value == "template.cache.%s.%s":
                            constant_found = True
                            break
            if constant_found:
                break

        self.assertTrue(constant_found, "Constant 'TEMPLATE_FRAGMENT_KEY_TEMPLATE' with value 'template.cache.%s.%s' not found in cache.py")

    def test_docs_reference_updated(self):
        # Path to the documentation file
        docs_file_path = '../docs/topics/cache.txt'  # or .rst, adjust as needed

        # Check if the documentation file exists
        self.assertTrue(os.path.exists(docs_file_path), f"Documentation file {docs_file_path} does not exist")

        # Check if the documentation references the new location of the function
        with open(docs_file_path, 'r') as file:
            docs_content = file.read()

        old_reference = "django.core.cache.utils.make_template_fragment_key"
        new_reference = "django.templatetags.cache.make_template_fragment_key"

        self.assertNotIn(old_reference, docs_content, "Old reference to 'make_template_fragment_key' found in documentation")
        self.assertIn(new_reference, docs_content, "New reference to 'make_template_fragment_key' not found in documentation")

    def test_tests_py_imports_updated(self):
        # Path to the test file
        tests_file_path = '../tests/cache/tests.py'

        # Check if the test file exists
        self.assertTrue(os.path.exists(tests_file_path), f"Test file {tests_file_path} does not exist")

        # Check if the import statement is correct
        with open(tests_file_path, 'r') as file:
            tree = ast.parse(file.read())

        import_found = False
        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom):
                if node.module == 'django.templatetags.cache' and \
                   any(alias.name == 'make_template_fragment_key' for alias in node.names):
                    import_found = True
                    break

        self.assertTrue(import_found, "Import 'from django.templatetags.cache import make_template_fragment_key' not found in tests.py")

if __name__ == '__main__':
    unittest.main()
