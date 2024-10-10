import unittest
import os
import ast

class TestSaltExitCodes(unittest.TestCase):

    def test_ex_cantcreate_in_exitcodes(self):
        file_path = '../salt/defaults/exitcodes.py'
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        ex_cantcreate_found = False
        for node in ast.walk(tree):
            if isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Name) and target.id == 'EX_CANTCREATE':
                        ex_cantcreate_found = True
                        break

        self.assertTrue(ex_cantcreate_found, f"'EX_CANTCREATE' not found in {file_path}")

    def test_ex_cantcreate_in_ssh_py_shim(self):
        file_path = '../salt/client/ssh/ssh_py_shim.py'
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        ex_cantcreate_found = False
        for node in ast.walk(tree):
            if isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Name) and target.id == 'EX_CANTCREATE':
                        ex_cantcreate_found = True
                        break

        self.assertTrue(ex_cantcreate_found, f"'EX_CANTCREATE' not found in {file_path}")

    def test_ssh_py_shim_uses_local_ex_cantcreate(self):
        file_path = '../salt/client/ssh/ssh_py_shim.py'
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        ex_cantcreate_used = False

        for node in ast.walk(tree):
            if isinstance(node, ast.Name) and node.id == 'EX_CANTCREATE':
                ex_cantcreate_used = True
                break

        self.assertTrue(ex_cantcreate_used, f"'EX_CANTCREATE' not used in {file_path}")

    def test_ssh_py_shim_does_not_import_exitcodes(self):
        file_path = '../salt/client/ssh/ssh_py_shim.py'
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        import_exitcodes_found = False

        for node in ast.walk(tree):
            if isinstance(node, ast.Import) or isinstance(node, ast.ImportFrom):
                for alias in node.names:
                    if alias.name == 'salt.defaults.exitcodes':
                        import_exitcodes_found = True
                        break

        self.assertFalse(import_exitcodes_found, f"'import salt.defaults.exitcodes' should not be found in {file_path}")

    def test_exitcodes_does_not_have_ex_cantcreat(self):
        file_path = '../salt/defaults/exitcodes.py'
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        ex_cantcreat_found = False
        for node in ast.walk(tree):
            if isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Name) and target.id == 'EX_CANTCREAT':
                        ex_cantcreat_found = True
                        break

        self.assertFalse(ex_cantcreat_found, f"'EX_CANTCREAT' (misspelled) found in {file_path}")

    def test_ssh_py_shim_does_not_have_ex_cantcreat(self):
        file_path = '../salt/client/ssh/ssh_py_shim.py'
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        ex_cantcreat_found = False
        for node in ast.walk(tree):
            if isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Name) and target.id == 'EX_CANTCREAT':
                        ex_cantcreat_found = True
                        break

        self.assertFalse(ex_cantcreat_found, f"'EX_CANTCREAT' (misspelled) found in {file_path}")
        
    def test_ex_cantcreate_is_used(self):
        file_path = '../salt/client/ssh/__init__.py'
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        with open(file_path, "r") as file:
            tree = ast.parse(file.read(), filename="__init__.py")
        
        ex_cantcreate_found = False
        
        # Traverse the syntax tree
        for node in ast.walk(tree):
            if isinstance(node, ast.Attribute):
                if (node.attr == "EX_CANTCREATE" and
                    isinstance(node.value, ast.Attribute) and
                    node.value.attr == "exitcodes" and
                    isinstance(node.value.value, ast.Attribute) and
                    node.value.value.attr == "defaults" and
                    isinstance(node.value.value.value, ast.Name) and
                    node.value.value.value.id == "salt"):
                    ex_cantcreate_found = True
                    break
        
        self.assertTrue(ex_cantcreate_found, "salt.defaults.exitcodes.EX_CANTCREATE was not found in salt/client/ssh/__init__.py")

    def test_ex_cantcreat_isnt_used(self):
        file_path = '../salt/client/ssh/__init__.py'
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        with open(file_path, "r") as file:
            tree = ast.parse(file.read(), filename="__init__.py")
        
        ex_cantcreat_found = False
        
        # Traverse the syntax tree
        for node in ast.walk(tree):
            if isinstance(node, ast.Attribute):
                if (node.attr == "EX_CANTCREAT" and
                    isinstance(node.value, ast.Attribute) and
                    node.value.attr == "exitcodes" and
                    isinstance(node.value.value, ast.Attribute) and
                    node.value.value.attr == "defaults" and
                    isinstance(node.value.value.value, ast.Name) and
                    node.value.value.value.id == "salt"):
                    ex_cantcreat_found = True
                    break
        
        self.assertFalse(ex_cantcreat_found, "salt.defaults.exitcodes.EX_CANTCREAT was found in salt/client/ssh/__init__.py, but it should not be used.")

if __name__ == '__main__':
    unittest.main()
