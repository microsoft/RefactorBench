import unittest
import ast

class TestFunctionSplitting(unittest.TestCase):

    def test_models_function(self):
        # Path to the file containing the split functions
        file_path = '../django/core/management/utils.py'

        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        models_function_found = False
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                if any(arg.arg == 'labels' for arg in node.args.args):
                    # Check if the function contains logic for models
                    models_logic = any(
                        isinstance(stmt, ast.If) and "." in stmt.test.left.s
                        for stmt in ast.walk(node)
                    )
                    if models_logic:
                        models_function_found = True
                        self.assertTrue(models_logic, "Function for extracting models is missing or incorrect")
                        break

        self.assertTrue(models_function_found, "Function for extracting models not found in the file")

    def test_apps_function(self):
        # Path to the file containing the split functions
        file_path = '../django/core/management/utils.py'

        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        apps_function_found = False
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                if any(arg.arg == 'labels' for arg in node.args.args):
                    # Check if the function contains logic for apps
                    apps_logic = any(
                        isinstance(stmt, ast.If) and isinstance(stmt.test, ast.Compare) and 
                        isinstance(stmt.test.ops[0], ast.NotIn)
                        for stmt in ast.walk(node)
                    )
                    if apps_logic:
                        apps_function_found = True
                        self.assertTrue(apps_logic, "Function for extracting apps is missing or incorrect")
                        break

        self.assertTrue(apps_function_found, "Function for extracting apps not found in the file")

    def test_original_function_absent(self):
        # Path to the file containing the original function
        file_path = '../django/core/management/utils.py'

        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        original_function_found = False
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef) and node.name == 'parse_apps_and_model_labels':
                original_function_found = True
                break

        self.assertFalse(original_function_found, "Original function 'parse_apps_and_model_labels' should not be present after refactoring")

    def test_import_of_new_functions(self):
        # Paths to the files that should import the new functions
        files_to_check = [
            '../django/core/management/commands/loaddata.py',
            '../django/core/management/commands/dumpdata.py',
        ]

        for file_path in files_to_check:
            with open(file_path, 'r') as file:
                tree = ast.parse(file.read())

            imports_models = False
            imports_apps = False

            for node in ast.walk(tree):
                if isinstance(node, ast.ImportFrom):
                    for alias in node.names:
                        if alias.name == 'get_models_from_labels':
                            imports_models = True
                        if alias.name == 'get_apps_from_labels':
                            imports_apps = True

            self.assertTrue(imports_models, f"'get_models_from_labels' not imported in {file_path}")
            self.assertTrue(imports_apps, f"'get_apps_from_labels' not imported in {file_path}")

    def test_usage_of_new_functions(self):
        # Paths to the files that should use the new functions
        files_to_check = [
            '../django/core/management/commands/loaddata.py',
            '../django/core/management/commands/dumpdata.py',
        ]

        for file_path in files_to_check:
            with open(file_path, 'r') as file:
                tree = ast.parse(file.read())

            uses_models_function = False
            uses_apps_function = False

            for node in ast.walk(tree):
                if isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
                    if node.func.id == 'get_models_from_labels':
                        uses_models_function = True
                    if node.func.id == 'get_apps_from_labels':
                        uses_apps_function = True

            self.assertTrue(uses_models_function, f"'get_models_from_labels' not used in {file_path}")
            self.assertTrue(uses_apps_function, f"'get_apps_from_labels' not used in {file_path}")

if __name__ == '__main__':
    unittest.main()
