import unittest
import os
import ast

class TestScrapyMigration(unittest.TestCase):

    def test_gunzipparams_class_exists(self):
        # Path to the file where the class should be defined
        file_path = '../scrapy/utils/gz.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Check if the GunzipParams class is defined in gz.py
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        class_found = False
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef) and node.name == 'GunzipParams':
                class_found = True
                break

        self.assertTrue(class_found, "Class 'GunzipParams' not found in gz.py")

    def test_gunzipparams_has_data_and_max_size(self):
        # Path to the file where the class should be defined
        file_path = '../scrapy/utils/gz.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Check if the GunzipParams class has self.data and self.max_size attributes
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        class_node = None
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef) and node.name == 'GunzipParams':
                class_node = node
                break

        self.assertIsNotNone(class_node, "Class 'GunzipParams' not found in gz.py")

        data_found = False
        max_size_found = False
        for node in ast.walk(class_node):
            if isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Attribute) and target.attr == 'data':
                        data_found = True
                    if isinstance(target, ast.Attribute) and target.attr == 'max_size':
                        max_size_found = True

        self.assertTrue(data_found, "Attribute 'self.data' not found in GunzipParams class")
        self.assertTrue(max_size_found, "Attribute 'self.max_size' not found in GunzipParams class")

    def test_gunzip_function_signature(self):
        # Path to the file where the function should be defined
        file_path = '../scrapy/utils/gz.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Check if the gunzip function has the correct signature
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        function_found = False
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef) and node.name == 'gunzip':
                # Check function parameters
                args = node.args
                if len(args.args) == 1 and isinstance(args.args[0].annotation, ast.Name) and args.args[0].annotation.id == 'GunzipParams':
                    # Check return type
                    if isinstance(node.returns, ast.Name) and node.returns.id == 'bytes':
                        function_found = True
                        break

        self.assertTrue(function_found, "Function 'gunzip' with signature 'def gunzip(params: GunzipParams) -> bytes' not found in gz.py")

    def test_gunzip_in_sitemapspider(self):
        # Path to the file where SitemapSpider should be defined
        file_path = '../scrapy/spiders/sitemap.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Check if the SitemapSpider class has a method _get_sitemap_body that uses gunzip with GunzipParams
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        sitemapspider_class = None
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef) and node.name == 'SitemapSpider':
                sitemapspider_class = node
                break

        self.assertIsNotNone(sitemapspider_class, "Class 'SitemapSpider' not found in sitemap.py")

        method_found = False
        gunzip_params_used = False
        for node in ast.walk(sitemapspider_class):
            if isinstance(node, ast.FunctionDef) and node.name == '_get_sitemap_body':
                method_found = True
                for inner_node in ast.walk(node):
                    if isinstance(inner_node, ast.Call) and isinstance(inner_node.func, ast.Name) and inner_node.func.id == 'gunzip':
                        if len(inner_node.args) == 1:
                            arg = inner_node.args[0]
                            # Check if the argument passed to gunzip is an instance of GunzipParams
                            if isinstance(arg, ast.Name) or (isinstance(arg, ast.Attribute) and arg.attr == 'GunzipParams'):
                                gunzip_params_used = True
                                break

        self.assertTrue(method_found, "Method '_get_sitemap_body' not found in SitemapSpider class")
        self.assertTrue(gunzip_params_used, "gunzip function inside '_get_sitemap_body' does not use a 'GunzipParams' object as a parameter")

    def test_imports_in_sitemap(self):
        # Path to the file where the imports should be defined
        file_path = '../scrapy/spiders/sitemap.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Check if the correct import statement is present
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        imports_found = {
            "GunzipParams": False,
            "gunzip": False,
            "gzip_magic_number": False
        }

        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom) and node.module == 'scrapy.utils.gz':
                for alias in node.names:
                    if alias.name in imports_found:
                        imports_found[alias.name] = True

        for import_name, found in imports_found.items():
            self.assertTrue(found, f"Import '{import_name}' not found in sitemap.py")

    def test_imports_in_test_utils_gz(self):
        # Path to the test file where the imports should be defined
        test_file_path = '../tests/test_utils_gz.py'

        # Check if the test file exists
        self.assertTrue(os.path.exists(test_file_path), f"{test_file_path} does not exist")

        # Check if the correct import statement is present
        with open(test_file_path, 'r') as file:
            tree = ast.parse(file.read())

        imports_found = {
            "GunzipParams": False,
            "gunzip": False,
            "gzip_magic_number": False
        }

        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom) and node.module == 'scrapy.utils.gz':
                for alias in node.names:
                    if alias.name in imports_found:
                        imports_found[alias.name] = True

        for import_name, found in imports_found.items():
            self.assertTrue(found, f"Import '{import_name}' not found in test_utils_gz.py")

    def test_gunzipparams_used_in_test_utils_gz(self):
        # Path to the test file where gunzip should be used with GunzipParams
        test_file_path = '../tests/test_utils_gz.py'

        # Check if the test file exists
        self.assertTrue(os.path.exists(test_file_path), f"{test_file_path} does not exist")

        # Check if the gunzip function is used with GunzipParams in the test file
        with open(test_file_path, 'r') as file:
            tree = ast.parse(file.read())

        gunzip_params_used = False
        for node in ast.walk(tree):
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == 'gunzip':
                if len(node.args) == 1:
                    arg = node.args[0]
                    # Check if the argument passed to gunzip is an instance of GunzipParams
                    if isinstance(arg, ast.Name) or (isinstance(arg, ast.Attribute) and arg.attr == 'GunzipParams'):
                        gunzip_params_used = True
                        break

        self.assertTrue(gunzip_params_used, "gunzip function in 'test_utils_gz.py' does not use a 'GunzipParams' object as a parameter")

    def test_imports_in_test_downloadermiddleware_httpcompression(self):
        # Path to the test file where the imports should be defined
        test_file_path = '../tests/test_downloadermiddleware_httpcompression.py'

        # Check if the test file exists
        self.assertTrue(os.path.exists(test_file_path), f"{test_file_path} does not exist")

        # Check if the correct import statement is present
        with open(test_file_path, 'r') as file:
            tree = ast.parse(file.read())

        imports_found = {
            "GunzipParams": False,
            "gunzip": False
        }

        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom) and node.module == 'scrapy.utils.gz':
                for alias in node.names:
                    if alias.name in imports_found:
                        imports_found[alias.name] = True

        for import_name, found in imports_found.items():
            self.assertTrue(found, f"Import '{import_name}' not found in test_downloadermiddleware_httpcompression.py")
    
    def test_gunzipparams_used_in_httpcompression_middleware(self):
        # Path to the middleware file where gunzip should be used with GunzipParams
        middleware_file_path = '../scrapy/downloadermiddlewares/httpcompression.py'

        # Check if the middleware file exists
        self.assertTrue(os.path.exists(middleware_file_path), f"{middleware_file_path} does not exist")

        # Check if the gunzip function is used with GunzipParams in the middleware file
        with open(middleware_file_path, 'r') as file:
            tree = ast.parse(file.read())

        gunzip_params_used = False
        for node in ast.walk(tree):
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == 'gunzip':
                if len(node.args) == 1:
                    arg = node.args[0]
                    # Check if the argument passed to gunzip is an instance of GunzipParams
                    if isinstance(arg, ast.Name) or (isinstance(arg, ast.Attribute) and arg.attr == 'GunzipParams'):
                        gunzip_params_used = True
                        break

        self.assertTrue(gunzip_params_used, "gunzip function in 'httpcompression.py' does not use a 'GunzipParams' object as a parameter")




if __name__ == '__main__':
    unittest.main()
