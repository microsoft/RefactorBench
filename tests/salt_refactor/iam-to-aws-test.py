import unittest
import os
import ast

class TestSaltUtilsAWS(unittest.TestCase):

    def test_aws_py_exists(self):
        file_path = '../salt/utils/aws.py'
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

    def test_aws_py_imports_pprint(self):
        file_path = '../salt/utils/aws.py'
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        pprint_imported = any(
            isinstance(node, ast.ImportFrom) and node.module == 'pprint'
            for node in ast.walk(tree)
        ) or any(
            isinstance(node, ast.Import) and any(alias.name == 'pprint' for alias in node.names)
            for node in ast.walk(tree)
        )

        self.assertTrue(pprint_imported, f"'pprint' is not imported in {file_path}")

    def test_convert_key_to_str_function_exists(self):
        file_path = '../salt/utils/aws.py'
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        convert_key_to_str_function = None
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef) and node.name == '_convert_key_to_str':
                convert_key_to_str_function = node
                break

        self.assertIsNotNone(convert_key_to_str_function, f"'_convert_key_to_str' function not found in {file_path}")

    def test_retry_get_url_function_exists(self):
        file_path = '../salt/utils/aws.py'
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        retry_get_url_function = None
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef) and node.name == '_retry_get_url':
                retry_get_url_function = node
                break

        self.assertIsNotNone(retry_get_url_function, f"'_retry_get_url' function not found in {file_path}")

    def test_utils_iam_py_does_not_exist(self):
        file_path = '../utils/iam.py'
        self.assertFalse(os.path.exists(file_path), f"{file_path} should not exist")

if __name__ == '__main__':
    unittest.main()
