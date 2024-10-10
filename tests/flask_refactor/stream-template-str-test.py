import unittest
import os
import ast

class TestHelpersFunctions(unittest.TestCase):

    def test_stream_template_string_not_in_templating(self):
        file_path = '../src/flask/templating.py'
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        function_found = False
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef) and node.name == 'stream_template_string':
                function_found = True
                break

        self.assertFalse(function_found, "'stream_template_string' function found in templating.py")

    def test_stream_template_str_exists_in_templating(self):
        file_path = '../src/flask/templating.py'
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        function_found = False
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef) and node.name == 'stream_template_str':
                function_found = True
                break

        self.assertTrue(function_found, "'stream_template_str' function not found in templating.py")

    def test_import_in_init(self):
        file_path = '../src/flask/__init__.py'
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        import_found = False
        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom):
                if (node.module == 'templating' and
                    any(alias.name == 'stream_template_str' and alias.asname == 'stream_template_string' for alias in node.names)):
                    import_found = True
                    break

        self.assertTrue(import_found, "Import 'from .templating import stream_template_str as stream_template_string' not found in __init__.py")

    def test_flask_stream_template_string_call(self):
        file_path = '../tests/test_templating.py'
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        correct_call_found = False
        incorrect_call_found = False
        for node in ast.walk(tree):
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute):
                if (isinstance(node.func.value, ast.Name) and
                    node.func.value.id == 'flask'):
                    if node.func.attr == 'stream_template_string':
                        correct_call_found = True
                    elif node.func.attr == 'stream_template_str':
                        incorrect_call_found = True

        self.assertTrue(correct_call_found, "Call to 'flask.stream_template_string' not found in test_templating.py")
        self.assertFalse(incorrect_call_found, "Incorrect call to 'flask.stream_template_str' found in test_templating.py")

if __name__ == '__main__':
    unittest.main()
