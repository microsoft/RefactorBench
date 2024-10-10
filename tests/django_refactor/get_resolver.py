import unittest
import ast
import os

class TestGetResolverLogging(unittest.TestCase):

    def test_function_definition(self):
        # Path to the file containing get_resolver
        file_path = '../django/urls/resolvers.py'  

        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef) and node.name == 'get_resolver':
                # Check if the function has the correct arguments
                args = [arg.arg for arg in node.args.args]
                self.assertIn('urlconf', args, "Missing 'urlconf' parameter")
                
                # Check for the log parameter
                boolean_param = next(
                    (kw for kw in node.args.defaults if isinstance(kw, ast.NameConstant) and kw.value is False), 
                    None
                )
                self.assertIsNotNone(boolean_param, "Boolean parameter with default False is missing")
                
                # Check the function body for a conditional based on this boolean parameter
                boolean_check = any(
                    isinstance(stmt, ast.If) and 
                    isinstance(stmt.test, ast.Name) and 
                    isinstance(stmt.test.ctx, ast.Load) and 
                    any(arg for arg in node.args.args if arg.arg == stmt.test.id)
                    for stmt in node.body
                )
                self.assertTrue(boolean_check, "Missing boolean check in function body")
                
                return  # We found and checked the function, so we can stop here

        self.fail("get_resolver function not found in the file")

    def test_usages_have_boolean_true(self):
        # List of files to check
        files_to_check = [
            '../django/urls/base.py',
            '../django/conf/urls/i18n.py',
            '../django/core/checks/urls.py',
            '../django/core/handlers/exception.py',
            '../django/utils/autoreload.py',
            '../django/contrib/admindocs/views.py',
            '../django/core/handlers/base.py',
        ]

        for file_path in files_to_check:
            with open(file_path, 'r') as f:
                tree = ast.parse(f.read())

            for node in ast.walk(tree):
                if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == 'get_resolver':
                    boolean_arg = next((kw for kw in node.keywords if isinstance(kw.value, ast.NameConstant) and kw.value.value is True), None)
                    self.assertIsNotNone(boolean_arg, f"Boolean parameter missing or not True in {file_path}")

    def test_usages_in_tests_have_boolean_false(self):
        # List of test files to check
        test_files_to_check = [
            '../tests/urlpatterns/test_resolvers.py',
            '../tests/urlpatterns_reverse/tests.py',
            '../tests/view_tests/views.py',
        ]

        for file_path in test_files_to_check:
            with open(file_path, 'r') as f:
                tree = ast.parse(f.read())

            for node in ast.walk(tree):
                if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == 'get_resolver':
                    boolean_arg = next((kw for kw in node.keywords if isinstance(kw.value, ast.NameConstant) and kw.value.value is False), None)
                    self.assertIsNotNone(boolean_arg, f"Boolean parameter missing or not False in {file_path}")

if __name__ == '__main__':
    unittest.main()
