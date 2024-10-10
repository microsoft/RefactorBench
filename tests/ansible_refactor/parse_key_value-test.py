import unittest
import os
import ast

class TestAnsibleImports(unittest.TestCase):

    def test_parse_key_value_defined_in_splitter_py(self):
        file_path = '../lib/ansible/parsing/splitter.py'
        function_name = 'parse_key_value'
        
        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")
        
        # Read and parse the file
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())
        
        # Check if the function parse_key_value is defined
        function_defined = False
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef) and node.name == function_name:
                function_defined = True
                break

        self.assertTrue(function_defined, f"Function '{function_name}' is not defined in {file_path}")

    def test_import_in_hacking_test_module_py(self):
        file_path = '../hacking/test-module.py'
        module_name = 'ansible.parsing.splitter'
        import_name = 'parse_key_value'
        
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")
        
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())
        
        import_found = False
        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom) and node.module == module_name:
                for name in node.names:
                    if name.name == import_name:
                        import_found = True
                        break

        self.assertTrue(import_found, f"Import '{import_name}' from '{module_name}' not found in {file_path}")

    def test_no_parse_kv_in_hacking_test_module_py(self):
        file_path = '../hacking/test-module.py'
        
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")
        
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        parse_kv_used = any(
            isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == 'parse_kv'
            for node in ast.walk(tree)
        )

        self.assertFalse(parse_kv_used, f"'parse_kv' should not be used in {file_path}")

    def test_import_in_lib_ansible_cli_adhoc_py(self):
        file_path = '../lib/ansible/cli/adhoc.py'
        module_name = 'ansible.parsing.splitter'
        import_name = 'parse_key_value'
        
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")
        
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())
        
        import_found = False
        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom) and node.module == module_name:
                for name in node.names:
                    if name.name == import_name:
                        import_found = True
                        break

        self.assertTrue(import_found, f"Import '{import_name}' from '{module_name}' not found in {file_path}")

    def test_no_parse_kv_in_lib_ansible_cli_adhoc_py(self):
        file_path = '../lib/ansible/cli/adhoc.py'
        
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")
        
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        parse_kv_used = any(
            isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == 'parse_kv'
            for node in ast.walk(tree)
        )

        self.assertFalse(parse_kv_used, f"'parse_kv' should not be used in {file_path}")

    def test_import_in_lib_ansible_cli_console_py(self):
        file_path = '../lib/ansible/cli/console.py'
        module_name = 'ansible.parsing.splitter'
        import_name = 'parse_key_value'
        
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")
        
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())
        
        import_found = False
        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom) and node.module == module_name:
                for name in node.names:
                    if name.name == import_name:
                        import_found = True
                        break

        self.assertTrue(import_found, f"Import '{import_name}' from '{module_name}' not found in {file_path}")

    def test_no_parse_kv_in_lib_ansible_cli_console_py(self):
        file_path = '../lib/ansible/cli/console.py'
        
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")
        
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        parse_kv_used = any(
            isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == 'parse_kv'
            for node in ast.walk(tree)
        )

        self.assertFalse(parse_kv_used, f"'parse_kv' should not be used in {file_path}")

    def test_import_in_lib_ansible_parsing_mod_args_py(self):
        file_path = '../lib/ansible/parsing/mod_args.py'
        module_name = 'ansible.parsing.splitter'
        import_name = 'parse_key_value'
        
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")
        
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())
        
        import_found = False
        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom) and node.module == module_name:
                for name in node.names:
                    if name.name == import_name:
                        import_found = True
                        break

        self.assertTrue(import_found, f"Import '{import_name}' from '{module_name}' not found in {file_path}")

    def test_no_parse_kv_in_lib_ansible_parsing_mod_args_py(self):
        file_path = '../lib/ansible/parsing/mod_args.py'
        
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")
        
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        parse_kv_used = any(
            isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == 'parse_kv'
            for node in ast.walk(tree)
        )

        self.assertFalse(parse_kv_used, f"'parse_kv' should not be used in {file_path}")

    def test_import_in_lib_ansible_parsing_splitter_py(self):
        file_path = '../lib/ansible/parsing/splitter.py'
        module_name = 'ansible.parsing.quoting'
        import_name = 'unquote'
        
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")
        
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())
        
        import_found = False
        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom) and node.module == module_name:
                for name in node.names:
                    if name.name == import_name:
                        import_found = True
                        break

        self.assertTrue(import_found, f"Import '{import_name}' from '{module_name}' not found in {file_path}")

    def test_no_parse_kv_in_lib_ansible_parsing_splitter_py(self):
        file_path = '../lib/ansible/parsing/splitter.py'
        
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")
        
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        parse_kv_used = any(
            isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == 'parse_kv'
            for node in ast.walk(tree)
        )

        self.assertFalse(parse_kv_used, f"'parse_kv' should not be defined in {file_path}")

    def test_import_in_lib_ansible_plugins_lookup_csvfile_py(self):
        file_path = '../lib/ansible/plugins/lookup/csvfile.py'
        module_name = 'ansible.parsing.splitter'
        import_name = 'parse_key_value'
        
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")
        
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())
        
        import_found = False
        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom) and node.module == module_name:
                for name in node.names:
                    if name.name == import_name:
                        import_found = True
                        break

        self.assertTrue(import_found, f"Import '{import_name}' from '{module_name}' not found in {file_path}")

    def test_no_parse_kv_in_lib_ansible_plugins_lookup_csvfile_py(self):
        file_path = '../lib/ansible/plugins/lookup/csvfile.py'
        
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")
        
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        parse_kv_used = any(
            isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == 'parse_kv'
            for node in ast.walk(tree)
        )

        self.assertFalse(parse_kv_used, f"'parse_kv' should not be used in {file_path}")

    def test_import_in_lib_ansible_plugins_lookup_password_py(self):
        file_path = '../lib/ansible/plugins/lookup/password.py'
        module_name = 'ansible.parsing.splitter'
        import_name = 'parse_key_value'
        
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")
        
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())
        
        import_found = False
        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom) and node.module == module_name:
                for name in node.names:
                    if name.name == import_name:
                        import_found = True
                        break

        self.assertTrue(import_found, f"Import '{import_name}' from '{module_name}' not found in {file_path}")

    def test_no_parse_kv_in_lib_ansible_plugins_lookup_password_py(self):
        file_path = '../lib/ansible/plugins/lookup/password.py'
        
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")
        
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        parse_kv_used = any(
            isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == 'parse_kv'
            for node in ast.walk(tree)
        )

        self.assertFalse(parse_kv_used, f"'parse_kv' should not be used in {file_path}")

    def test_import_in_lib_ansible_plugins_lookup_sequence_py(self):
        file_path = '../lib/ansible/plugins/lookup/sequence.py'
        module_name = 'ansible.parsing.splitter'
        import_name = 'parse_key_value'
        
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")
        
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())
        
        import_found = False
        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom) and node.module == module_name:
                for name in node.names:
                    if name.name == import_name:
                        import_found = True
                        break

        self.assertTrue(import_found, f"Import '{import_name}' from '{module_name}' not found in {file_path}")

    def test_no_parse_kv_in_lib_ansible_plugins_lookup_sequence_py(self):
        file_path = '../lib/ansible/plugins/lookup/sequence.py'
        
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")
        
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        parse_kv_used = any(
            isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == 'parse_kv'
            for node in ast.walk(tree)
        )

        self.assertFalse(parse_kv_used, f"'parse_kv' should not be used in {file_path}")

    def test_import_in_lib_ansible_utils_vars_py(self):
        file_path = '../lib/ansible/utils/vars.py'
        module_name = 'ansible.parsing.splitter'
        import_name = 'parse_key_value'
        
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")
        
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())
        
        import_found = False
        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom) and node.module == module_name:
                for name in node.names:
                    if name.name == import_name:
                        import_found = True
                        break

        self.assertTrue(import_found, f"Import '{import_name}' from '{module_name}' not found in {file_path}")

    def test_no_parse_kv_in_lib_ansible_utils_vars_py(self):
        file_path = '../lib/ansible/utils/vars.py'
        
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")
        
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        parse_kv_used = any(
            isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == 'parse_kv'
            for node in ast.walk(tree)
        )

        self.assertFalse(parse_kv_used, f"'parse_kv' should not be used in {file_path}")

    def test_import_in_test_units_parsing_test_splitter_py(self):
        file_path = '../test/units/parsing/test_splitter.py'
        module_name = 'ansible.parsing.splitter'
        import_name = 'parse_key_value'
        
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")
        
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())
        
        import_found = False
        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom) and node.module == module_name:
                for name in node.names:
                    if name.name == import_name:
                        import_found = True
                        break

        self.assertTrue(import_found, f"Import '{import_name}' from '{module_name}' not found in {file_path}")

    def test_no_parse_kv_in_test_units_parsing_test_splitter_py(self):
        file_path = '../test/units/parsing/test_splitter.py'
        
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")
        
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        parse_kv_used = any(
            isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == 'parse_kv'
            for node in ast.walk(tree)
        )

        self.assertFalse(parse_kv_used, f"'parse_kv' should not be used in {file_path}")

if __name__ == '__main__':
    unittest.main()
