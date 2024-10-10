import unittest
import os
import ast

class TestSaltUtilsSMB(unittest.TestCase):

    def test_ex_pillar_fail_in_exitcodes(self):
        file_path = '../salt/defaults/exitcodes.py'
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        ex_pillar_fail_found = False
        ex_pillar_failure_found = False
        for node in ast.walk(tree):
            if isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Name):
                        if target.id == 'EX_PILLAR_FAIL':
                            ex_pillar_fail_found = True
                        if target.id == 'EX_PILLAR_FAILURE':
                            ex_pillar_failure_found = True

        self.assertTrue(ex_pillar_fail_found, f"'EX_PILLAR_FAIL' not found in {file_path}")
        self.assertFalse(ex_pillar_failure_found, f"'EX_PILLAR_FAILURE' (misspelled) found in {file_path}")

    def test_ex_pillar_failure_isnt_used_in_state_wrapper(self):
        file_path = '../salt/client/ssh/wrapper/state.py'
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        ex_pillar_failure_found = False

        for node in ast.walk(tree):
            if isinstance(node, ast.Attribute):
                if (node.attr == "EX_PILLAR_FAILURE" and
                    isinstance(node.value, ast.Attribute) and
                    node.value.attr == "exitcodes" and
                    isinstance(node.value.value, ast.Attribute) and
                    node.value.value.attr == "defaults" and
                    isinstance(node.value.value.value, ast.Name) and
                    node.value.value.value.id == "salt"):
                    ex_pillar_failure_found = True
                    break

        self.assertFalse(ex_pillar_failure_found, "salt.defaults.exitcodes.EX_PILLAR_FAILURE was found in salt/client/ssh/wrapper/state.py, but it should not be used.")

    def test_ex_pillar_fail_is_used_in_state_wrapper(self):
        file_path = '../salt/client/ssh/wrapper/state.py'
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        ex_pillar_fail_found = False

        for node in ast.walk(tree):
            if isinstance(node, ast.Attribute):
                if (node.attr == "EX_PILLAR_FAIL" and
                    isinstance(node.value, ast.Attribute) and
                    node.value.attr == "exitcodes" and
                    isinstance(node.value.value, ast.Attribute) and
                    node.value.value.attr == "defaults" and
                    isinstance(node.value.value.value, ast.Name) and
                    node.value.value.value.id == "salt"):
                    ex_pillar_fail_found = True
                    break

        self.assertTrue(ex_pillar_fail_found, "salt.defaults.exitcodes.EX_PILLAR_FAIL was not found in salt/client/ssh/wrapper/state.py")

    def test_ex_pillar_failure_isnt_used_in_state_module(self):
        file_path = '../salt/modules/state.py'
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        ex_pillar_failure_found = False

        for node in ast.walk(tree):
            if isinstance(node, ast.Attribute):
                if (node.attr == "EX_PILLAR_FAILURE" and
                    isinstance(node.value, ast.Attribute) and
                    node.value.attr == "exitcodes" and
                    isinstance(node.value.value, ast.Attribute) and
                    node.value.value.attr == "defaults" and
                    isinstance(node.value.value.value, ast.Name) and
                    node.value.value.value.id == "salt"):
                    ex_pillar_failure_found = True
                    break

        self.assertFalse(ex_pillar_failure_found, "salt.defaults.exitcodes.EX_PILLAR_FAILURE was found in salt/modules/state.py, but it should not be used.")

    def test_ex_pillar_fail_is_used_in_state_module(self):
        file_path = '../salt/modules/state.py'
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        ex_pillar_fail_found = False

        for node in ast.walk(tree):
            if isinstance(node, ast.Attribute):
                if (node.attr == "EX_PILLAR_FAIL" and
                    isinstance(node.value, ast.Attribute) and
                    node.value.attr == "exitcodes" and
                    isinstance(node.value.value, ast.Attribute) and
                    node.value.value.attr == "defaults" and
                    isinstance(node.value.value.value, ast.Name) and
                    node.value.value.value.id == "salt"):
                    ex_pillar_fail_found = True
                    break

        self.assertTrue(ex_pillar_fail_found, "salt.defaults.exitcodes.EX_PILLAR_FAIL was not found in salt/modules/state.py")

if __name__ == '__main__':
    unittest.main()
