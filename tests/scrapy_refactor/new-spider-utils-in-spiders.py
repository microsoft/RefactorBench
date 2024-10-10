import unittest
import os
import ast

class TestScrapyMigration(unittest.TestCase):

    def setUp(self):
        # Paths to the relevant files
        self.spider_utils_path = '../scrapy/spiders/spider_utils.py'
        self.sitemap_path = '../scrapy/spiders/sitemap.py'
        self.crawl_path = '../scrapy/spiders/crawl.py'

        # Check if the spider_utils file exists
        self.assertTrue(os.path.exists(self.spider_utils_path), f"{self.spider_utils_path} does not exist")

        # Parse the spider_utils file into an AST tree
        with open(self.spider_utils_path, 'r') as file:
            self.spider_utils_tree = ast.parse(file.read())

        # Check if the sitemap file exists
        self.assertTrue(os.path.exists(self.sitemap_path), f"{self.sitemap_path} does not exist")

        # Parse the sitemap file into an AST tree
        with open(self.sitemap_path, 'r') as file:
            self.sitemap_tree = ast.parse(file.read())

        # Check if the crawl file exists
        self.assertTrue(os.path.exists(self.crawl_path), f"{self.crawl_path} does not exist")

        # Parse the crawl file into an AST tree
        with open(self.crawl_path, 'r') as file:
            self.crawl_tree = ast.parse(file.read())

    def _function_exists(self, tree, function_name):
        """Helper function to check if a function exists in the AST."""
        return any(
            isinstance(node, ast.FunctionDef) and node.name == function_name
            for node in ast.walk(tree)
        )

    def _import_exists(self, tree, module_name, import_names):
        """Helper function to check if a specific import statement exists."""
        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom) and node.module == module_name:
                imported_names = [alias.name for alias in node.names]
                if all(name in imported_names for name in import_names):
                    return True
        return False

    def test_identity_function_exists(self):
        self.assertTrue(
            self._function_exists(self.spider_utils_tree, '_identity'),
            "Function '_identity' not found in spider_utils.py"
        )

    def test_get_method_function_exists(self):
        self.assertTrue(
            self._function_exists(self.spider_utils_tree, '_get_method'),
            "Function '_get_method' not found in spider_utils.py"
        )

    def test_regex_function_exists(self):
        self.assertTrue(
            self._function_exists(self.spider_utils_tree, 'regex'),
            "Function 'regex' not found in spider_utils.py"
        )

    def test_iterloc_function_exists(self):
        self.assertTrue(
            self._function_exists(self.spider_utils_tree, 'iterloc'),
            "Function 'iterloc' not found in spider_utils.py"
        )

    def test_required_imports_exist(self):
        required_imports = [
            ('import re', []),
            ('typing', ['Any', 'Dict', 'Iterable', 'Callable', 'Optional', 'TypeVar', 'Union']),
            ('scrapy.http', ['Request', 'Response']),
            ('scrapy.spiders', ['Spider'])
        ]

        for module, imports in required_imports:
            if module == 'import re':  # Handle standard imports separately
                self.assertTrue(
                    any(isinstance(node, ast.Import) and any(alias.name == 're' for alias in node.names)
                        for node in ast.walk(self.spider_utils_tree)),
                    "Required import 'import re' not found in spider_utils.py"
                )
            else:
                self.assertTrue(
                    self._import_exists(self.spider_utils_tree, module, imports),
                    f"Required import 'from {module} import {', '.join(imports)}' not found in spider_utils.py"
                )

    def test_t_alias_exists(self):
        alias_found = any(
            isinstance(node, ast.Assign) and
            any(target.id == '_T' for target in node.targets)
            for node in ast.walk(self.spider_utils_tree)
        )
        self.assertTrue(alias_found, "Alias '_T' not found in spider_utils.py")

    def test_sitemap_imports_spider_utils(self):
        import_found = self._import_exists(
            self.sitemap_tree, 'scrapy.spiders.spider_utils', ['regex', 'iterloc']
        )
        self.assertTrue(
            import_found,
            "Import 'from scrapy.spiders.spider_utils import regex, iterloc' not found in sitemap.py"
        )

    def test_crawl_imports_spider_utils(self):
        import_found = self._import_exists(
            self.crawl_tree, 'scrapy.spiders.spider_utils', ['_get_method', '_identity', '_identity_process_request']
        )
        self.assertTrue(
            import_found,
            "Import 'from scrapy.spiders.spider_utils import _get_method, _identity, _identity_process_request' not found in crawl.py"
        )

if __name__ == '__main__':
    unittest.main()
