import unittest
import os
import ast

class TestSaltCryptFunctions(unittest.TestCase):

    def test_salt_cloud_init_py(self):
        file_path = '../salt/cloud/__init__.py'
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        old_function_found = any(isinstance(node, ast.Attribute) and node.attr == 'pem_finger' for node in ast.walk(tree))
        new_function_found = any(isinstance(node, ast.Attribute) and node.attr == 'pem_fingerprint' for node in ast.walk(tree))

        self.assertFalse(old_function_found, f"'pem_finger' found in {file_path}, but it should not be used")
        self.assertTrue(new_function_found, f"'pem_fingerprint' not found in {file_path}, but it should be used")

    def test_salt_crypt_py(self):
        file_path = '../salt/crypt.py'
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        old_function_found = any(isinstance(node, ast.Attribute) and node.attr == 'pem_finger' for node in ast.walk(tree))
        new_function_found = any(isinstance(node, ast.Attribute) and node.attr == 'pem_fingerprint' for node in ast.walk(tree))

        self.assertFalse(old_function_found, f"'pem_finger' found in {file_path}, but it should not be used")
        self.assertTrue(new_function_found, f"'pem_fingerprint' not found in {file_path}, but it should be used")

    def test_salt_key_py(self):
        file_path = '../salt/key.py'
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        old_function_found = any(isinstance(node, ast.Attribute) and node.attr == 'pem_finger' for node in ast.walk(tree))
        new_function_found = any(isinstance(node, ast.Attribute) and node.attr == 'pem_fingerprint' for node in ast.walk(tree))

        self.assertFalse(old_function_found, f"'pem_finger' found in {file_path}, but it should not be used")
        self.assertTrue(new_function_found, f"'pem_fingerprint' not found in {file_path}, but it should be used")

    def test_salt_modules_key_py(self):
        file_path = '../salt/modules/key.py'
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        old_function_found = any(isinstance(node, ast.Attribute) and node.attr == 'pem_finger' for node in ast.walk(tree))
        new_function_found = any(isinstance(node, ast.Attribute) and node.attr == 'pem_fingerprint' for node in ast.walk(tree))

        self.assertFalse(old_function_found, f"'pem_finger' found in {file_path}, but it should not be used")
        self.assertTrue(new_function_found, f"'pem_fingerprint' not found in {file_path}, but it should be used")

    def test_salt_utils_cloud_py(self):
        file_path = '../salt/utils/cloud.py'
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        old_function_found = any(isinstance(node, ast.Attribute) and node.attr == 'pem_finger' for node in ast.walk(tree))
        new_function_found = any(isinstance(node, ast.Attribute) and node.attr == 'pem_fingerprint' for node in ast.walk(tree))

        self.assertFalse(old_function_found, f"'pem_finger' found in {file_path}, but it should not be used")
        self.assertTrue(new_function_found, f"'pem_fingerprint' not found in {file_path}, but it should be used")

    def test_salt_wheel_key_py(self):
        file_path = '../salt/wheel/key.py'
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        old_function_found = any(isinstance(node, ast.Attribute) and node.attr == 'pem_finger' for node in ast.walk(tree))
        new_function_found = any(isinstance(node, ast.Attribute) and node.attr == 'pem_fingerprint' for node in ast.walk(tree))

        self.assertFalse(old_function_found, f"'pem_finger' found in {file_path}, but it should not be used")
        self.assertTrue(new_function_found, f"'pem_fingerprint' not found in {file_path}, but it should be used")

    def test_tests_pytests_unit_utils_test_crypt_py(self):
        file_path = '../tests/pytests/unit/utils/test_crypt.py'
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        old_function_found = any(isinstance(node, ast.Attribute) and node.attr == 'pem_finger' for node in ast.walk(tree))
        new_function_found = any(isinstance(node, ast.Attribute) and node.attr == 'pem_fingerprint' for node in ast.walk(tree))

        self.assertFalse(old_function_found, f"'pem_finger' found in {file_path}, but it should not be used")
        self.assertTrue(new_function_found, f"'pem_fingerprint' not found in {file_path}, but it should be used")

    def test_pem_finger_def_not_exists_in_utils_crypt(self):
        file_path = '../salt/utils/crypt.py'
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        pem_finger_def_found = any(isinstance(node, ast.FunctionDef) and node.name == 'pem_finger' for node in ast.walk(tree))

        self.assertFalse(pem_finger_def_found, f"Function definition 'pem_finger' found in {file_path}, but it should not exist")

    def test_pem_fingerprint_def_exists_in_utils_crypt(self):
        file_path = '../salt/utils/crypt.py'
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        pem_fingerprint_def_found = any(isinstance(node, ast.FunctionDef) and node.name == 'pem_fingerprint' for node in ast.walk(tree))

        self.assertTrue(pem_fingerprint_def_found, f"Function definition 'pem_fingerprint' not found in {file_path}, but it should exist")

    def test_patch_pem_fingerprint_in_test_key_py(self):
        file_path = '../tests/pytests/unit/modules/test_key.py'
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        with open(file_path, 'r') as file:
            content = file.read()

        self.assertIn("patch.object", content, f"'patch.object' not found in {file_path}")
        self.assertIn("pem_fingerprint", content, f"'pem_fingerprint' not found in a patch.object() call in {file_path}")

if __name__ == '__main__':
    unittest.main()
