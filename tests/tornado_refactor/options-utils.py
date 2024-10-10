import unittest
import os
import ast

class TestTornadoGlobalOptionsImports(unittest.TestCase):

    def test_import_in_blog(self):
        # Path to the file where the import should be checked
        file_path = '../demos/blog/blog.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Read and parse the content of blog.py
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        # Check if 'from tornado.global_options import define, options' is present
        import_found = False
        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom):
                if node.module == 'tornado.global_options' and \
                   any(alias.name == 'define' for alias in node.names) and \
                   any(alias.name == 'options' for alias in node.names):
                    import_found = True
                    break

        self.assertTrue(import_found, "Import 'from tornado.global_options import define, options' not found in blog.py")

    def test_import_in_facebook(self):
        file_path = '../demos/facebook/facebook.py'

        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        import_found = False
        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom):
                if node.module == 'tornado.global_options' and \
                   any(alias.name == 'define' for alias in node.names) and \
                   any(alias.name == 'options' for alias in node.names):
                    import_found = True
                    break

        self.assertTrue(import_found, "Import 'from tornado.global_options import define, options' not found in facebook.py")

    def test_import_in_file_uploader(self):
        file_path = '../demos/file_upload/file_uploader.py'

        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        import_found = False
        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom):
                if node.module == 'tornado.global_options' and \
                   any(alias.name == 'define' for alias in node.names) and \
                   any(alias.name == 'options' for alias in node.names):
                    import_found = True
                    break

        self.assertTrue(import_found, "Import 'from tornado.global_options import define, options' not found in file_uploader.py")

    def test_import_in_google_auth(self):
        file_path = '../demos/google_auth/main.py'

        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        import_found = False
        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom):
                if node.module == 'tornado.global_options' and \
                   any(alias.name == 'define' for alias in node.names) and \
                   any(alias.name == 'options' for alias in node.names):
                    import_found = True
                    break

        self.assertTrue(import_found, "Import 'from tornado.global_options import define, options' not found in main.py")

    def test_import_in_helloworld(self):
        file_path = '../demos/helloworld/helloworld.py'

        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        import_found = False
        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom):
                if node.module == 'tornado.global_options' and \
                   any(alias.name == 'define' for alias in node.names) and \
                   any(alias.name == 'options' for alias in node.names):
                    import_found = True
                    break

        self.assertTrue(import_found, "Import 'from tornado.global_options import define, options' not found in helloworld.py")

    def test_import_in_s3server(self):
        file_path = '../demos/s3server/s3server.py'

        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        import_found = False
        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom):
                if node.module == 'tornado.global_options' and \
                   any(alias.name == 'define' for alias in node.names) and \
                   any(alias.name == 'options' for alias in node.names):
                    import_found = True
                    break

        self.assertTrue(import_found, "Import 'from tornado.global_options import define, options' not found in s3server.py")

    def test_import_in_tcp_client(self):
        file_path = '../demos/tcpecho/client.py'

        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        import_found = False
        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom):
                if node.module == 'tornado.global_options' and \
                   any(alias.name == 'define' for alias in node.names) and \
                   any(alias.name == 'options' for alias in node.names):
                    import_found = True
                    break

        self.assertTrue(import_found, "Import 'from tornado.global_options import define, options' not found in client.py")

    def test_import_in_tcp_server(self):
        file_path = '../demos/tcpecho/server.py'

        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        import_found = False
        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom):
                if node.module == 'tornado.global_options' and \
                   any(alias.name == 'define' for alias in node.names) and \
                   any(alias.name == 'options' for alias in node.names):
                    import_found = True
                    break

        self.assertTrue(import_found, "Import 'from tornado.global_options import define, options' not found in server.py")

    def test_import_in_chatdemo(self):
        file_path = '../demos/websocket/chatdemo.py'

        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        import_found = False
        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom):
                if node.module == 'tornado.global_options' and \
                   any(alias.name == 'define' for alias in node.names) and \
                   any(alias.name == 'options' for alias in node.names):
                    import_found = True
                    break

        self.assertTrue(import_found, "Import 'from tornado.global_options import define, options' not found in chatdemo.py")
    
    def test_import_in_chat_chatdemo(self):
        # Path to the file where the import should be checked
        file_path = '../demos/chat/chatdemo.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Read and parse the content of chatdemo.py
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        # Check if 'from tornado.global_options import define, options, parse_command_line' is present
        import_found = False
        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom):
                if node.module == 'tornado.global_options' and \
                any(alias.name == 'define' for alias in node.names) and \
                any(alias.name == 'options' for alias in node.names) and \
                any(alias.name == 'parse_command_line' for alias in node.names):
                    import_found = True
                    break

        self.assertTrue(import_found, "Import 'from tornado.global_options import define, options, parse_command_line' not found in chatdemo.py")


    def test_import_in_benchmark(self):
        # Path to the file where the import should be checked
        file_path = '../maint/benchmark/benchmark.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Read and parse the content of benchmark.py
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        # Check if 'from tornado.global_options import define, options, parse_command_line' is present
        import_found = False
        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom):
                if node.module == 'tornado.global_options' and \
                any(alias.name == 'define' for alias in node.names) and \
                any(alias.name == 'options' for alias in node.names) and \
                any(alias.name == 'parse_command_line' for alias in node.names):
                    import_found = True
                    break

        self.assertTrue(import_found, "Import 'from tornado.global_options import define, options, parse_command_line' not found in benchmark.py")


    def test_import_in_chunk_benchmark(self):
        # Path to the file where the import should be checked
        file_path = '../maint/benchmark/chunk_benchmark.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Read and parse the content of chunk_benchmark.py
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        # Check if 'from tornado.global_options import define, options, parse_command_line' is present
        import_found = False
        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom):
                if node.module == 'tornado.global_options' and \
                any(alias.name == 'define' for alias in node.names) and \
                any(alias.name == 'options' for alias in node.names) and \
                any(alias.name == 'parse_command_line' for alias in node.names):
                    import_found = True
                    break

        self.assertTrue(import_found, "Import 'from tornado.global_options import define, options, parse_command_line' not found in chunk_benchmark.py")
    
    def test_import_in_gen_benchmark(self):
        # Path to the file where the import should be checked
        file_path = '../maint/benchmark/gen_benchmark.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Read and parse the content of gen_benchmark.py
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        # Check if 'from tornado.global_options import define, options, parse_command_line' is present
        import_found = False
        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom):
                if node.module == 'tornado.global_options' and \
                any(alias.name == 'define' for alias in node.names) and \
                any(alias.name == 'options' for alias in node.names) and \
                any(alias.name == 'parse_command_line' for alias in node.names):
                    import_found = True
                    break

        self.assertTrue(import_found, "Import 'from tornado.global_options import define, options, parse_command_line' not found in gen_benchmark.py")

    def test_import_in_parsing_benchmark(self):
        # Path to the file where the import should be checked
        file_path = '../maint/benchmark/parsing_benchmark.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Read and parse the content of chunk_benchmark.py
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        # Check if 'from tornado.global_options import define, options, parse_command_line' is present
        import_found = False
        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom):
                if node.module == 'tornado.global_options' and \
                any(alias.name == 'define' for alias in node.names) and \
                any(alias.name == 'options' for alias in node.names) and \
                any(alias.name == 'parse_command_line' for alias in node.names):
                    import_found = True
                    break

        self.assertTrue(import_found, "Import 'from tornado.global_options import define, options, parse_command_line' not found in parsing_benchmark.py")

    def test_import_in_template_benchmark(self):
        # Path to the file where the import should be checked
        file_path = '../maint/benchmark/template_benchmark.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Read and parse the content of chunk_benchmark.py
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        # Check if 'from tornado.global_options import define, options, parse_command_line' is present
        import_found = False
        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom):
                if node.module == 'tornado.global_options' and \
                any(alias.name == 'define' for alias in node.names) and \
                any(alias.name == 'options' for alias in node.names) and \
                any(alias.name == 'parse_command_line' for alias in node.names):
                    import_found = True
                    break

        self.assertTrue(import_found, "Import 'from tornado.global_options import define, options, parse_command_line' not found in template_benchmark.py")

    def test_import_in_chunk_benchmark(self):
        # Path to the file where the import should be checked
        file_path = '../maint/scripts/test_resolvers.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Read and parse the content of chunk_benchmark.py
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        # Check if 'from tornado.global_options import define, options, parse_command_line' is present
        import_found = False
        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom):
                if node.module == 'tornado.global_options' and \
                any(alias.name == 'define' for alias in node.names) and \
                any(alias.name == 'options' for alias in node.names) and \
                any(alias.name == 'parse_command_line' for alias in node.names):
                    import_found = True
                    break

        self.assertTrue(import_found, "Import 'from tornado.global_options import define, options, parse_command_line' not found in chunk_benchmark.py")

    def test_import_in_websocket_client(self):
        # Path to the file where the import should be checked
        file_path = '../maint/test/websocket/client.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Read and parse the content of client.py
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        # Check if 'from tornado.global_options import define, options, parse_command_line' is present
        import_found = False
        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom):
                if node.module == 'tornado.global_options' and \
                any(alias.name == 'define' for alias in node.names) and \
                any(alias.name == 'options' for alias in node.names) and \
                any(alias.name == 'parse_command_line' for alias in node.names):
                    import_found = True
                    break

        self.assertTrue(import_found, "Import 'from tornado.global_options import define, options, parse_command_line' not found in client.py")


    def test_import_in_websocket_server(self):
        # Path to the file where the import should be checked
        file_path = '../maint/test/websocket/server.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Read and parse the content of server.py
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        # Check if 'from tornado.global_options import define, options, parse_command_line' is present
        import_found = False
        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom):
                if node.module == 'tornado.global_options' and \
                any(alias.name == 'define' for alias in node.names) and \
                any(alias.name == 'options' for alias in node.names) and \
                any(alias.name == 'parse_command_line' for alias in node.names):
                    import_found = True
                    break

        self.assertTrue(import_found, "Import 'from tornado.global_options import define, options, parse_command_line' not found in server.py")
    def test_global_options_file_exists(self):
        # Path to the file that should be checked
        file_path = '../tornado/global_options.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

    def test_define_function_exists(self):
        # Path to the file where the function should be checked
        file_path = '../tornado/global_options.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Read and parse the content of global_options.py
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        # Check if function define exists with the correct signature
        function_found = False
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef) and node.name == 'define':
                # Check function arguments
                arg_names = [arg.arg for arg in node.args.args]
                if arg_names == ['name', 'default', 'type', 'help', 'metavar', 'multiple', 'group', 'callback']:
                    function_found = True
                    break

        self.assertTrue(function_found, "Function 'define' with the correct signature not found in global_options.py")

    def test_parse_command_line_function_exists(self):
        # Path to the file where the function should be checked
        file_path = '../tornado/global_options.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Read and parse the content of global_options.py
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        # Check if function parse_command_line exists
        function_found = False
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef) and node.name == 'parse_command_line':
                function_found = True
                break

        self.assertTrue(function_found, "Function 'parse_command_line' not found in global_options.py")

    def test_add_parse_callback_function_exists(self):
        # Path to the file where the function should be checked
        file_path = '../tornado/global_options.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Read and parse the content of global_options.py
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        # Check if function add_parse_callback exists
        function_found = False
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef) and node.name == 'add_parse_callback':
                function_found = True
                break

        self.assertTrue(function_found, "Function 'add_parse_callback' not found in global_options.py")

    def test_define_logging_options_exists(self):
        # Path to the file where the specific line should be checked
        file_path = '../tornado/global_options.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Read the file content
        with open(file_path, 'r') as file:
            content = file.read()

        # Check if the line 'define_logging_options(options)' exists
        self.assertIn('define_logging_options(options)', content, "Line 'define_logging_options(options)' not found in global_options.py")



if __name__ == '__main__':
    unittest.main()