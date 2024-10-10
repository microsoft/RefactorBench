import unittest
import os
import ast

class TestSaltUtilsModules(unittest.TestCase):

    # Check that 'mksls' does not exist in preseed.py
    def test_preseed_py_does_not_have_mksls(self):
        file_path = '../salt/utils/preseed.py'
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        mksls_function_found = any(
            isinstance(node, ast.FunctionDef) and node.name == 'mksls'
            for node in ast.walk(tree)
        )

        self.assertFalse(mksls_function_found, f"'mksls' should not be found in {file_path}")

    # Check that 'mksls' does not exist in kickstart.py
    def test_kickstart_py_does_not_have_mksls(self):
        file_path = '../salt/utils/kickstart.py'
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        mksls_function_found = any(
            isinstance(node, ast.FunctionDef) and node.name == 'mksls'
            for node in ast.walk(tree)
        )

        self.assertFalse(mksls_function_found, f"'mksls' should not be found in {file_path}")

    # Check that 'mksls' does not exist in yast.py
    def test_yast_py_does_not_have_mksls(self):
        file_path = '../salt/utils/yast.py'
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        mksls_function_found = any(
            isinstance(node, ast.FunctionDef) and node.name == 'mksls'
            for node in ast.walk(tree)
        )

        self.assertFalse(mksls_function_found, f"'mksls' should not be found in {file_path}")

    # Check that 'preseed_to_sls' exists in preseed.py
    def test_preseed_py_has_preseed_to_sls(self):
        file_path = '../salt/utils/preseed.py'
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        preseed_to_sls_function_found = any(
            isinstance(node, ast.FunctionDef) and node.name == 'preseed_to_sls'
            for node in ast.walk(tree)
        )

        self.assertTrue(preseed_to_sls_function_found, f"'preseed_to_sls' not found in {file_path}")

    # Check that 'kickstart_to_sls' exists in kickstart.py
    def test_kickstart_py_has_kickstart_to_sls(self):
        file_path = '../salt/utils/kickstart.py'
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        kickstart_to_sls_function_found = any(
            isinstance(node, ast.FunctionDef) and node.name == 'kickstart_to_sls'
            for node in ast.walk(tree)
        )

        self.assertTrue(kickstart_to_sls_function_found, f"'kickstart_to_sls' not found in {file_path}")

    # Check that 'autoyast_to_sls' exists in yast.py
    def test_yast_py_has_autoyast_to_sls(self):
        file_path = '../salt/utils/yast.py'
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        autoyast_to_sls_function_found = any(
            isinstance(node, ast.FunctionDef) and node.name == 'autoyast_to_sls'
            for node in ast.walk(tree)
        )

        self.assertTrue(autoyast_to_sls_function_found, f"'autoyast_to_sls' not found in {file_path}")

if __name__ == '__main__':
    unittest.main()
