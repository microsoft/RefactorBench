import unittest
import os
import ast

class TestFastAPISecurityUtils(unittest.TestCase):

    def test_utils_file_exists(self):
        # Path to the file where the functions should be defined
        file_path = '../fastapi/security/utils.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

    def test_get_auth_scheme_param_function_exists(self):
        # Path to the file where the get_auth_scheme_param function should be defined
        file_path = '../fastapi/security/utils.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Parse the utils.py file to check for the get_auth_scheme_param function
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        get_auth_scheme_param_function = None

        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef) and node.name == 'get_auth_scheme_param':
                get_auth_scheme_param_function = node
                break

        self.assertIsNotNone(get_auth_scheme_param_function, "Function 'get_auth_scheme_param' not found in utils.py")

    def test_get_authorization_scheme_param_function_does_not_exist(self):
        # Path to the file where the get_authorization_scheme_param function might have been defined
        file_path = '../fastapi/security/utils.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Parse the utils.py file to check that get_authorization_scheme_param is no longer present
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        get_authorization_scheme_param_function = None

        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef) and node.name == 'get_authorization_scheme_param':
                get_authorization_scheme_param_function = node
                break

        self.assertIsNone(get_authorization_scheme_param_function, "Function 'get_authorization_scheme_param' is still present in utils.py, it should be renamed to 'get_auth_scheme_param'")

    def test_oauth2_file_exists(self):
        # Path to the file where the import should be checked
        file_path = '../fastapi/security/oauth2.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

    def test_import_get_auth_scheme_param(self):
        # Path to the file where the import should be checked
        file_path = '../fastapi/security/oauth2.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Parse the oauth2.py file to check for the specific import
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        import_found = False

        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom):
                if node.module == 'fastapi.security.utils':
                    imported_names = {alias.name for alias in node.names}
                    if 'get_auth_scheme_param' in imported_names:
                        import_found = True
                        break

        self.assertTrue(import_found, "'get_auth_scheme_param' not imported from 'fastapi.security.utils' in oauth2.py")

    def test_http_file_exists(self):
        # Path to the file where the import should be checked
        file_path = '../fastapi/security/http.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

    def test_import_get_auth_scheme_param(self):
        # Path to the file where the import should be checked
        file_path = '../fastapi/security/http.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Parse the http.py file to check for the specific import
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        import_found = False

        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom):
                if node.module == 'fastapi.security.utils':
                    imported_names = {alias.name for alias in node.names}
                    if 'get_auth_scheme_param' in imported_names:
                        import_found = True
                        break

        self.assertTrue(import_found, "'get_auth_scheme_param' not imported from 'fastapi.security.utils' in http.py")

    
if __name__ == '__main__':
    unittest.main()
