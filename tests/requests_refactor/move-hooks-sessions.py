import unittest
import os
import ast

class TestHooksMigration(unittest.TestCase):

    def test_hooks_py_removed(self):
        # Path to the hooks.py file that should be removed
        file_path = '../src/requests/hooks.py'

        # Check if the file does not exist
        self.assertFalse(os.path.exists(file_path), f"{file_path} should not exist")

    def test_default_hooks_in_sessions(self):
        # Path to the sessions.py file where the function should be located
        file_path = '../src/requests/sessions.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Parse the file to check if the default_hooks function is defined
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        function_found = False
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef) and node.name == 'default_hooks':
                function_found = True
                break

        self.assertTrue(function_found, "Function 'default_hooks' not found in sessions.py")

    def test_dispatch_hook_in_sessions(self):
        # Path to the sessions.py file where the function should be located
        file_path = '../src/requests/sessions.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Parse the file to check if the dispatch_hook function is defined
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        function_found = False
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef) and node.name == 'dispatch_hook':
                function_found = True
                break

        self.assertTrue(function_found, "Function 'dispatch_hook' not found in sessions.py")

    def test_models_imports_default_hooks(self):
        # Path to the models.py file where the import should be located
        file_path = '../src/requests/models.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Parse the file to check if default_hooks is imported from sessions
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        import_found = False
        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom):
                if node.module == 'sessions':
                    for alias in node.names:
                        if alias.name == 'default_hooks':
                            import_found = True
                            break

        self.assertTrue(import_found, "Import 'from requests.sessions import default_hooks' not found in models.py")

    def test_test_requests_imports(self):
        # Path to the test_requests.py file where the imports should be located
        file_path = '../tests/test_requests.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Parse the file to check if SessionRedirectMixin and default_hooks are imported from sessions
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        session_redirect_mixin_found = False
        default_hooks_found = False

        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom):
                if node.module == 'requests.sessions':
                    for alias in node.names:
                        if alias.name == 'SessionRedirectMixin':
                            session_redirect_mixin_found = True
                        if alias.name == 'default_hooks':
                            default_hooks_found = True

        self.assertTrue(session_redirect_mixin_found, "Import 'from requests.sessions import SessionRedirectMixin' not found in test_requests.py")
        self.assertTrue(default_hooks_found, "Import 'from requests.sessions import default_hooks' not found in test_requests.py")

    def test_test_hooks_imports_sessions(self):
        # Path to the test_hooks.py file where the import should be located
        file_path = '../tests/test_hooks.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Parse the file to check if sessions is imported from requests
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        import_found = False
        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom):
                if node.module == 'requests' and any(alias.name == 'sessions' for alias in node.names):
                    import_found = True
                    break

        self.assertTrue(import_found, "Import 'from requests import sessions' not found in test_hooks.py")
        
    def test_sessions_does_not_import_from_hooks(self):
        # Path to the sessions.py file where the import should not be located
        file_path = '../src/requests/sessions.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Parse the file to check if there is an import from hooks
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        import_found = False
        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom) and node.module == 'requests.hooks':
                import_found = True
                break

        self.assertFalse(import_found, "Import 'from requests.hooks import ...' found in sessions.py, which should not be present")


if __name__ == '__main__':
    unittest.main()
