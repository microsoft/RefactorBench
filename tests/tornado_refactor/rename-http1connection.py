import unittest
import os
import ast

class TestTornadoHTTP1xConnectionMigration(unittest.TestCase):

    def test_HTTP1xConnection_class_exists(self):
        # Path to the file to check for the class existence
        file_path = '../tornado/http1connection.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Read and parse the content of http1connection.py
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        HTTP1xConnection_found = False
        HTTP1Connection_found = False

        # Check for the existence of HTTP1xConnection and HTTP1Connection
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef):
                if node.name == 'HTTP1xConnection':
                    HTTP1xConnection_found = True
                elif node.name == 'HTTP1Connection':
                    HTTP1Connection_found = True

        self.assertTrue(HTTP1xConnection_found, "Class 'HTTP1xConnection' not found in http1connection.py")
        self.assertFalse(HTTP1Connection_found, "Class 'HTTP1Connection' found in http1connection.py, but it should not be present")

    def test_imports_in_simple_httpclient(self):
        # Path to the file to check the import statement
        file_path = '../tornado/simple_httpclient.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Read and parse the content of simple_httpclient.py
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        imports_found = False

        # Check if 'from tornado.http1connection import HTTP1xConnection, HTTP1ConnectionParameters' is present
        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom):
                if node.module == 'tornado.http1connection' and \
                   any(alias.name == 'HTTP1xConnection' for alias in node.names) and \
                   any(alias.name == 'HTTP1ConnectionParameters' for alias in node.names):
                    imports_found = True
                    break

        self.assertTrue(imports_found, "'from tornado.http1connection import HTTP1xConnection, HTTP1ConnectionParameters' not found in simple_httpclient.py")

    def test_create_connection_method_in_simple_httpclient(self):
        # Path to the file to check the method definition
        file_path = '../tornado/simple_httpclient.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Read and parse the content of simple_httpclient.py
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        method_found = False

        # Check if 'def _create_connection(self, stream: IOStream) -> HTTP1xConnection' is present
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef) and node.name == '_create_connection':
                for arg in node.args.args:
                    if hasattr(arg.annotation, 'id') and arg.annotation.id == 'IOStream':
                        if hasattr(node.returns, 'id') and node.returns.id == 'HTTP1xConnection':
                            method_found = True
                            break

        self.assertTrue(method_found, "'def _create_connection(self, stream: IOStream) -> HTTP1xConnection' not found in simple_httpclient.py")

    
    def test_import_HTTP1xConnection_in_http1connection_test(self):
        # Path to the file to check the import statement in http1connection_test.py
        file_path = '../tornado/test/http1connection_test.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Read and parse the content of http1connection_test.py
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        import_found = False

        # Check if 'from tornado.http1connection import HTTP1xConnection' is present
        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom):
                if node.module == 'tornado.http1connection' and \
                   any(alias.name == 'HTTP1xConnection' for alias in node.names):
                    import_found = True
                    break

        self.assertTrue(import_found, "'from tornado.http1connection import HTTP1xConnection' not found in http1connection_test.py")

    def test_import_HTTP1xConnection_in_httpserver_test(self):
        # Path to the file to check the import statement in httpserver_test.py
        file_path = '../tornado/test/httpserver_test.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Read and parse the content of httpserver_test.py
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        import_found = False

        # Check if 'from tornado.http1connection import HTTP1xConnection' is present
        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom):
                if node.module == 'tornado.http1connection' and \
                   any(alias.name == 'HTTP1xConnection' for alias in node.names):
                    import_found = True
                    break

        self.assertTrue(import_found, "'from tornado.http1connection import HTTP1xConnection' not found in httpserver_test.py")

    def test_HTTP1xConnection_in_comment_in_web_test(self):
        # Path to the file to check for the comment in web_test.py
        file_path = '../tornado/test/web_test.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Read the content of web_test.py
        with open(file_path, 'r') as file:
            lines = file.readlines()

        comment_HTTP1xConnection_found = False
        comment_HTTP1Connection_found = False

        # Check for 'HTTP1xConnection' and 'HTTP1Connection' in comments
        for line in lines:
            if line.lstrip().startswith('#'):
                if 'HTTP1xConnection' in line:
                    comment_HTTP1xConnection_found = True
                if 'HTTP1Connection' in line:
                    comment_HTTP1Connection_found = True

        self.assertTrue(comment_HTTP1xConnection_found, "'HTTP1xConnection' not found in a comment in web_test.py")
        self.assertFalse(comment_HTTP1Connection_found, "'HTTP1Connection' found in a comment in web_test.py, but it should not be present")


if __name__ == '__main__':
    unittest.main()