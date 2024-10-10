import unittest
import os
import ast

class TestPagedCallRedefinition(unittest.TestCase):

    def test_imported_paged_call_exists(self):
        file_path = '../salt/utils/boto3mod.py'
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        imported_paged_call_exists = any(
            isinstance(node, ast.ImportFrom) and
            node.module == 'salt.utils.botomod' and
            any(alias.name == 'paged_call' and alias.asname == 'imported_paged_call' for alias in node.names)
            for node in ast.walk(tree)
        )

        self.assertTrue(imported_paged_call_exists, f"Import for 'paged_call as imported_paged_call' from 'salt.utils.botomod' not found in {file_path}")

    def test_paged_call_redefinition_exists(self):
        file_path = '../salt/utils/boto3mod.py'
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        paged_call_function = next(
            (node for node in ast.walk(tree) if isinstance(node, ast.FunctionDef) and node.name == 'paged_call'),
            None
        )

        self.assertIsNotNone(paged_call_function, f"'paged_call' function not found in {file_path}")

    def test_paged_call_calls_imported_paged_call(self):
        file_path = '../salt/utils/boto3mod.py'
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        paged_call_function = next(
            (node for node in ast.walk(tree) if isinstance(node, ast.FunctionDef) and node.name == 'paged_call'),
            None
        )

        self.assertIsNotNone(paged_call_function, f"'paged_call' function not found in {file_path}")

        # Check if the function contains a call to `imported_paged_call`
        function_calls_imported_paged_call = any(
            isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == 'imported_paged_call'
            for node in ast.walk(paged_call_function)
        )

        self.assertTrue(function_calls_imported_paged_call, f"'paged_call' function does not call 'imported_paged_call' in {file_path}")

    def test_original_paged_call_has_key_elements(self):
        file_path = '../salt/utils/botomod.py'
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        paged_call_function = next(
            (node for node in ast.walk(tree) if isinstance(node, ast.FunctionDef) and node.name == 'paged_call'),
            None
        )

        self.assertIsNotNone(paged_call_function, f"'paged_call' function not found in {file_path}")

        # Check for key elements in the function
        has_docstring = isinstance(paged_call_function.body[0], ast.Expr) and isinstance(paged_call_function.body[0].value, ast.Str)
        has_pop_marker_flag = any(
            isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute) and node.func.attr == 'pop' and
            isinstance(node.args[0], ast.Str) and node.args[0].s == 'marker_flag'
            for node in ast.walk(paged_call_function)
        )
        has_while_loop = any(isinstance(node, ast.While) for node in paged_call_function.body)

        self.assertTrue(has_docstring, "'paged_call' function does not contain the expected docstring")
        self.assertTrue(has_pop_marker_flag, "'paged_call' function does not pop 'marker_flag' from kwargs")
        self.assertTrue(has_while_loop, "'paged_call' function does not contain the expected while loop")

if __name__ == '__main__':
    unittest.main()
