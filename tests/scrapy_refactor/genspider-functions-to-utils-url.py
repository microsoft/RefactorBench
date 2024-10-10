import unittest
import os
import ast

class TestFunctionMigration(unittest.TestCase):

    def test_functions_moved_to_utils_url(self):
        # Path to the file where the functions should be moved
        utils_url_path = '../scrapy/utils/url.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(utils_url_path), f"{utils_url_path} does not exist")

        # Check if the functions are defined in url.py
        with open(utils_url_path, 'r') as file:
            tree = ast.parse(file.read())

        functions_to_check = ['verify_url_scheme', 'sanitize_module_name', 'extract_domain']
        functions_found = {function: False for function in functions_to_check}

        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef) and node.name in functions_found:
                functions_found[node.name] = True

        for function, found in functions_found.items():
            self.assertTrue(found, f"Function '{function}' not found in url.py")

    def test_functions_removed_from_genspider(self):
        # Path to the file where the functions should be removed from
        genspider_path = '../scrapy/commands/genspider.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(genspider_path), f"{genspider_path} does not exist")

        # Check if the functions are not defined in genspider.py
        with open(genspider_path, 'r') as file:
            tree = ast.parse(file.read())

        functions_to_check = ['verify_url_scheme', 'sanitize_module_name', 'extract_domain']
        functions_found = {function: False for function in functions_to_check}

        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef) and node.name in functions_found:
                functions_found[node.name] = True

        for function, found in functions_found.items():
            self.assertFalse(found, f"Function '{function}' should not be found in genspider.py")

    def test_utils_url_imports_string(self):
        # Path to the file where the string module should be imported
        utils_url_path = '../scrapy/utils/url.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(utils_url_path), f"{utils_url_path} does not exist")

        # Check if the string module is imported in url.py
        with open(utils_url_path, 'r') as file:
            tree = ast.parse(file.read())

        string_import_found = False
        for node in ast.walk(tree):
            if isinstance(node, ast.Import) or isinstance(node, ast.ImportFrom):
                if isinstance(node, ast.Import):
                    if any(alias.name == 'string' for alias in node.names):
                        string_import_found = True
                        break
                elif isinstance(node, ast.ImportFrom) and node.module == 'string':
                    string_import_found = True
                    break

        self.assertTrue(string_import_found, "The 'string' module is not imported in url.py")

    def test_genspider_imports_from_utils_url(self):
        # Path to the file where the imports should be present
        genspider_path = '../scrapy/commands/genspider.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(genspider_path), f"{genspider_path} does not exist")

        # Check if the required imports are present in genspider.py
        with open(genspider_path, 'r') as file:
            tree = ast.parse(file.read())

        import_found = False
        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom) and node.module == 'scrapy.utils.url':
                imported_functions = {alias.name for alias in node.names}
                if {'extract_domain', 'sanitize_module_name', 'verify_url_scheme'}.issubset(imported_functions):
                    import_found = True
                    break

        self.assertTrue(import_found, 
            "The imports 'from scrapy.utils.url import extract_domain, sanitize_module_name, verify_url_scheme' were not found in genspider.py")

if __name__ == '__main__':
    unittest.main()
