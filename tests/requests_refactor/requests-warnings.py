import unittest
import os
import ast

class TestWarningsFile(unittest.TestCase):

    def test_warnings_file_exists(self):
        # Path to the file where the classes should be located
        file_path = '../src/requests/warnings.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

    def test_requests_warning_class_exists(self):
        # Path to the file where the class should be located
        file_path = '../src/requests/warnings.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Parse the file to check for the RequestsWarning class
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        class_found = False
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef) and node.name == 'RequestsWarning':
                class_found = True
                break

        self.assertTrue(class_found, "Class 'RequestsWarning' not found in warnings.py")

    def test_file_mode_warning_class_exists(self):
        # Path to the file where the class should be located
        file_path = '../src/requests/warnings.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Parse the file to check for the FileModeWarning class
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        class_found = False
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef) and node.name == 'FileModeWarning':
                class_found = True
                break

        self.assertTrue(class_found, "Class 'FileModeWarning' not found in warnings.py")

    def test_requests_dependency_warning_class_exists(self):
        # Path to the file where the class should be located
        file_path = '../src/requests/warnings.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Parse the file to check for the RequestsDependencyWarning class
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        class_found = False
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef) and node.name == 'RequestsDependencyWarning':
                class_found = True
                break

        self.assertTrue(class_found, "Class 'RequestsDependencyWarning' not found in warnings.py")

    def test_requests_warning_class_not_in_exceptions(self):
        # Path to the exceptions file
        file_path = '../src/requests/exceptions.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Parse the file to check that RequestsWarning is not present
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        class_found = False
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef) and node.name == 'RequestsWarning':
                class_found = True
                break

        self.assertFalse(class_found, "Class 'RequestsWarning' should not be present in exceptions.py")

    def test_file_mode_warning_class_not_in_exceptions(self):
        # Path to the exceptions file
        file_path = '../src/requests/exceptions.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Parse the file to check that FileModeWarning is not present
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        class_found = False
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef) and node.name == 'FileModeWarning':
                class_found = True
                break

        self.assertFalse(class_found, "Class 'FileModeWarning' should not be present in exceptions.py")

    def test_requests_dependency_warning_class_not_in_exceptions(self):
        # Path to the exceptions file
        file_path = '../src/requests/exceptions.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Parse the file to check that RequestsDependencyWarning is not present
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        class_found = False
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef) and node.name == 'RequestsDependencyWarning':
                class_found = True
                break

        self.assertFalse(class_found, "Class 'RequestsDependencyWarning' should not be present in exceptions.py")

    def test_init_imports_requests_dependency_warning(self):
        # Path to the __init__.py file
        file_path = '../src/requests/__init__.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Parse the file to check if the correct import is present
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        import_found = False
        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom) and node.module == 'warnings':
                for alias in node.names:
                    if alias.name == 'RequestsDependencyWarning':
                        import_found = True
                        break

        self.assertTrue(import_found, "Import 'from .warnings import RequestsDependencyWarning' not found in __init__.py")

    def test_utils_imports_file_mode_warning(self):
        # Path to the utils.py file
        file_path = '../src/requests/utils.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Parse the file to check if the correct import is present
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        import_found = False
        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom) and node.module == 'warnings':
                for alias in node.names:
                    if alias.name == 'FileModeWarning':
                        import_found = True
                        break

        self.assertTrue(import_found, "Import 'from .warnings import FileModeWarning' not found in utils.py")

if __name__ == '__main__':
    unittest.main()
