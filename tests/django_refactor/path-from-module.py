import unittest
import ast
import os

class TestAppsUtils(unittest.TestCase):

    def test_path_from_module_function_definition(self):
        # Path to the apps_utils.py file containing _path_from_module
        file_path = '../django/apps/apps_utils.py'

        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef) and node.name == '_path_from_module':
                # Check if the function has the correct arguments
                args = [arg.arg for arg in node.args.args]
                self.assertIn('module', args, "Missing 'module' parameter")
                
                return  # We found and checked the function, so we can stop here

        self.fail("_path_from_module function not found in the file")

    def test_path_from_module_import_in_app_config(self):
        # Path to the file containing AppConfig class
        file_path = '../django/apps/config.py'  

        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        # Check if _path_from_module is imported
        import_found = False
        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom) and node.module == 'apps_utils':
                for alias in node.names:
                    if alias.name == '_path_from_module':
                        import_found = True
                        break

        self.assertTrue(import_found, "_path_from_module not imported from apps_utils in base.py")

if __name__ == '__main__':
    unittest.main()
