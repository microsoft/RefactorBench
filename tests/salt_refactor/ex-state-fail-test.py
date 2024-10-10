import unittest
import os
import ast

class TestSaltUtilsStateFail(unittest.TestCase):

    def test_ex_state_failure_not_in_exitcodes(self):
        file_path = '../salt/defaults/exitcodes.py'
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        ex_state_failure_found = False
        for node in ast.walk(tree):
            if isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Name) and target.id == 'EX_STATE_FAILURE':
                        ex_state_failure_found = True
                        break

        self.assertFalse(ex_state_failure_found, f"'EX_STATE_FAILURE' should not exist in {file_path}")

    def test_ex_state_fail_in_exitcodes(self):
        file_path = '../salt/defaults/exitcodes.py'
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        ex_state_fail_found = False
        for node in ast.walk(tree):
            if isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Name) and target.id == 'EX_STATE_FAIL':
                        ex_state_fail_found = True
                        break

        self.assertTrue(ex_state_fail_found, f"'EX_STATE_FAIL' not found in {file_path}")

    def test_ex_state_failure_not_in_state(self):
        file_path = '../salt/modules/state.py'
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        ex_state_failure_found = False

        for node in ast.walk(tree):
            if isinstance(node, ast.Attribute):
                if (node.attr == "EX_STATE_FAILURE" and
                    isinstance(node.value, ast.Attribute) and
                    node.value.attr == "exitcodes" and
                    isinstance(node.value.value, ast.Attribute) and
                    node.value.value.attr == "defaults" and
                    isinstance(node.value.value.value, ast.Name) and
                    node.value.value.value.id == "salt"):
                    ex_state_failure_found = True
                    break

        self.assertFalse(ex_state_failure_found, "salt.defaults.exitcodes.EX_STATE_FAILURE should not exist in salt/modules/state.py")

    def test_ex_state_fail_is_used_in_state(self):
        file_path = '../salt/modules/state.py'
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        ex_state_fail_found = False

        for node in ast.walk(tree):
            if isinstance(node, ast.Attribute):
                if (node.attr == "EX_STATE_FAIL" and
                    isinstance(node.value, ast.Attribute) and
                    node.value.attr == "exitcodes" and
                    isinstance(node.value.value, ast.Attribute) and
                    node.value.value.attr == "defaults" and
                    isinstance(node.value.value.value, ast.Name) and
                    node.value.value.value.id == "salt"):
                    ex_state_fail_found = True
                    break

        self.assertTrue(ex_state_fail_found, "salt.defaults.exitcodes.EX_STATE_FAIL was not found in salt/modules/state.py")

    def test_ex_state_failure_not_in_test_salt_call(self):
        file_path = '../tests/pytests/integration/cli/test_salt_call.py'
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        ex_state_failure_found = False

        for node in ast.walk(tree):
            if isinstance(node, ast.Attribute):
                if (node.attr == "EX_STATE_FAILURE" and
                    isinstance(node.value, ast.Attribute) and
                    node.value.attr == "exitcodes" and
                    isinstance(node.value.value, ast.Attribute) and
                    node.value.value.attr == "defaults" and
                    isinstance(node.value.value.value, ast.Name) and
                    node.value.value.value.id == "salt"):
                    ex_state_failure_found = True
                    break

        self.assertFalse(ex_state_failure_found, "salt.defaults.exitcodes.EX_STATE_FAILURE should not exist in tests/pytests/integration/cli/test_salt_call.py")

    def test_ex_state_fail_is_used_in_test_salt_call(self):
        file_path = '../tests/pytests/integration/cli/test_salt_call.py'
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        ex_state_fail_found = False

        for node in ast.walk(tree):
            if isinstance(node, ast.Attribute):
                if (node.attr == "EX_STATE_FAIL" and
                    isinstance(node.value, ast.Attribute) and
                    node.value.attr == "exitcodes" and
                    isinstance(node.value.value, ast.Attribute) and
                    node.value.value.attr == "defaults" and
                    isinstance(node.value.value.value, ast.Name) and
                    node.value.value.value.id == "salt"):
                    ex_state_fail_found = True
                    break

        self.assertTrue(ex_state_fail_found, "salt.defaults.exitcodes.EX_STATE_FAIL was not found in tests/pytests/integration/cli/test_salt_call.py")

if __name__ == '__main__':
    unittest.main()
