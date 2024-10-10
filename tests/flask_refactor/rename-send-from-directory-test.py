import unittest
import os
import ast

class TestHelpersFunctions(unittest.TestCase):

    def test_send_from_directory_helper_import_in_blueprints(self):
        file_path = '../src/flask/blueprints.py'
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        import_found = False
        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom):
                if node.module == 'helpers' and any(alias.name == 'send_from_directory_helper' for alias in node.names):
                    import_found = True
                    break

        self.assertTrue(import_found, "Import 'send_from_directory_helper' not found in blueprints.py")

    def test_send_from_directory_helper_import_in_init(self):
        file_path = '../src/flask/__init__.py'
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        import_found = False
        alias_correct = False
        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom):
                if node.module == 'helpers':
                    for alias in node.names:
                        if alias.name == 'send_from_directory_helper':
                            import_found = True
                            if alias.asname == 'send_from_directory':
                                alias_correct = True
                            break

        self.assertTrue(import_found, "Import 'send_from_directory_helper' not found in __init__.py")
        self.assertTrue(alias_correct, "Alias 'send_from_directory' not correctly assigned in __init__.py")

    def test_send_from_directory_helper_import_in_app(self):
        file_path = '../src/flask/app.py'
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        import_found = False
        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom):
                if node.module == 'helpers' and any(alias.name == 'send_from_directory_helper' for alias in node.names):
                    import_found = True
                    break

        self.assertTrue(import_found, "Import 'send_from_directory_helper' not found in app.py")

    def test_send_from_directory_call_in_test_helpers(self):
        # Path to the test_helpers.py file
        file_path = '../tests/test_helpers.py'
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Check if rv = flask.send_from_directory("static", "hello.txt") is called in a function within a class
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        call_found = False
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef):  # Check for class definition
                for class_node in node.body:
                    if isinstance(class_node, ast.FunctionDef):  # Check for function definition within the class
                        for func_node in class_node.body:
                            if isinstance(func_node, ast.Assign):  # Check if the statement is an assignment
                                if isinstance(func_node.value, ast.Call):
                                    call = func_node.value
                                    if (isinstance(call.func, ast.Attribute) and
                                            isinstance(call.func.value, ast.Name) and
                                            call.func.value.id == "flask" and
                                            call.func.attr == "send_from_directory" and
                                            len(call.args) == 2 and
                                            isinstance(call.args[0], ast.Constant) and call.args[0].value == "static" and
                                            isinstance(call.args[1], ast.Constant) and call.args[1].value == "hello.txt"):
                                        call_found = True
                                        break

        self.assertTrue(call_found, "Call to 'flask.send_from_directory(\"static\", \"hello.txt\")' not found in test_helpers.py")

if __name__ == '__main__':
    unittest.main()
