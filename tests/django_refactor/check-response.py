import unittest
import ast
import os

class TestHandlerUtils(unittest.TestCase):

    def test_check_response_function_definition(self):
        # Path to the handler_utils.py file containing check_response
        file_path = '../django/core/handlers/handler_utils.py'

        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef) and node.name == 'check_response':
                # Check if the function has the correct arguments
                args = [arg.arg for arg in node.args.args]
                self.assertIn('response', args, "Missing 'response' parameter")
                self.assertIn('callback', args, "Missing 'callback' parameter")
                
                # Check for optional parameters
                optional_args = {'name'}
                self.assertTrue(optional_args.issubset(args), "Missing optional parameter 'name'")
                
                return  # We found and checked the function, so we can stop here

        self.fail("check_response function not found in the file")

    def test_check_response_import_in_base_handler(self):
        # Path to the base.py file
        file_path = '../django/core/handlers/base.py'  

        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        # Check if check_response is imported
        import_found = False
        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom) and node.module == 'handler_utils':
                for alias in node.names:
                    if alias.name == 'check_response':
                        import_found = True
                        break

        self.assertTrue(import_found, "check_response not imported from handler_utils in base.py")

if __name__ == '__main__':
    unittest.main()
