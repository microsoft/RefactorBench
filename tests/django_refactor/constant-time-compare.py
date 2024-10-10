import unittest
import ast
import os

class TestConstantTimeCompareLogging(unittest.TestCase):

    def test_function_definition(self):
        # Path to the file containing constant_time_compare
        file_path = '../django/utils/crypto.py'

        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef) and node.name == 'constant_time_compare':
                # Check if the function has the correct arguments
                args = [arg.arg for arg in node.args.args]
                self.assertIn('log', args, "Missing 'log' parameter")
                
                # Check for the log parameter default value
                boolean_param = next(
                    (kw for kw in node.args.defaults if isinstance(kw, ast.Constant) and kw.value is False), 
                    None
                )
                self.assertIsNotNone(boolean_param, "Boolean parameter 'log' with default False is missing")
                
                # Check the function body for a conditional based on this boolean parameter
                boolean_check = any(
                    isinstance(stmt, ast.If) and 
                    isinstance(stmt.test, ast.Name) and 
                    stmt.test.id == 'log'
                    for stmt in node.body
                )
                self.assertTrue(boolean_check, "Missing boolean check for 'log' in function body")
                
                return  # We found and checked the function, so we can stop here

        self.fail("constant_time_compare function not found in the file")

    def test_usages_have_boolean_true(self):
        # List of files to check
        files_to_check = [
            '../django/contrib/auth/__init__.py',
            '../django/contrib/auth/hashers.py',
            '../django/contrib/auth/tokens.py',
            '../django/core/signing.py',
            '../django/middleware/csrf.py',
        ]

        for file_path in files_to_check:
            with open(file_path, 'r') as f:
                tree = ast.parse(f.read())

            for node in ast.walk(tree):
                if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == 'constant_time_compare':
                    boolean_arg = next((kw for kw in node.keywords if isinstance(kw.value, ast.Constant) and kw.value.value is True), None)
                    self.assertIsNotNone(boolean_arg, f"Boolean parameter 'log' missing or not True in {file_path}")

    def test_usages_in_tests_have_boolean_false(self):
        # List of test files to check
        test_files_to_check = [
            '../tests/utils_tests/test_crypto.py',
        ]

        for file_path in test_files_to_check:
            with open(file_path, 'r') as f:
                tree = ast.parse(f.read())

            for node in ast.walk(tree):
                if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == 'constant_time_compare':
                    boolean_arg = next((kw for kw in node.keywords if isinstance(kw.value, ast.Constant) and kw.value.value is False), None)
                    self.assertIsNotNone(boolean_arg, f"Boolean parameter 'log' missing or not False in {file_path}")

if __name__ == '__main__':
    unittest.main()
