import unittest
import os
import ast

class TestScrapyMigration(unittest.TestCase):

    def setUp(self):
        # Paths to the relevant files
        self.engine_file_path = '../scrapy/utils/engine.py'
        self.debug_file_path = '../scrapy/extensions/debug.py'
        self.telnet_file_path = '../scrapy/extensions/telnet.py'
        self.memusage_file_path = '../scrapy/extensions/memusage.py'
        self.docs_file_path = '../docs/topics/extensions.rst'
        self.crawl_test_file_path = '../tests/test_crawl.py'

        # Check if the engine.py file exists
        self.assertTrue(os.path.exists(self.engine_file_path), f"{self.engine_file_path} does not exist")

        # Check if the debug.py file exists
        self.assertTrue(os.path.exists(self.debug_file_path), f"{self.debug_file_path} does not exist")

        # Check if the telnet.py file exists
        self.assertTrue(os.path.exists(self.telnet_file_path), f"{self.telnet_file_path} does not exist")

        # Check if the memusage.py file exists
        self.assertTrue(os.path.exists(self.memusage_file_path), f"{self.memusage_file_path} does not exist")

        # Check if the extensions.rst file exists
        self.assertTrue(os.path.exists(self.docs_file_path), f"{self.docs_file_path} does not exist")

        # Check if the test_crawl.py file exists
        self.assertTrue(os.path.exists(self.crawl_test_file_path), f"{self.crawl_test_file_path} does not exist")

    def test_get_engine_status_function_exists(self):
        with open(self.engine_file_path, 'r') as file:
            tree = ast.parse(file.read())
        function_found = any(
            isinstance(node, ast.FunctionDef) and node.name == '_get_engine_status'
            for node in ast.walk(tree)
        )
        self.assertTrue(function_found, "Function '_get_engine_status' not found in engine.py")

    def test_format_engine_status_function_exists(self):
        with open(self.engine_file_path, 'r') as file:
            tree = ast.parse(file.read())
        function_found = any(
            isinstance(node, ast.FunctionDef) and node.name == '_format_engine_status'
            for node in ast.walk(tree)
        )
        self.assertTrue(function_found, "Function '_format_engine_status' not found in engine.py")

    def test_print_engine_status_function_exists(self):
        with open(self.engine_file_path, 'r') as file:
            tree = ast.parse(file.read())
        function_found = any(
            isinstance(node, ast.FunctionDef) and node.name == '_print_engine_status'
            for node in ast.walk(tree)
        )
        self.assertTrue(function_found, "Function '_print_engine_status' not found in engine.py")

    def test_debug_imports_format_engine_status(self):
        with open(self.debug_file_path, 'r') as file:
            tree = ast.parse(file.read())
        import_found = any(
            isinstance(node, ast.ImportFrom) and node.module == 'scrapy.utils.engine' and
            any(alias.name == '_format_engine_status' for alias in node.names)
            for node in ast.walk(tree)
        )
        self.assertTrue(import_found, "Import 'from scrapy.utils.engine import _format_engine_status' not found in debug.py")

    def test_telnet_imports_print_engine_status(self):
        with open(self.telnet_file_path, 'r') as file:
            tree = ast.parse(file.read())
        import_found = any(
            isinstance(node, ast.ImportFrom) and node.module == 'scrapy.utils.engine' and
            any(alias.name == '_print_engine_status' for alias in node.names)
            for node in ast.walk(tree)
        )
        self.assertTrue(import_found, "Import 'from scrapy.utils.engine import _print_engine_status' not found in telnet.py")

    def test_memusage_imports_get_engine_status(self):
        with open(self.memusage_file_path, 'r') as file:
            tree = ast.parse(file.read())
        import_found = any(
            isinstance(node, ast.ImportFrom) and node.module == 'scrapy.utils.engine' and
            any(alias.name == '_get_engine_status' for alias in node.names)
            for node in ast.walk(tree)
        )
        self.assertTrue(import_found, "Import 'from scrapy.utils.engine import _get_engine_status' not found in memusage.py")

    def test_docs_references_get_engine_status(self):
        # Check if the docs file contains the specific phrase
        with open(self.docs_file_path, 'r') as file:
            content = file.read()
        self.assertIn('(using ``scrapy.utils.engine._get_engine_status()``)', content,
                      "Reference to 'scrapy.utils.engine._get_engine_status' not found in extensions.rst")

    def test_crawl_test_file_imports_and_usage(self):
        with open(self.crawl_test_file_path, 'r') as file:
            tree = ast.parse(file.read())

        imports_found = {
            '_get_engine_status': False,
            '_format_engine_status': False,
        }

        usage_found = {
            '_get_engine_status': False,
            '_format_engine_status': False,
        }

        # Walk through the AST tree
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef) and node.name == 'CrawlTestCase':
                # Inside the CrawlTestCase class, look for functions
                for class_node in node.body:
                    if isinstance(class_node, ast.FunctionDef):
                        # Check for imports within functions
                        for func_node in class_node.body:
                            if isinstance(func_node, ast.ImportFrom) and func_node.module == 'scrapy.utils.engine':
                                for alias in func_node.names:
                                    if alias.name == '_get_engine_status':
                                        imports_found['_get_engine_status'] = True
                                    if alias.name == '_format_engine_status':
                                        imports_found['_format_engine_status'] = True
                        # Check for calls to functions inside this function
                        for func_node in class_node.body:
                            if isinstance(func_node, ast.FunctionDef):
                                # Look for calls to other functions within the nested function
                                for nested_func_node in ast.walk(func_node):
                                    if isinstance(nested_func_node, ast.Call):
                                        # Check if it's a direct call
                                        if isinstance(nested_func_node.func, ast.Name):
                                            if nested_func_node.func.id == '_get_engine_status':
                                                usage_found['_get_engine_status'] = True
                                            if nested_func_node.func.id == '_format_engine_status':
                                                usage_found['_format_engine_status'] = True
                                        # Check if it's a method call (e.g., object._get_engine_status())
                                        elif isinstance(nested_func_node.func, ast.Attribute):
                                            if nested_func_node.func.attr == '_get_engine_status':
                                                usage_found['_get_engine_status'] = True
                                            if nested_func_node.func.attr == '_format_engine_status':
                                                usage_found['_format_engine_status'] = True

        self.assertTrue(imports_found['_get_engine_status'], "Import 'from scrapy.utils.engine import _get_engine_status' not found in CrawlTestCase class in test_crawl.py")
        self.assertTrue(imports_found['_format_engine_status'], "Import 'from scrapy.utils.engine import _format_engine_status' not found in CrawlTestCase class in test_crawl.py")
        self.assertTrue(usage_found['_get_engine_status'], "'_get_engine_status' is not used in CrawlTestCase class in test_crawl.py")
        self.assertTrue(usage_found['_format_engine_status'], "'_format_engine_status' is not used in CrawlTestCase class in test_crawl.py")

if __name__ == '__main__':
    unittest.main()
