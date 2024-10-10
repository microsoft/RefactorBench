import unittest
import os
import ast

class TestHelpersFunctions(unittest.TestCase):

    def test_render_template_string_not_in_templating(self):
        file_path = '../src/flask/templating.py'
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        function_found = False
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef) and node.name == 'render_template_string':
                function_found = True
                break

        self.assertFalse(function_found, "'render_template_string' function found in templating.py")

    def test_render_template_str_exists_in_templating(self):
        file_path = '../src/flask/templating.py'
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        function_found = False
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef) and node.name == 'render_template_str':
                function_found = True
                break

        self.assertTrue(function_found, "'render_template_str' function not found in templating.py")

    def test_render_template_str_import_in_init(self):
        file_path = '../src/flask/__init__.py'
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        import_found = False
        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom):
                if (node.module == 'templating' and
                    any(alias.name == 'render_template_str' and alias.asname == 'render_template_str' for alias in node.names)):
                    import_found = True
                    break

        self.assertTrue(import_found, "Import 'from .templating import render_template_str as render_template_string' not found in __init__.py")

    def test_render_template_str_call_in_test_templating(self):
        # Path to the test_templating.py file
        file_path = '../tests/test_templating.py'
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Check if render_template_string is correctly aliased and called as render_template_str
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        correct_call_found = False
        incorrect_call_found = False
        for node in ast.walk(tree):
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute):
                if (isinstance(node.func.value, ast.Name) and
                    node.func.value.id == 'flask'):
                    if node.func.attr == 'render_template_str':
                        correct_call_found = True
                    elif node.func.attr == 'render_template_string':
                        incorrect_call_found = True

        self.assertTrue(correct_call_found, "Call to 'flask.render_template_string' not found in test_templating.py")
        self.assertFalse(incorrect_call_found, "Incorrect call to 'flask.render_template_str' found in test_templating.py")

    def test_render_template_usage_in_test_appctx(self):
        file_path = '../tests/test_appctx.py'
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        correct_call_found = False
        incorrect_call_found = False
        for node in ast.walk(tree):
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute):
                if (isinstance(node.func.value, ast.Name) and node.func.value.id == 'flask'):
                    if node.func.attr == 'render_template_str':
                        correct_call_found = True
                    elif node.func.attr == 'render_template_string':
                        incorrect_call_found = True

        self.assertTrue(correct_call_found, "Call to 'flask.render_template_str' not found in test_appctx.py")
        self.assertFalse(incorrect_call_found, "Incorrect call to 'flask.render_template_string' found in test_appctx.py")


    def test_render_template_usage_in_test_blueprints(self):
        file_path = '../tests/test_blueprints.py'
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        correct_call_found = False
        incorrect_call_found = False
        for node in ast.walk(tree):
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute):
                if (isinstance(node.func.value, ast.Name) and node.func.value.id == 'flask'):
                    if node.func.attr == 'render_template_str':
                        correct_call_found = True
                    elif node.func.attr == 'render_template_string':
                        incorrect_call_found = True

        self.assertTrue(correct_call_found, "Call to 'flask.render_template_str' not found in test_blueprints.py")
        self.assertFalse(incorrect_call_found, "Incorrect call to 'flask.render_template_string' found in test_blueprints.py")


    def test_render_template_usage_in_test_json(self):
        file_path = '../tests/test_json.py'
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        correct_call_found = False
        incorrect_call_found = False
        for node in ast.walk(tree):
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute):
                if (isinstance(node.func.value, ast.Name) and node.func.value.id == 'flask'):
                    if node.func.attr == 'render_template_str':
                        correct_call_found = True
                    elif node.func.attr == 'render_template_string':
                        incorrect_call_found = True

        self.assertTrue(correct_call_found, "Call to 'flask.render_template_str' not found in test_json.py")
        self.assertFalse(incorrect_call_found, "Incorrect call to 'flask.render_template_string' found in test_json.py")


    def test_render_template_usage_in_test_templating(self):
        file_path = '../tests/test_templating.py'
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        correct_call_found = False
        incorrect_call_found = False
        for node in ast.walk(tree):
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute):
                if (isinstance(node.func.value, ast.Name) and node.func.value.id == 'flask'):
                    if node.func.attr == 'render_template_str':
                        correct_call_found = True
                    elif node.func.attr == 'render_template_string':
                        incorrect_call_found = True

        self.assertTrue(correct_call_found, "Call to 'flask.render_template_str' not found in test_templating.py")
        self.assertFalse(incorrect_call_found, "Incorrect call to 'flask.render_template_string' found in test_templating.py")

    def test_render_template_str_in_api_rst(self):
        file_path = '../docs/api.rst'
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        with open(file_path, 'r') as file:
            content = file.read()

        self.assertIn('render_template_str', content, "Expected 'render_template_str' not found in api.rst")
        self.assertNotIn('render_template_string', content, "Unexpected 'render_template_string' found in api.rst")

    def test_flask_templating_render_template_str_in_templating_rst(self):
        file_path = '../docs/templating.rst'
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        with open(file_path, 'r') as file:
            content = file.read()

        self.assertIn('flask.templating.render_template_str', content, "Expected 'flask.templating.render_template_str' not found in templating.rst")

    
if __name__ == '__main__':
    unittest.main()
