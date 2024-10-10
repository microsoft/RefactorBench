import unittest
import os
import ast

class TestFunctionRefactoring(unittest.TestCase):

    def test_old_functions_removed(self):
        # Path to the file where the functions should be located
        file_path = '../src/requests/utils.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Parse the file to check the presence of old functions
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        from_key_found = False
        to_key_found = False

        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                if node.name == 'from_key_val_list':
                    from_key_found = True
                if node.name == 'to_key_val_list':
                    to_key_found = True

        self.assertFalse(from_key_found, "Function 'from_key_val_list' is still present in the file")
        self.assertFalse(to_key_found, "Function 'to_key_val_list' is still present in the file")

    def test_new_function_exists(self):
        # Path to the file where the new function should be located
        file_path = '../src/requests/utils.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Parse the file to check the new function's parameters
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        function_found = False
        to_dict_is_second_param = False

        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef) and node.name == 'key_val_convert':
                function_found = True
                # Check if the second parameter is 'to_dict'
                if len(node.args.args) > 1 and node.args.args[1].arg == 'to_dict':
                    to_dict_is_second_param = True
                break

        self.assertTrue(function_found, "Function 'key_val_convert' not found in the file")
        self.assertTrue(to_dict_is_second_param, "The 'to_dict' parameter in 'key_val_convert' is not the second parameter")



    def test_sessions_imports(self):
        # Path to the file where the imports should be located
        file_path = '../src/requests/sessions.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Parse the file to check for the imports
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        expected_imports = {
            "DEFAULT_PORTS", "default_headers", "get_auth_from_url", "get_environ_proxies",
            "get_netrc_auth", "requote_uri", "resolve_proxies", "rewind_body",
            "should_bypass_proxies", "key_val_convert"
        }
        actual_imports = set()

        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom) and node.module == 'utils':
                for alias in node.names:
                    actual_imports.add(alias.name)

        self.assertTrue(expected_imports.issubset(actual_imports), 
                        f"Not all expected imports are present in 'sessions.py'. Missing: {expected_imports - actual_imports}")

    def test_model_imports(self):
        # Path to the file where the imports should be located
        file_path = '../src/requests/models.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Parse the file to check for the imports
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        expected_imports = {
            "check_header_validity", "get_auth_from_url", "guess_filename", "guess_json_utf",
            "iter_slices", "parse_header_links", "requote_uri", "stream_decode_response_unicode",
            "super_len", "key_val_convert"
        }
        actual_imports = set()

        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom) and node.module == 'utils':
                for alias in node.names:
                    actual_imports.add(alias.name)

        self.assertTrue(expected_imports.issubset(actual_imports), 
                        f"Not all expected imports are present in 'models.py'. Missing: {expected_imports - actual_imports}")

    def test_key_val_convert_to_dict_false(self):
        # Files to check for the correct usage of key_val_convert
        files_to_check = [
            '../src/requests/models.py',
            '../src/requests/sessions.py',
            '../tests/test_utils.py'
        ]

        for file_path in files_to_check:
            # Check if the file exists
            self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

            # Parse the file to check the function call's arguments
            with open(file_path, 'r') as file:
                tree = ast.parse(file.read())

            key_val_convert_calls = 0
            correct_param_usage = 0

            for node in ast.walk(tree):
                if isinstance(node, ast.FunctionDef):  # Look inside functions
                    for child in ast.walk(node):
                        if isinstance(child, ast.Call) and isinstance(child.func, ast.Name) and child.func.id == 'key_val_convert':
                            key_val_convert_calls += 1
                            
                            # Check if 'to_dict' parameter is set to False as the second argument
                            if len(child.args) > 1 and isinstance(child.args[1], ast.Constant) and child.args[1].value is False:
                                correct_param_usage += 1
                            else:
                                # Check keyword arguments for 'to_dict'
                                for keyword in child.keywords:
                                    if keyword.arg == 'to_dict' and isinstance(keyword.value, ast.Constant) and keyword.value.value is False:
                                        correct_param_usage += 1
                                        break

            self.assertEqual(key_val_convert_calls, correct_param_usage, 
                             f"{key_val_convert_calls} != {correct_param_usage}  Not all 'key_val_convert' calls in {file_path} have 'to_dict=False' as the second argument")

if __name__ == '__main__':
    unittest.main()
