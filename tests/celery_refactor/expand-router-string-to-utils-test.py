import unittest
import os
import ast

class TestCeleryUtils(unittest.TestCase):

    def test_utils_file_exists(self):
        # Path to the file where the expand_router_string function should be defined
        file_path = '../celery/app/utils.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

    def test_expand_router_string_function_exists(self):
        # Path to the file where the expand_router_string function should be defined
        file_path = '../celery/app/utils.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Check if expand_router_string function is defined in utils.py
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        expand_router_string_function = None

        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef) and node.name == 'expand_router_string':
                expand_router_string_function = node
                break

        self.assertIsNotNone(expand_router_string_function, "Function 'expand_router_string' not found in utils.py")

    def test_expand_router_string_in_all_declaration(self):
        # Path to the file where the __all__ declaration should be checked
        file_path = '../celery/app/utils.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Check if expand_router_string is included in __all__ in utils.py
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        all_declaration = None

        # Look for the __all__ assignment
        for node in ast.walk(tree):
            if isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Name) and target.id == '__all__':
                        all_declaration = node
                        break
            if all_declaration:
                break

        # Verify that __all__ is found and that expand_router_string is included
        self.assertIsNotNone(all_declaration, "__all__ declaration not found in utils.py")

        # Extract the names from the __all__ declaration
        if isinstance(all_declaration.value, (ast.Tuple, ast.List)):
            all_elements = {elt.s for elt in all_declaration.value.elts if isinstance(elt, ast.Str)}
            self.assertIn('expand_router_string', all_elements, "'expand_router_string' not found in __all__ declaration in utils.py")
        else:
            self.fail("__all__ declaration is not a tuple or list in utils.py")

    def test_import_expand_router_string_in_routes(self):
        # Path to the file where the import should be checked
        file_path = '../celery/app/routes.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Parse the routes.py file to check for the specific import
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        import_found = False

        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom):
                if node.module == 'celery.app.utils':
                    imported_names = {alias.name for alias in node.names}
                    if 'expand_router_string' in imported_names:
                        import_found = True
                        break

        self.assertTrue(import_found, "'expand_router_string' not imported from 'celery.app.utils' in routes.py")

if __name__ == '__main__':
    unittest.main()
