import unittest
import os
import ast

class TestSaltExitCodes(unittest.TestCase):

    def test_exitcodes_has_ex_unavail(self):
        file_path = '../salt/defaults/exitcodes.py'
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        ex_unavail_found = False
        for node in ast.walk(tree):
            if isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Name) and target.id == 'EX_UNAVAIL':
                        if isinstance(node.value, ast.Constant) and node.value.value == 69:
                            ex_unavail_found = True
                            break

        self.assertTrue(ex_unavail_found, f"'EX_UNAVAIL = 69' not found in {file_path}")

    def test_scripts_py_uses_ex_unavail(self):
        file_path = '../salt/scripts.py'
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        ex_unavail_used = False

        for node in ast.walk(tree):
            if isinstance(node, ast.Attribute):
                if (isinstance(node.value, ast.Attribute) and 
                    isinstance(node.value.value, ast.Attribute) and 
                    isinstance(node.value.value.value, ast.Name) and 
                    node.value.value.value.id == 'salt' and 
                    node.value.value.attr == 'defaults' and 
                    node.value.attr == 'exitcodes' and 
                    node.attr == 'EX_UNAVAIL'):
                    ex_unavail_used = True
                    break

        self.assertTrue(ex_unavail_used, f"'salt.defaults.exitcodes.EX_UNAVAIL' not found in {file_path}")
    
    def test_scripts_py_does_not_use_ex_unavailable(self):
        file_path = '../salt/scripts.py'
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        ex_unavailable_used = False

        for node in ast.walk(tree):
            if isinstance(node, ast.Attribute):
                if (isinstance(node.value, ast.Attribute) and 
                    isinstance(node.value.value, ast.Attribute) and 
                    isinstance(node.value.value.value, ast.Name) and 
                    node.value.value.value.id == 'salt' and 
                    node.value.value.attr == 'defaults' and 
                    node.value.attr == 'exitcodes' and 
                    node.attr == 'EX_UNAVAILABLE'):
                    ex_unavailable_used = True
                    break

        self.assertFalse(ex_unavailable_used, f"'salt.defaults.exitcodes.EX_UNAVAILABLE' found in {file_path}")

    def test_parsers_py_uses_ex_unavail(self):
        file_path = '../salt/utils/parsers.py'
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        ex_unavail_used = False

        for node in ast.walk(tree):
            if isinstance(node, ast.Attribute):
                if (isinstance(node.value, ast.Attribute) and 
                    isinstance(node.value.value, ast.Attribute) and 
                    isinstance(node.value.value.value, ast.Name) and 
                    node.value.value.value.id == 'salt' and 
                    node.value.value.attr == 'defaults' and 
                    node.value.attr == 'exitcodes' and 
                    node.attr == 'EX_UNAVAIL'):
                    ex_unavail_used = True
                    break

        self.assertTrue(ex_unavail_used, f"'salt.defaults.exitcodes.EX_UNAVAIL' not found in {file_path}")
    
    def test_parsers_py_does_not_use_ex_unavailable(self):
        file_path = '../salt/utils/parsers.py'
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        ex_unavailable_used = False

        for node in ast.walk(tree):
            if isinstance(node, ast.Attribute):
                if (isinstance(node.value, ast.Attribute) and 
                    isinstance(node.value.value, ast.Attribute) and 
                    isinstance(node.value.value.value, ast.Name) and 
                    node.value.value.value.id == 'salt' and 
                    node.value.value.attr == 'defaults' and 
                    node.value.attr == 'exitcodes' and 
                    node.attr == 'EX_UNAVAILABLE'):
                    ex_unavailable_used = True
                    break

        self.assertFalse(ex_unavailable_used, f"'salt.defaults.exitcodes.EX_UNAVAILABLE' found in {file_path}")

    def test_salt_call_py_uses_ex_unavail(self):
        file_path = '../tests/pytests/integration/cli/test_salt_call.py'
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        ex_unavail_used = False

        for node in ast.walk(tree):
            if isinstance(node, ast.Attribute):
                if (isinstance(node.value, ast.Attribute) and 
                    isinstance(node.value.value, ast.Attribute) and 
                    isinstance(node.value.value.value, ast.Name) and 
                    node.value.value.value.id == 'salt' and 
                    node.value.value.attr == 'defaults' and 
                    node.value.attr == 'exitcodes' and 
                    node.attr == 'EX_UNAVAIL'):
                    ex_unavail_used = True
                    break

        self.assertTrue(ex_unavail_used, f"'salt.defaults.exitcodes.EX_UNAVAIL' not found in {file_path}")
    
    def test_salt_call_py_does_not_use_ex_unavailable(self):
        file_path = '../tests/pytests/integration/cli/test_salt_call.py'
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        ex_unavailable_used = False

        for node in ast.walk(tree):
            if isinstance(node, ast.Attribute):
                if (isinstance(node.value, ast.Attribute) and 
                    isinstance(node.value.value, ast.Attribute) and 
                    isinstance(node.value.value.value, ast.Name) and 
                    node.value.value.value.id == 'salt' and 
                    node.value.value.attr == 'defaults' and 
                    node.value.attr == 'exitcodes' and 
                    node.attr == 'EX_UNAVAILABLE'):
                    ex_unavailable_used = True
                    break

        self.assertFalse(ex_unavailable_used, f"'salt.defaults.exitcodes.EX_UNAVAILABLE' found in {file_path}")

    def test_scripts_py_imports_exitcodes(self):
        file_path = '../salt/scripts.py'
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        import_found = False

        for node in ast.walk(tree):
            if isinstance(node, ast.Import) or isinstance(node, ast.ImportFrom):
                for alias in node.names:
                    if alias.name == 'salt.defaults.exitcodes':
                        import_found = True
                        break

        self.assertTrue(import_found, f"'import salt.defaults.exitcodes' not found in {file_path}")

    def test_parsers_py_imports_exitcodes(self):
        file_path = '../salt/utils/parsers.py'
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        import_found = False

        for node in ast.walk(tree):
            if isinstance(node, ast.Import) or isinstance(node, ast.ImportFrom):
                for alias in node.names:
                    if alias.name == 'salt.defaults.exitcodes':
                        import_found = True
                        break

        self.assertTrue(import_found, f"'import salt.defaults.exitcodes' not found in {file_path}")

    def test_salt_call_py_imports_exitcodes(self):
        file_path = '../tests/pytests/integration/cli/test_salt_call.py'
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        import_found = False

        for node in ast.walk(tree):
            if isinstance(node, ast.Import) or isinstance(node, ast.ImportFrom):
                for alias in node.names:
                    if alias.name == 'salt.defaults.exitcodes':
                        import_found = True
                        break

        self.assertTrue(import_found, f"'import salt.defaults.exitcodes' not found in {file_path}")



    
if __name__ == '__main__':
    unittest.main()
