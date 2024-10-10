import unittest
import os
import ast

class TestTCPClientConfigImports(unittest.TestCase):

    def test_import_in_tcpecho_client_py(self):
        # Path to the file where the import should be checked
        file_path = '../demos/tcpecho/client.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Read and parse the content of client.py
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        # Check if 'from tornado.tcpclientconfig import TCPClientConfig' exists
        import_found = False
        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom) and node.module == 'tornado.tcpclientconfig':
                if any(alias.name == 'TCPClientConfig' for alias in node.names):
                    import_found = True
                    break

        self.assertTrue(import_found, "'from tornado.tcpclientconfig import TCPClientConfig' not found in client.py")

    def test_tcpclient_connect_usage_in_tcpecho_client_py(self):
        # Path to the file where the usage should be checked
        file_path = '../demos/tcpecho/client.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Read and parse the content of client.py
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        # Check if the usage 'stream = await TCPClient().connect(TCPClientConfig(options.host, options.port))' exists
        usage_found = False
        for node in ast.walk(tree):
            if isinstance(node, ast.Assign) and isinstance(node.value, ast.Await):
                if (isinstance(node.value.value, ast.Call) and
                    isinstance(node.value.value.func, ast.Attribute) and
                    node.value.value.func.attr == 'connect' and
                    isinstance(node.value.value.func.value, ast.Call) and
                    isinstance(node.value.value.func.value.func, ast.Name) and
                    node.value.value.func.value.func.id == 'TCPClient'):
                    # Check the argument passed to connect
                    if (isinstance(node.value.value.args[0], ast.Call) and
                        isinstance(node.value.value.args[0].func, ast.Name) and
                        node.value.value.args[0].func.id == 'TCPClientConfig'):
                        usage_found = True
                        break

        self.assertTrue(usage_found, "'stream = await TCPClient().connect(TCPClientConfig(options.host, options.port))' not found in client.py")

    def test_import_in_simple_httpclient_py(self):
        # Path to the file where the import should be checked
        file_path = '../tornado/simple_httpclient.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Read and parse the content of simple_httpclient.py
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        # Check if 'from tornado.tcpclientconfig import TCPClientConfig' exists
        import_found = False
        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom) and node.module == 'tornado.tcpclientconfig':
                if any(alias.name == 'TCPClientConfig' for alias in node.names):
                    import_found = True
                    break

        self.assertTrue(import_found, "'from tornado.tcpclientconfig import TCPClientConfig' not found in simple_httpclient.py")

    def test_import_in_tcpclient_py(self):
        # Path to the file where the import should be checked
        file_path = '../tornado/tcpclient.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Read and parse the content of tcpclient.py
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        # Check if 'from tornado.tcpclientconfig import TCPClientConfig' exists
        import_found = False
        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom) and node.module == 'tornado.tcpclientconfig':
                if any(alias.name == 'TCPClientConfig' for alias in node.names):
                    import_found = True
                    break

        self.assertTrue(import_found, "'from tornado.tcpclientconfig import TCPClientConfig' not found in tcpclient.py")

    def test_tcpclientconfig_py_exists_and_has_TCPClientConfig_class(self):
        # Path to the file where the existence and class definition should be checked
        file_path = '../tornado/tcpclientconfig.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Read and parse the content of tcpclientconfig.py
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        # Check if 'class TCPClientConfig' exists
        class_found = False
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef) and node.name == 'TCPClientConfig':
                class_found = True
                break

        self.assertTrue(class_found, "'class TCPClientConfig' not found in tcpclientconfig.py")

    
    def test_import_in_tcpclient_test_py(self):
        # Path to the file where the import should be checked
        file_path = '../tornado/test/tcpclient_test.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Read and parse the content of tcpclient_test.py
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        # Check if 'from tornado.tcpclientconfig import TCPClientConfig' exists
        import_found = False
        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom) and node.module == 'tornado.tcpclientconfig':
                if any(alias.name == 'TCPClientConfig' for alias in node.names):
                    import_found = True
                    break

        self.assertTrue(import_found, "'from tornado.tcpclientconfig import TCPClientConfig' not found in tcpclient_test.py")


if __name__ == '__main__':
    unittest.main()