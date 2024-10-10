import unittest
import os
import ast

class TestScrapyMigration(unittest.TestCase):

    def test_sitemap_urls_from_robots_moved(self):
        # Path to the file where the function should be moved
        file_path = '../scrapy/utils/url.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Check if the function is defined in url.py
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        function_found = False
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef) and node.name == 'sitemap_urls_from_robots':
                function_found = True
                break

        self.assertTrue(function_found, "Function 'sitemap_urls_from_robots' not found in url.py")

    def test_tests_py_imports_updated(self):
        # Path to the test file
        tests_file_path = '../tests/test_utils_sitemap.py' 

        # Check if the test file exists
        self.assertTrue(os.path.exists(tests_file_path), f"Test file {tests_file_path} does not exist")

        # Check if the import statement is correct
        with open(tests_file_path, 'r') as file:
            tree = ast.parse(file.read())

        import_found = False
        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom):
                if node.module == 'scrapy.utils.url' and \
                   any(alias.name == 'sitemap_urls_from_robots' for alias in node.names):
                    import_found = True
                    break

        self.assertTrue(import_found, "Import 'from scrapy.utils.url import sitemap_urls_from_robots' not found in test_utils_sitemap.py")

    def test_spider_import_updated(self):
        # Path to the spider file
        spider_file_path = '../scrapy/spiders/sitemap.py'

        # Check if the spider file exists
        self.assertTrue(os.path.exists(spider_file_path), f"Spider file {spider_file_path} does not exist")

        # Check if the correct import statement is present
        with open(spider_file_path, 'r') as file:
            tree = ast.parse(file.read())

        import_found = False
        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom):
                if node.module == 'scrapy.utils.url' and \
                   any(alias.name == 'sitemap_urls_from_robots' for alias in node.names):
                    import_found = True
                    break

        self.assertTrue(import_found, "Import 'from scrapy.utils.url import sitemap_urls_from_robots' not found in sitemap.py")

if __name__ == '__main__':
    unittest.main()
