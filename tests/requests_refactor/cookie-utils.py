import unittest
import os
import ast

class TestCookieUtilsMigration(unittest.TestCase):

    def test_cookie_utils_class_exists(self):
        # Path to the file where the CookieUtils class should be defined
        file_path = '../src/requests/cookies.py'  # adjust as needed

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Check if the CookieUtils class is defined in cookies.py
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        class_found = False
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef) and node.name == 'CookieUtils':
                class_found = True
                break

        self.assertTrue(class_found, "Class 'CookieUtils' not found in cookies.py")

    def test_functions_in_cookie_utils(self):
        # Path to the file where the CookieUtils class should be defined
        file_path = '../src/requests/cookies.py'  # adjust as needed

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Expected functions that should be in the CookieUtils class
        expected_functions = [
            'extract_cookies_to_jar',
            'get_cookie_header',
            'remove_cookie_by_name',
            'cookiejar_from_dict',
            'merge_cookies',
            '_copy_cookie_jar',
            'create_cookie',
            'morsel_to_cookie'
        ]

        # Check if the functions are defined in the CookieUtils class
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        functions_found = {func: False for func in expected_functions}

        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef) and node.name == 'CookieUtils':
                for class_node in ast.walk(node):
                    if isinstance(class_node, ast.FunctionDef) and class_node.name in functions_found:
                        functions_found[class_node.name] = True

        missing_functions = [func for func, found in functions_found.items() if not found]

        self.assertFalse(missing_functions, f"Functions {missing_functions} not found in CookieUtils class")

    def test_file_imports_cookie_utils(self):
        # List of files where CookieUtils should be imported
        files_to_check = [
            '../src/requests/adapters.py',
            '../src/requests/auth.py',
            '../src/requests/models.py',
            '../src/requests/sessions.py',
            '../src/requests/utils.py',
        ]

        # Iterate through each file and check for the import statement
        for test_file_path in files_to_check:
            with self.subTest(test_file_path=test_file_path):
                # Check if the file exists
                self.assertTrue(os.path.exists(test_file_path), f"Test file {test_file_path} does not exist")

                # Check if the import statement for CookieUtils is correct
                with open(test_file_path, 'r') as file:
                    tree = ast.parse(file.read())

                import_found = False
                for node in ast.walk(tree):
                    if isinstance(node, ast.ImportFrom):
                        if node.module == 'cookies' and \
                           any(alias.name == 'CookieUtils' for alias in node.names):
                            import_found = True
                            break

                self.assertTrue(import_found, f"Import 'from requests.cookies import CookieUtils' not found in {test_file_path}")

    def test_file_imports_cookie_utils_tests(self):
        # List of files where CookieUtils should be imported
        files_to_check = [
            '../tests/test_requests.py'
        ]

        # Iterate through each file and check for the import statement
        for test_file_path in files_to_check:
            with self.subTest(test_file_path=test_file_path):
                # Check if the file exists
                self.assertTrue(os.path.exists(test_file_path), f"Test file {test_file_path} does not exist")

                # Check if the import statement for CookieUtils is correct
                with open(test_file_path, 'r') as file:
                    tree = ast.parse(file.read())

                import_found = False
                for node in ast.walk(tree):
                    if isinstance(node, ast.ImportFrom):
                        if node.module == 'requests.cookies' and \
                           any(alias.name == 'CookieUtils' for alias in node.names):
                            import_found = True
                            break

                self.assertTrue(import_found, f"Import 'from requests.cookies import CookieUtils' not found in {test_file_path}")


if __name__ == '__main__':
    unittest.main()
