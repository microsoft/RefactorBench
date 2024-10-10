import unittest
import os
import ast

class TestCacheMigration(unittest.TestCase):

    def test_internal_utils_py_removed(self):
        # Check if the _internal_utils.py file has been removed
        file_path = '../src/requests/_internal_utils.py'
        self.assertFalse(os.path.exists(file_path), f"{file_path} should be removed but still exists")

    def test_internal_utils_py_not_a_file(self):
        # Check if _internal_utils.py is not a file (it should either be a directory or non-existent)
        file_path = '../src/requests/_internal_utils.py'
        self.assertFalse(os.path.isfile(file_path), f"{file_path} is still a file")

    def test_auth_py_imports_updated(self):
        # Path to the auth.py file
        file_path = '../src/requests/auth.py'
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        import_found = False
        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom):
                if node.module == 'utils' and \
                   any(alias.name == 'to_native_string' for alias in node.names):
                    import_found = True
                    break

        self.assertTrue(import_found, f"Import 'from requests.utils import to_native_string' not found in {file_path}")

    def test_cookies_py_imports_updated(self):
        # Path to the cookies.py file
        file_path = '../src/requests/cookies.py'
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        import_found = False
        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom):
                if node.module == 'utils' and \
                   any(alias.name == 'to_native_string' for alias in node.names):
                    import_found = True
                    break

        self.assertTrue(import_found, f"Import 'from requests.utils import to_native_string' not found in {file_path}")

    def test_models_py_imports_updated(self):
        # Path to the models.py file
        file_path = '../src/requests/models.py'
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        required_imports = {
            'check_header_validity',
            'get_auth_from_url',
            'guess_filename',
            'guess_json_utf',
            'iter_slices',
            'parse_header_links',
            'requote_uri',
            'stream_decode_response_unicode',
            'super_len',
            'to_key_val_list',
            'to_native_string',
            'unicode_is_ascii'
        }

        imports_found = set()
        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom):
                if node.module == 'utils':
                    for alias in node.names:
                        if alias.name in required_imports:
                            imports_found.add(alias.name)

        missing_imports = required_imports - imports_found
        self.assertTrue(not missing_imports, f"Imports from requests.utils not found in {file_path}: {missing_imports}")

    def test_sessions_py_imports_updated(self):
        # Path to the sessions.py file
        file_path = '../src/requests/sessions.py'
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        import_found = False
        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom):
                if node.module == 'utils' and \
                   any(alias.name == 'to_native_string' for alias in node.names):
                    import_found = True
                    break

        self.assertTrue(import_found, f"Import 'from requests.utils import to_native_string' not found in {file_path}")

    def test_tests_py_imports_updated(self):
        # Path to the test_utils.py file
        file_path = '../tests/test_utils.py'
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        import_found = False
        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom):
                if node.module == 'requests.utils' and \
                   any(alias.name == 'to_native_string' for alias in node.names):
                    import_found = True
                    break

        self.assertTrue(import_found, f"Import 'from requests.utils import to_native_string' not found in {file_path}")

if __name__ == '__main__':
    unittest.main()
