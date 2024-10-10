import unittest
import os
import ast

class TestSaltUtilsSMB(unittest.TestCase):

    def test_ex_perm_denied_in_exitcodes(self):
        file_path = '../salt/defaults/exitcodes.py'
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        ex_perm_denied_found = False
        for node in ast.walk(tree):
            if isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Name) and target.id == 'EX_PERM_DENIED':
                        ex_perm_denied_found = True
                        break

        self.assertTrue(ex_perm_denied_found, f"'EX_PERM_DENIED' not found in {file_path}")

    def test_ex_noperm_not_in_exitcodes(self):
        file_path = '../salt/defaults/exitcodes.py'
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        ex_noperm_found = False
        for node in ast.walk(tree):
            if isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Name) and target.id == 'EX_NOPERM':
                        ex_noperm_found = True
                        break

        self.assertFalse(ex_noperm_found, f"'EX_NOPERM' (misspelled) found in {file_path}")

    def test_ex_noperm_isnt_used_in_ssh(self):
        file_path = '../salt/client/ssh/__init__.py'
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        ex_noperm_found = False

        for node in ast.walk(tree):
            if isinstance(node, ast.Attribute):
                if (node.attr == "EX_NOPERM" and
                    isinstance(node.value, ast.Attribute) and
                    node.value.attr == "exitcodes" and
                    isinstance(node.value.value, ast.Attribute) and
                    node.value.value.attr == "defaults" and
                    isinstance(node.value.value.value, ast.Name) and
                    node.value.value.value.id == "salt"):
                    ex_noperm_found = True
                    break

        self.assertFalse(ex_noperm_found, "salt.defaults.exitcodes.EX_NOPERM was found in salt/client/ssh/__init__.py, but it should not be used.")

    def test_ex_perm_denied_is_used_in_crypt(self):
        file_path = '../salt/crypt.py'
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        ex_perm_denied_found = False

        for node in ast.walk(tree):
            if isinstance(node, ast.Attribute):
                if (node.attr == "EX_PERM_DENIED" and
                    isinstance(node.value, ast.Attribute) and
                    node.value.attr == "exitcodes" and
                    isinstance(node.value.value, ast.Attribute) and
                    node.value.value.attr == "defaults" and
                    isinstance(node.value.value.value, ast.Name) and
                    node.value.value.value.id == "salt"):
                    ex_perm_denied_found = True
                    break

        self.assertTrue(ex_perm_denied_found, "salt.defaults.exitcodes.EX_PERM_DENIED was not found in salt/crypt.py")

    def test_ex_noperm_isnt_used_in_crypt(self):
        file_path = '../salt/crypt.py'
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        ex_noperm_found = False

        for node in ast.walk(tree):
            if isinstance(node, ast.Attribute):
                if (node.attr == "EX_NOPERM" and
                    isinstance(node.value, ast.Attribute) and
                    node.value.attr == "exitcodes" and
                    isinstance(node.value.value, ast.Attribute) and
                    node.value.value.attr == "defaults" and
                    isinstance(node.value.value.value, ast.Name) and
                    node.value.value.value.id == "salt"):
                    ex_noperm_found = True
                    break

        self.assertFalse(ex_noperm_found, "salt.defaults.exitcodes.EX_NOPERM was found in salt/crypt.py, but it should not be used.")

if __name__ == '__main__':
    unittest.main()
