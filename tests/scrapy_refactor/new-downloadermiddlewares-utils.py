import unittest
import os
import ast

class TestScrapyMigration(unittest.TestCase):

    def test_downloadermiddlewares_file_exists(self):
        # Path to the file where the functions should be located
        file_path = '../scrapy/utils/downloadermiddlewares.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

    def test_get_status_size_function_exists(self):
        # Path to the file where the function should be located
        file_path = '../scrapy/utils/downloadermiddlewares.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Check if the function is defined in downloadermiddlewares.py
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        function_found = False
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef) and node.name == 'get_status_size':
                function_found = True
                break

        self.assertTrue(function_found, "Function 'get_status_size' not found in downloadermiddlewares.py")

    def test_get_header_size_function_exists(self):
        # Path to the file where the function should be located
        file_path = '../scrapy/utils/downloadermiddlewares.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Check if the function is defined in downloadermiddlewares.py
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        function_found = False
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef) and node.name == 'get_header_size':
                function_found = True
                break

        self.assertTrue(function_found, "Function 'get_header_size' not found in downloadermiddlewares.py")

    def test_downloadermiddlewares_imports(self):
        # Path to the file where the imports should be located
        file_path = '../scrapy/utils/downloadermiddlewares.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Parse the file and check for imports
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        required_imports = {
            'typing': {'Dict', 'List', 'Tuple', 'Union'},
            'twisted.web.http': set(),
            'scrapy.utils.python': {'to_bytes'}
        }

        imports_found = {
            'typing': set(),
            'twisted.web.http': set(),
            'scrapy.utils.python': set()
        }

        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom):
                if node.module == 'typing':
                    for alias in node.names:
                        if alias.name in required_imports['typing']:
                            imports_found['typing'].add(alias.name)
                elif node.module == 'twisted.web.http':
                    imports_found['twisted.web.http'] = set()
                elif node.module == 'scrapy.utils.python':
                    for alias in node.names:
                        if alias.name == 'to_bytes':
                            imports_found['scrapy.utils.python'].add(alias.name)

        # Check that all required imports were found
        for module, names in required_imports.items():
            if names:
                self.assertTrue(names.issubset(imports_found[module]), f"Missing imports from '{module}': {names - imports_found[module]}")
            else:
                self.assertTrue(imports_found[module] == names, f"Missing imports from '{module}'")

    def test_stats_imports_get_size_functions(self):
        # Path to the stats file where the import should be located
        file_path = '../scrapy/downloadermiddlewares/stats.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Parse the file and check for the specific import
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        import_found = False
        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom):
                if node.module == 'scrapy.utils.downloadermiddlewares' and \
                   any(alias.name == 'get_header_size' for alias in node.names) and \
                   any(alias.name == 'get_status_size' for alias in node.names):
                    import_found = True
                    break

        self.assertTrue(import_found, "Import 'from scrapy.utils.downloadermiddlewares import get_header_size, get_status_size' not found in stats.py")

if __name__ == '__main__':
    unittest.main()
