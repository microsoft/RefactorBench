import unittest
import os
import ast

class TestCelerySerializationUtils(unittest.TestCase):

    def test_serialization_utils_file_exists(self):
        # Path to the file where the evaluate_promises function should be defined
        file_path = '../celery/utils/serialization.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

    def test_evaluate_promises_function_exists(self):
        # Path to the file where the evaluate_promises function should be defined
        file_path = '../celery/utils/serialization.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Check if evaluate_promises function is defined in serialization.py
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        evaluate_promises_function = None

        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef) and node.name == 'evaluate_promises':
                evaluate_promises_function = node
                break

        self.assertIsNotNone(evaluate_promises_function, "Function 'evaluate_promises' not found in serialization.py")


    def test_import_evaluate_promises(self):
        # Path to the file where the import should be checked
        file_path = '../celery/utils/functional.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Parse the serialization.py file to check for the specific import
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        import_found = False

        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom):
                if node.module == 'celery.utils.serialization':
                    imported_names = {alias.name for alias in node.names}
                    if 'evaluate_promises' in imported_names:
                        import_found = True
                        break

        self.assertTrue(import_found, "'evaluate_promises' not imported from 'celery.utils.serialization' in functional.py")

    def test_import_promise_from_vine(self):
        # Path to the file where the import should be checked
        file_path = '../celery/utils/serialization.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Parse the serialization.py file to check for the specific import
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        import_found = False

        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom) and node.module == 'vine':
                imported_names = {alias.name for alias in node.names}
                if 'promise' in imported_names:
                    import_found = True
                    break

        self.assertTrue(import_found, "'promise' not imported from 'vine' in serialization.py")

    
if __name__ == '__main__':
    unittest.main()
