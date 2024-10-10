import unittest
import os
import ast

class TestExceptionHandlersReference(unittest.TestCase):

    def test_de_handling_errors_md(self):
        file_path = '../docs/de/docs/tutorial/handling-errors.md'
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")
        with open(file_path, 'r') as file:
            content = file.read()
            self.assertNotIn('exception_handlers.py', content, f"'exception_handlers.py' found in {file_path}")

    def test_em_handling_errors_md(self):
        file_path = '../docs/em/docs/tutorial/handling-errors.md'
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")
        with open(file_path, 'r') as file:
            content = file.read()
            self.assertNotIn('exception_handlers.py', content, f"'exception_handlers.py' found in {file_path}")

    def test_en_handling_errors_md(self):
        file_path = '../docs/en/docs/tutorial/handling-errors.md'
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")
        with open(file_path, 'r') as file:
            content = file.read()
            self.assertNotIn('exception_handlers.py', content, f"'exception_handlers.py' found in {file_path}")

    def test_ja_handling_errors_md(self):
        file_path = '../docs/ja/docs/tutorial/handling-errors.md'
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")
        with open(file_path, 'r') as file:
            content = file.read()
            self.assertNotIn('exception_handlers.py', content, f"'exception_handlers.py' found in {file_path}")

    def test_pt_handling_errors_md(self):
        file_path = '../docs/pt/docs/tutorial/handling-errors.md'
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")
        with open(file_path, 'r') as file:
            content = file.read()
            self.assertNotIn('exception_handlers.py', content, f"'exception_handlers.py' found in {file_path}")

    def test_ru_handling_errors_md(self):
        file_path = '../docs/ru/docs/tutorial/handling-errors.md'
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")
        with open(file_path, 'r') as file:
            content = file.read()
            self.assertNotIn('exception_handlers.py', content, f"'exception_handlers.py' found in {file_path}")

    def test_zh_handling_errors_md(self):
        file_path = '../docs/zh/docs/tutorial/handling-errors.md'
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")
        with open(file_path, 'r') as file:
            content = file.read()
            self.assertNotIn('exception_handlers.py', content, f"'exception_handlers.py' found in {file_path}")

    def test_tutorial006_py(self):
        file_path = '../docs_src/handling_errors/tutorial006.py'
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")
        with open(file_path, 'r') as file:
            content = file.read()
            self.assertNotIn('exception_handlers.py', content, f"'exception_handlers.py' found in {file_path}")

    def test_applications_py(self):
        file_path = '../fastapi/applications.py'
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")
        with open(file_path, 'r') as file:
            content = file.read()
            self.assertNotIn('exception_handlers.py', content, f"'exception_handlers.py' found in {file_path}")
            
    def test_handlers_and_exception_handlers_files(self):
        handlers_path = '../fastapi/handlers.py'
        exception_handlers_path = '../fastapi/exception_handlers.py'
        
        # Check that fastapi/handlers.py exists
        self.assertTrue(os.path.exists(handlers_path), f"{handlers_path} does not exist")
        
        # Check that fastapi/exception_handlers.py does not exist
        self.assertFalse(os.path.exists(exception_handlers_path), f"{exception_handlers_path} should not exist")

    def test_applications_py_has_correct_imports(self):
        file_path = '../fastapi/applications.py'
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        import_found = False

        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom):
                if node.module == 'fastapi.handlers':
                    imported_names = {alias.name for alias in node.names}
                    if {
                        'http_exception_handler',
                        'request_validation_exception_handler',
                        'websocket_request_validation_exception_handler'
                    }.issubset(imported_names):
                        import_found = True
                        break

        self.assertTrue(import_found, "The required import statement from 'fastapi.handlers' is not found in 'applications.py'")

    def test_tutorial006_py_has_correct_imports(self):
        file_path = '../docs_src/handling_errors/tutorial006.py'
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        import_found = False

        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom):
                if node.module == 'fastapi.handlers':
                    imported_names = {alias.name for alias in node.names}
                    if {
                        'http_exception_handler',
                        'request_validation_exception_handler'
                    }.issubset(imported_names):
                        import_found = True
                        break

        self.assertTrue(import_found, "The required import statement from 'fastapi.handlers' is not found in 'tutorial006.py'")


if __name__ == '__main__':
    unittest.main()
