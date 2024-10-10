import unittest
import os
import ast

class TestCeleryRegistry(unittest.TestCase):
    
    def test_unpickle_task_exists(self):
        # Path to the file where the _unpickle_task function should be defined
        file_path = '../celery/app/registry.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Parse the registry.py file to check for the _unpickle_task function
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        unpickle_task_function = None

        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef) and node.name == '_unpickle_task':
                unpickle_task_function = node
                break

        self.assertIsNotNone(unpickle_task_function, "Function '_unpickle_task' not found in registry.py")

    def test_unpickle_task_v2_not_exists(self):
        # Path to the file where the _unpickle_task_v2 function should be defined
        file_path = '../celery/app/registry.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Parse the registry.py file to check for the _unpickle_task_v2 function
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        unpickle_task_v2_function = None

        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef) and node.name == '_unpickle_task_v2':
                unpickle_task_v2_function = node
                break

        self.assertIsNone(unpickle_task_v2_function, "Function '_unpickle_task_v2' was found in registry.py, but it should not exist")

    def test_import_unpickle_task_in_task_py(self):
        # Path to the task.py file
        file_path = '../celery/app/task.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Parse the task.py file to check for the specific import
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        import_found = False

        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom):
                if node.module == 'registry':
                    imported_names = {alias.name for alias in node.names}
                    if '_unpickle_task' in imported_names:
                        import_found = True
                        break

        self.assertTrue(import_found, "'from .registry import _unpickle_task' not found in task.py")

    def test_import_unpickle_task_in_test_registry(self):
        # Path to the test_registry.py file
        file_path = '../t/unit/app/test_registry.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Parse the test_registry.py file to check for the specific import
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        import_found = False

        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom):
                if node.module == 'celery.app.registry':
                    imported_names = {alias.name for alias in node.names}
                    if '_unpickle_task' in imported_names:
                        import_found = True
                        break

        self.assertTrue(import_found, "'from celery.app.registry import _unpickle_task' not found in test_registry.py")

    def test_class_test_unpickle_test_exists(self):
        # Path to the test_registry.py file
        file_path = '../t/unit/app/test_registry.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Parse the test_registry.py file to check for the TestUnpickleTest class
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        class_found = False

        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef) and node.name == 'test_unpickle_task':
                class_found = True
                break

        self.assertTrue(class_found, "Class 'test_unpickle_task' not found in test_registry.py")

    def test_function_test_unpickle_exists_in_test_unpickle_test(self):
        # Path to the test_registry.py file
        file_path = '../t/unit/app/test_registry.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Parse the test_registry.py file to check for the test_unpickle function within TestUnpickleTest class
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        test_unpickle_function_found = False

        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef) and node.name == 'test_unpickle_task':
                for class_node in node.body:
                    if isinstance(class_node, ast.FunctionDef) and class_node.name == 'test_unpickle':
                        test_unpickle_function_found = True
                        break
                break

        self.assertTrue(test_unpickle_function_found, "Function 'test_unpickle' not found in class 'TestUnpickleTest' in test_registry.py")



if __name__ == '__main__':
    unittest.main()
