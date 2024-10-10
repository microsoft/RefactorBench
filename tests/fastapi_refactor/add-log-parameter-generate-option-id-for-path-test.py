import unittest
import os
import ast

class TestFastAPIUtils(unittest.TestCase):

    def test_utils_file_exists(self):
        # Path to the file where the functions should be defined
        file_path = '../fastapi/utils.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

    def test_generate_operation_id_for_path_has_log_parameter_with_default_false(self):
        # Path to the file where the generate_operation_id_for_path function should be defined
        file_path = '../fastapi/utils.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Parse the utils.py file to check for the generate_operation_id_for_path function and its parameters
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        generate_operation_id_for_path_function = None

        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef) and node.name == 'generate_operation_id_for_path':
                generate_operation_id_for_path_function = node
                break

        # Check if the function is defined
        self.assertIsNotNone(generate_operation_id_for_path_function, "Function 'generate_operation_id_for_path' not found in utils.py")

        # Check if the function has a 'log' parameter with a default value of False
        parameter_found = False
        for kwarg in generate_operation_id_for_path_function.args.kwonlyargs:
            if kwarg.arg == 'log':
                # Find the corresponding default value index
                default_value_index = generate_operation_id_for_path_function.args.kwonlyargs.index(kwarg)
                default_value = generate_operation_id_for_path_function.args.kw_defaults[default_value_index]
                
                if isinstance(default_value, ast.Constant) and default_value.value is False:
                    parameter_found = True
                break

        self.assertTrue(parameter_found, "'log' parameter with default value False not found in 'generate_operation_id_for_path' function")

    def test_openapi_utils_file_exists(self):
        # Path to the file where the import should be checked
        file_path = '../fastapi/openapi/utils.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

    def test_import_from_fastapi_utils(self):
        # Path to the file where the import should be checked
        file_path = '../fastapi/openapi/utils.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Parse the utils.py file to check for the specific import
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        import_found = False

        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom) and node.module == 'fastapi.utils':
                imported_names = {alias.name for alias in node.names}
                if {'deep_dict_update', 'generate_operation_id_for_path', 'is_body_allowed_for_status_code'}.issubset(imported_names):
                    import_found = True
                    break

        self.assertTrue(import_found, "The required import statement from 'fastapi.utils' is not found in 'fastapi/openapi/utils.py'")

    def test_generate_operation_id_for_path_calls_log_true(self):
        # Path to the file where the function calls should be checked
        file_path = '../fastapi/openapi/utils.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Parse the utils.py file to check for calls to generate_operation_id_for_path
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        # Find all calls to generate_operation_id_for_path
        calls_with_log_true = True

        for node in ast.walk(tree):
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == 'generate_operation_id_for_path':
                # Check if the call has the argument log=True
                has_log_true = False
                for keyword in node.keywords:
                    if keyword.arg == 'log' and isinstance(keyword.value, ast.Constant) and keyword.value.value is True:
                        has_log_true = True
                        break
                
                if not has_log_true:
                    calls_with_log_true = False
                    break

        self.assertTrue(calls_with_log_true, "Not all calls to 'generate_operation_id_for_path' have 'log=True' in 'fastapi/openapi/utils.py'")

    
if __name__ == '__main__':
    unittest.main()
