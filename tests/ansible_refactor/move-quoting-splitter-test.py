import unittest
import os
import ast

class TestAnsibleImports(unittest.TestCase):

    def test_config_imports_unquote(self):
        # Path to the config.py file
        file_path = '../lib/ansible/cli/config.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Check if unquote is imported
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        unquote_imported = False

        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom) and node.module == 'ansible.parsing.splitter':
                for name in node.names:
                    if name.name == 'is_quoted':
                        unquote_imported = True

        self.assertTrue(unquote_imported, "'is_quoted' not imported from 'ansible.parsing.splitter' in config.py")

    def test_dataloader_imports_unquote(self):
        # Path to the dataloader.py file
        file_path = '../lib/ansible/parsing/dataloader.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Check if unquote is imported
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        unquote_imported = False

        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom) and node.module == 'ansible.parsing.splitter':
                for name in node.names:
                    if name.name == 'unquote':
                        unquote_imported = True

        self.assertTrue(unquote_imported, "'unquote' not imported from 'ansible.parsing.splitter' in dataloader.py")

    def test_splitter_contains_unquote_and_is_quoted(self):
        # Path to the splitter.py file
        file_path = '../lib/ansible/parsing/splitter.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Check if unquote and is_quoted are defined
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        unquote_found = False
        is_quoted_found = False

        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                if node.name == 'unquote':
                    unquote_found = True
                if node.name == 'is_quoted':
                    is_quoted_found = True

        self.assertTrue(unquote_found, "'unquote' function not found in splitter.py")
        self.assertTrue(is_quoted_found, "'is_quoted' function not found in splitter.py")

    def test_schema_imports_unquote(self):
        # Path to the schema.py file
        file_path = '../test/lib/ansible_test/_util/controller/sanity/validate-modules/validate_modules/schema.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Check if unquote is imported
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        unquote_imported = False

        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom) and node.module == 'ansible.parsing.splitter':
                for name in node.names:
                    if name.name == 'unquote':
                        unquote_imported = True

        self.assertTrue(unquote_imported, "'unquote' not imported from 'ansible.parsing.splitter' in schema.py")

    def test_test_unquote_imports_unquote(self):
        # Path to the test_unquote.py file
        file_path = '../test/units/parsing/test_unquote.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Check if unquote is imported
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        unquote_imported = False

        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom) and node.module == 'ansible.parsing.splitter':
                for name in node.names:
                    if name.name == 'unquote':
                        unquote_imported = True

        self.assertTrue(unquote_imported, "'unquote' not imported from 'ansible.parsing.splitter' in test_unquote.py")

    def test_quoting_file_deleted(self):
        # Path to the quoting.py file
        file_path = '../lib/ansible/parsing/quoting.py'

        # Check if the file has been deleted
        self.assertFalse(os.path.exists(file_path), f"{file_path} should be deleted but still exists")


if __name__ == '__main__':
    unittest.main()
