import unittest
import os
import ast

class TestAnsibleConnectionUtils(unittest.TestCase):

    def test_connection_utils_exists(self):
        # Path to the connection.py file
        file_path = '../lib/ansible/module_utils/connection.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Check if ConnectionUtils class is defined in the file
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        connection_utils_class = None
        expected_functions = {'write_to_stream', 'send_data', 'recv_data', 'exec_command', 'request_builder'}
        found_functions = set()

        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef) and node.name == 'ConnectionUtils':
                connection_utils_class = node
                for func in node.body:
                    if isinstance(func, ast.FunctionDef) and func.name in expected_functions:
                        found_functions.add(func.name)

        self.assertIsNotNone(connection_utils_class, "Class 'ConnectionUtils' not found in connection.py")
        self.assertEqual(expected_functions, found_functions, "Not all expected functions were found in 'ConnectionUtils'")

    def test_imports_connection_utils_in_task_executor(self):
        # Path to the task_executor.py file
        file_path = '../lib/ansible/executor/task_executor.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Check if ConnectionUtils is imported in the file
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        connection_utils_imported = False

        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom) and node.module == 'ansible.module_utils.connection':
                for alias in node.names:
                    if alias.name == 'ConnectionUtils':
                        connection_utils_imported = True
                        break

        self.assertTrue(connection_utils_imported, "ConnectionUtils not imported in task_executor.py")

    def test_imports_connection_utils_in_ansible_connection_cli_stub(self):
        # Path to the ansible_connection_cli_stub.py file
        file_path = '../lib/ansible/cli/scripts/ansible_connection_cli_stub.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Check if ConnectionUtils is imported in the file
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        connection_utils_imported = False

        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom) and node.module == 'ansible.module_utils.connection':
                for alias in node.names:
                    if alias.name == 'ConnectionUtils':
                        connection_utils_imported = True
                        break

        self.assertTrue(connection_utils_imported, "ConnectionUtils not imported in ansible_connection_cli_stub.py")
        
    def test_connection_uses_connection_utils(self):
        # Path to the connection.py file
        file_path = '../lib/ansible/module_utils/connection.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Check if Connection class uses ConnectionUtils methods
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        connection_class = None
        request_builder_used = False
        recv_data_used = False

        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef) and node.name == 'Connection':
                connection_class = node
                for method in node.body:
                    if isinstance(method, ast.FunctionDef):
                        if method.name == '_exec_jsonrpc':
                            for inner_node in ast.walk(method):
                                if isinstance(inner_node, ast.Call) and isinstance(inner_node.func, ast.Attribute):
                                    if (inner_node.func.attr == 'request_builder' and
                                            isinstance(inner_node.func.value, ast.Name) and
                                            inner_node.func.value.id == 'ConnectionUtils'):
                                        request_builder_used = True
                        elif method.name == 'send':
                            for inner_node in ast.walk(method):
                                if isinstance(inner_node, ast.Call) and isinstance(inner_node.func, ast.Attribute):
                                    if (inner_node.func.attr == 'recv_data' and
                                            isinstance(inner_node.func.value, ast.Name) and
                                            inner_node.func.value.id == 'ConnectionUtils'):
                                        recv_data_used = True

        self.assertIsNotNone(connection_class, "Class 'Connection' not found in connection.py")
        self.assertTrue(request_builder_used, "'request_builder' from ConnectionUtils is not used in '_exec_jsonrpc' method")
        self.assertTrue(recv_data_used, "'recv_data' from ConnectionUtils is not used in 'send' method")

    def test_start_connection_uses_write_to_stream(self):
        # Path to the task_executor.py file
        file_path = '../lib/ansible/executor/task_executor.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Check if ConnectionUtils.write_to_stream is used in start_connection
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        start_connection_function = None
        write_to_stream_used = False

        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef) and node.name == 'start_connection':
                start_connection_function = node
                for inner_node in ast.walk(start_connection_function):
                    if isinstance(inner_node, ast.Call) and isinstance(inner_node.func, ast.Attribute):
                        if (inner_node.func.attr == 'write_to_stream' and
                                isinstance(inner_node.func.value, ast.Name) and
                                inner_node.func.value.id == 'ConnectionUtils'):
                            write_to_stream_used = True
                            break

        self.assertIsNotNone(start_connection_function, "Function 'start_connection' not found in task_executor.py")
        self.assertTrue(write_to_stream_used, "'write_to_stream' from ConnectionUtils is not used in 'start_connection' function")

    def test_ansible_connection_cli_stub_imports(self):
        # Path to the ansible_connection_cli_stub.py file
        file_path = '../lib/ansible/cli/scripts/ansible_connection_cli_stub.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Check if Connection, ConnectionError, and ConnectionUtils are imported from ansible.module_utils.connection
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        expected_imports = {'Connection', 'ConnectionError', 'ConnectionUtils'}
        found_imports = set()

        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom) and node.module == 'ansible.module_utils.connection':
                for alias in node.names:
                    if alias.name in expected_imports:
                        found_imports.add(alias.name)

        self.assertEqual(expected_imports, found_imports, "Not all expected imports found in ansible_connection_cli_stub.py")
        
    def test_run_function_uses_recv_send_data(self):
        # Path to the ansible_connection_cli_stub.py file
        file_path = '../lib/ansible/cli/scripts/ansible_connection_cli_stub.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Check if ConnectionUtils.recv_data and ConnectionUtils.send_data are used in the run function of ConnectionProcess class
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        connection_process_class = None
        recv_data_used = False
        send_data_used = False

        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef) and node.name == 'ConnectionProcess':
                connection_process_class = node
                for method in node.body:
                    if isinstance(method, ast.FunctionDef) and method.name == 'run':
                        for inner_node in ast.walk(method):
                            if isinstance(inner_node, ast.Call) and isinstance(inner_node.func, ast.Attribute):
                                if (inner_node.func.attr == 'recv_data' and
                                        isinstance(inner_node.func.value, ast.Name) and
                                        inner_node.func.value.id == 'ConnectionUtils'):
                                    recv_data_used = True
                                if (inner_node.func.attr == 'send_data' and
                                        isinstance(inner_node.func.value, ast.Name) and
                                        inner_node.func.value.id == 'ConnectionUtils'):
                                    send_data_used = True

        self.assertIsNotNone(connection_process_class, "Class 'ConnectionProcess' not found in ansible_connection_cli_stub.py")
        self.assertTrue(recv_data_used, "'recv_data' from ConnectionUtils is not used in 'run' function of ConnectionProcess class")
        self.assertTrue(send_data_used, "'send_data' from ConnectionUtils is not used in 'run' function of ConnectionProcess class")



if __name__ == '__main__':
    unittest.main()
