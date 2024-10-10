import unittest
import os
import ast

class TestCeleryUtils(unittest.TestCase):

    def test_ensure_serialize_function_exists(self):
        # Path to the file where the ensure_serialize function should be defined
        file_path = '../celery/utils/serialization.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Check if ensure_serialize function is defined in serialization.py
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        ensure_serialize_function = None

        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef) and node.name == 'ensure_serialize':
                ensure_serialize_function = node
                break

        self.assertIsNotNone(ensure_serialize_function, "Function 'ensure_serialize' not found in serialization.py")

    def test_ensure_serialization_function_does_not_exist(self):
        # Path to the file where the ensure_serialization function should not be defined
        file_path = '../celery/utils/serialization.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Check if ensure_serialization function is not defined in serialization.py
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        ensure_serialization_function = None

        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef) and node.name == 'ensure_serialization':
                ensure_serialization_function = node
                break

        self.assertIsNone(ensure_serialization_function, "Function 'ensure_serialization' should not be present in serialization.py")

    def test_ensure_serialize_usage_count(self):
        # Path to the file where the ensure_serialize function usage should be checked
        file_path = '../celery/utils/serialization.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Parse the serialization.py file to count the usages of ensure_serialize
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        ensure_serialize_usages = 0

        for node in ast.walk(tree):
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == 'ensure_serialize':
                ensure_serialize_usages += 1

        self.assertEqual(ensure_serialize_usages, 1, "There should be exactly one usage of 'ensure_serialize' in serialization.py")

    def test_required_imports_in_base(self):
        # Path to the file where the imports should be checked
        file_path = '../celery/backends/base.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Parse the base.py file to check for the required imports
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        required_imports = {
            'create_exception_cls': False,
            'ensure_serialize': False,
            'get_pickleable_exception': False,
            'get_pickled_exception': False,
            'raise_with_context': False,
        }

        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom) and node.module == 'celery.utils.serialization':
                for name in node.names:
                    if name.name in required_imports:
                        required_imports[name.name] = True

        for import_name, is_imported in required_imports.items():
            self.assertTrue(is_imported, f"'{import_name}' is not imported from 'celery.utils.serialization' in base.py")

    def test_class_test_ensure_serialize_exists(self):
        # Path to the file where the test_ensure_serialize class should be defined
        file_path = '../t/unit/utils/test_serialization.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Parse the test_serialization.py file to check for the class definition
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        class_found = False
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef) and node.name == 'test_ensure_serialize':
                class_found = True
                break

        self.assertTrue(class_found, "Class 'test_ensure_serialize' not found in test_serialization.py")

    def test_methods_exist_in_test_ensure_serialize(self):
        # Path to the file where the methods should be defined in the test_ensure_serialize class
        file_path = '../t/unit/utils/test_serialization.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Parse the test_serialization.py file to check for the method definitions
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        methods_found = {'test_json_py3': False, 'test_pickle': False}
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef) and node.name == 'test_ensure_serialize':
                for method in node.body:
                    if isinstance(method, ast.FunctionDef):
                        if method.name in methods_found:
                            methods_found[method.name] = True
                break

        for method_name, found in methods_found.items():
            self.assertTrue(found, f"Method '{method_name}' not found in class 'test_ensure_serialize'")

    def test_ensure_serialize_used_in_methods(self):
        # Path to the file where the ensure_serialize function usage should be checked in the test methods
        file_path = '../t/unit/utils/test_serialization.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Parse the test_serialization.py file to check for ensure_serialize usage
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        ensure_serialize_usage_found = {'test_json_py3': False, 'test_pickle': False}
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef) and node.name == 'test_ensure_serialize':
                for method in node.body:
                    if isinstance(method, ast.FunctionDef):
                        for subnode in ast.walk(method):
                            if isinstance(subnode, ast.Call) and isinstance(subnode.func, ast.Name) and subnode.func.id == 'ensure_serialize':
                                ensure_serialize_usage_found[method.name] = True
                break

        for method_name, found in ensure_serialize_usage_found.items():
            self.assertTrue(found, f"'ensure_serialize' not used in method '{method_name}'")

    def test_required_imports_in_test_serialization(self):
        # Path to the file where the imports should be checked
        file_path = '../t/unit/utils/test_serialization.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Parse the test_serialization.py file to check for the required imports
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        required_imports = {
            'STRTOBOOL_DEFAULT_TABLE': False,
            'UnpickleableExceptionWrapper': False,
            'ensure_serialize': False,
            'get_pickleable_etype': False,
            'jsonify': False,
            'strtobool': False,
        }

        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom) and node.module == 'celery.utils.serialization':
                for name in node.names:
                    if name.name in required_imports:
                        required_imports[name.name] = True

        for import_name, is_imported in required_imports.items():
            self.assertTrue(is_imported, f"'{import_name}' is not imported from 'celery.utils.serialization' in test_serialization.py")

    def test_serialization_ensure_serialize_used_in_test_base(self):
        # Path to the file where serialization.ensure_serialize usage should be checked
        file_path = '../t/unit/backends/test_base.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Parse the test_base.py file to check for serialization.ensure_serialize usage
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        ensure_serialize_usage_found = False

        for node in ast.walk(tree):
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute):
                if (isinstance(node.func.value, ast.Name) and node.func.value.id == 'serialization' 
                    and node.func.attr == 'ensure_serialize'):
                    ensure_serialize_usage_found = True
                    break

        self.assertTrue(ensure_serialize_usage_found, "'serialization.ensure_serialize' not used in test_base.py")


    
if __name__ == '__main__':
    unittest.main()
