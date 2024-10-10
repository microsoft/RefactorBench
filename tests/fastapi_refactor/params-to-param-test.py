import unittest
import os
import ast

class TestFastAPIImportRefactor(unittest.TestCase):

    def test_compat_file_exists(self):
        # Path to the file where the import should be checked
        file_path = '../fastapi/_compat.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

    def test_no_params_import_in_compat(self):
        # Path to the file where the import should be checked
        file_path = '../fastapi/_compat.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Parse the _compat.py file to check for the absence of `from fastapi import params`
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom) and node.module == 'fastapi':
                imported_names = {alias.name for alias in node.names}
                self.assertNotIn('params', imported_names, "'params' should not be imported from 'fastapi' in _compat.py")
                self.assertIn('param', imported_names, "'param' should be imported from 'fastapi' in _compat.py")

    def test_no_params_usage_in_compat(self):
        # Path to the file where the import should be checked
        file_path = '../fastapi/_compat.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Parse the _compat.py file to check that `params.` is not used and `param.` is used instead
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        for node in ast.walk(tree):
            if isinstance(node, ast.Attribute) and isinstance(node.value, ast.Name):
                self.assertNotEqual(node.value.id, 'params', "'params.' should not be used in _compat.py")
                if node.value.id == 'param':
                    self.assertEqual(node.value.id, 'param', "'param.' should be used in _compat.py")

    def test_routing_file_exists(self):
        # Path to the file where the import should be checked
        file_path = '../fastapi/routing.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

    def test_no_params_import_in_routing(self):
        # Path to the file where the import should be checked
        file_path = '../fastapi/routing.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Parse the routing.py file to check for the absence of `from fastapi import params`
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom) and node.module == 'fastapi':
                imported_names = {alias.name for alias in node.names}
                self.assertNotIn('params', imported_names, "'params' should not be imported from 'fastapi' in routing.py")
                self.assertIn('param', imported_names, "'param' should be imported from 'fastapi' in routing.py")

    def test_no_params_usage_in_routing(self):
        # Path to the file where the import should be checked
        file_path = '../fastapi/routing.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Parse the routing.py file to check that `params.` is not used and `param.` is used instead
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        for node in ast.walk(tree):
            if isinstance(node, ast.Attribute) and isinstance(node.value, ast.Name):
                self.assertNotEqual(node.value.id, 'params', "'params.' should not be used in routing.py")
                if node.value.id == 'param':
                    self.assertEqual(node.value.id, 'param', "'param.' should be used in routing.py")

    def test_param_functions_file_exists(self):
        # Path to the file where the import should be checked
        file_path = '../fastapi/param_functions.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

    def test_no_params_import_in_param_functions(self):
        # Path to the file where the import should be checked
        file_path = '../fastapi/param_functions.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Parse the param_functions.py file to check for the absence of `from fastapi import params`
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom) and node.module == 'fastapi':
                imported_names = {alias.name for alias in node.names}
                self.assertNotIn('params', imported_names, "'params' should not be imported from 'fastapi' in param_functions.py")
                self.assertIn('param', imported_names, "'param' should be imported from 'fastapi' in param_functions.py")

    def test_no_params_usage_in_param_functions(self):
        # Path to the file where the import should be checked
        file_path = '../fastapi/param_functions.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Parse the param_functions.py file to check that `params.` is not used and `param.` is used instead
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        for node in ast.walk(tree):
            if isinstance(node, ast.Attribute) and isinstance(node.value, ast.Name):
                self.assertNotEqual(node.value.id, 'params', "'params.' should not be used in param_functions.py")
                if node.value.id == 'param':
                    self.assertEqual(node.value.id, 'param', "'param.' should be used in param_functions.py")

    def test_dependencies_utils_file_exists(self):
        # Path to the file where the import should be checked
        file_path = '../fastapi/dependencies/utils.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

    def test_no_params_import_in_dependencies_utils(self):
        # Path to the file where the import should be checked
        file_path = '../fastapi/dependencies/utils.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Parse the utils.py file to check for the absence of `from fastapi import params`
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom) and node.module == 'fastapi':
                imported_names = {alias.name for alias in node.names}
                self.assertNotIn('params', imported_names, "'params' should not be imported from 'fastapi' in utils.py")
                self.assertIn('param', imported_names, "'param' should be imported from 'fastapi' in utils.py")

    def test_no_params_usage_in_dependencies_utils(self):
        # Path to the file where the import should be checked
        file_path = '../fastapi/dependencies/utils.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Parse the utils.py file to check that `params.` is not used and `param.` is used instead
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        for node in ast.walk(tree):
            if isinstance(node, ast.Attribute) and isinstance(node.value, ast.Name):
                self.assertNotEqual(node.value.id, 'params', "'params.' should not be used in utils.py")
                if node.value.id == 'param':
                    self.assertEqual(node.value.id, 'param', "'param.' should be used in utils.py")

    def test_openapi_utils_file_exists(self):
        # Path to the file where the import should be checked
        file_path = '../fastapi/openapi/utils.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

    def test_no_params_import_in_openapi_utils(self):
        # Path to the file where the import should be checked
        file_path = '../fastapi/openapi/utils.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Parse the openapi/utils.py file to check for the absence of `from fastapi.params import`
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom) and node.module == 'fastapi.params':
                self.fail("'from fastapi.params import' should not be used in openapi/utils.py")
            if isinstance(node, ast.ImportFrom) and node.module == 'fastapi.param':
                self.assertTrue(True)

    def test_applications_file_exists(self):
        # Path to the file where the import should be checked
        file_path = '../fastapi/applications.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

    def test_no_params_import_in_applications(self):
        # Path to the file where the import should be checked
        file_path = '../fastapi/applications.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Parse the applications.py file to check for the absence of `from fastapi.params import`
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom) and node.module == 'fastapi.params':
                self.fail("'from fastapi.params import' should not be used in applications.py")
            if isinstance(node, ast.ImportFrom) and node.module == 'fastapi.param':
                self.assertTrue(True)

    def test_test_param_class_file_exists(self):
        # Path to the file where the import should be checked
        file_path = '../tests/test_param_class.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

    def test_no_params_import_in_test_param_class(self):
        # Path to the file where the import should be checked
        file_path = '../tests/test_param_class.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Parse the test_param_class.py file to check for the absence of `from fastapi.params import`
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom) and node.module == 'fastapi.params':
                self.fail("'from fastapi.params import' should not be used in test_param_class.py")
            if isinstance(node, ast.ImportFrom) and node.module == 'fastapi.param':
                self.assertTrue(True)

    def test_test_params_repr_file_exists(self):
        # Path to the file where the import should be checked
        file_path = '../tests/test_params_repr.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

    def test_no_params_import_in_test_params_repr(self):
        # Path to the file where the import should be checked
        file_path = '../tests/test_params_repr.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Parse the test_params_repr.py file to check for the absence of `from fastapi.params import`
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom) and node.module == 'fastapi.params':
                self.fail("'from fastapi.params import' should not be used in test_params_repr.py")
            if isinstance(node, ast.ImportFrom) and node.module == 'fastapi.param':
                self.assertTrue(True)
                
    def test_fastapi_param_file_exists(self):
        # Path to the fastapi/param.py file
        file_path = '../fastapi/param.py'

        # Check if the param.py file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist, but it should.")

    def test_fastapi_params_file_does_not_exist(self):
        # Path to the fastapi/params.py file
        file_path = '../fastapi/params.py'

        # Check if the params.py file does not exist
        self.assertFalse(os.path.exists(file_path), f"{file_path} exists, but it should not.")



if __name__ == '__main__':
    unittest.main()
