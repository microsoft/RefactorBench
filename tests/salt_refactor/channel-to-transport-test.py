import unittest
import os
import ast

class TestSaltUtilsAndMaster(unittest.TestCase):

    def test_channel_py_does_not_exist(self):
        file_path = '../salt/utils/channel.py'
        self.assertFalse(os.path.exists(file_path), f"{file_path} should not exist")

    def test_transport_py_exists(self):
        file_path = '../salt/utils/transport.py'
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

    def test_transport_has_iter_transport_opts(self):
        file_path = '../salt/utils/transport.py'
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        iter_transport_opts_function = next(
            (node for node in ast.walk(tree) if isinstance(node, ast.FunctionDef) and node.name == 'iter_transport_opts'),
            None
        )

        self.assertIsNotNone(iter_transport_opts_function, f"'iter_transport_opts' function not found in {file_path}")

    def test_master_imports_iter_transport_opts(self):
        file_path = '../salt/master.py'
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        import_statement_exists = any(
            isinstance(node, ast.ImportFrom) and
            node.module == 'salt.utils.transport' and
            any(alias.name == 'iter_transport_opts' for alias in node.names)
            for node in ast.walk(tree)
        )

        self.assertTrue(import_statement_exists, f"'iter_transport_opts' is not imported from 'salt.utils.transport' in {file_path}")

    def test_imports_salt_utils_transport(self):
        file_path = '../salt/channel/server.py'
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        import_statement_exists = any(
            isinstance(node, ast.Import) and
            any(alias.name == 'salt.utils.transport' for alias in node.names)
            for node in ast.walk(tree)
        )

        self.assertTrue(import_statement_exists, f"'import salt.utils.transport' is not found in {file_path}")


    def test_uses_iter_transport_opts(self):
        file_path = '../salt/channel/server.py'
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        iter_transport_opts_used = any(
            isinstance(node, ast.Call) and
            isinstance(node.func, ast.Attribute) and
            isinstance(node.func.value, ast.Attribute) and
            node.func.value.attr == 'transport' and
            node.func.attr == 'iter_transport_opts' and
            isinstance(node.args[0], ast.Name) and
            node.args[0].id == 'opts'
            for node in ast.walk(tree)
        )

        self.assertTrue(
            iter_transport_opts_used,
            f"'salt.utils.transport.iter_transport_opts(opts)' is not used in {file_path}"
        )
        
if __name__ == '__main__':
    unittest.main()
