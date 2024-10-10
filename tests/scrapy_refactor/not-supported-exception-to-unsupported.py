import unittest
import os
import ast

class TestScrapyMigration(unittest.TestCase):

    def test_not_supported_not_imported_in_downloader_init(self):
        file_path = '../scrapy/core/downloader/handlers/__init__.py'
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        not_supported_found = False
        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom):
                if any(alias.name == 'NotSupported' for alias in node.names):
                    not_supported_found = True
                    break

        self.assertFalse(not_supported_found, f"Import 'NotSupported' found in {file_path}")

    def test_not_supported_not_imported_in_http_response_init(self):
        file_path = '../scrapy/http/response/__init__.py'
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        not_supported_found = False
        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom):
                if any(alias.name == 'NotSupported' for alias in node.names):
                    not_supported_found = True
                    break

        self.assertFalse(not_supported_found, f"Import 'NotSupported' found in {file_path}")

    def test_not_supported_not_imported_in_feed_spiders(self):
        file_path = '../scrapy/spiders/feed.py'
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        not_supported_found = False
        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom):
                if any(alias.name == 'NotSupported' for alias in node.names):
                    not_supported_found = True
                    break

        self.assertFalse(not_supported_found, f"Import 'NotSupported' found in {file_path}")

    def test_not_supported_not_imported_in_test_http_response(self):
        file_path = '../tests/test_http_response.py'
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        not_supported_found = False
        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom):
                if any(alias.name == 'NotSupported' for alias in node.names):
                    not_supported_found = True
                    break

        self.assertFalse(not_supported_found, f"Import 'NotSupported' found in {file_path}")

    def test_unsupported_class_defined_in_exceptions(self):
        file_path = '../scrapy/exceptions.py'
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        class_found = False
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef) and node.name == 'Unsupported':
                # Check if Unsupported inherits from Exception
                if any(isinstance(base, ast.Name) and base.id == 'Exception' for base in node.bases):
                    class_found = True
                    break

        self.assertTrue(class_found, "Class 'Unsupported(Exception)' not found in exceptions.py")

    def test_not_supported_replaced_with_unsupported_in_exceptions_rst(self):
        file_path = '../docs/topics/exceptions.rst'
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        with open(file_path, 'r') as file:
            content = file.read()

        not_supported_present = 'NotSupported' in content
        unsupported_present = 'Unsupported' in content

        self.assertFalse(not_supported_present, "The term 'NotSupported' is still present in exceptions.rst")
        self.assertTrue(unsupported_present, "The term 'Unsupported' is not present in exceptions.rst")

    def test_unsupported_exception_used_in_downloader_init(self):
        file_path = '../scrapy/core/downloader/handlers/__init__.py'
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        unsupported_used = False
        for node in ast.walk(tree):
            if isinstance(node, ast.Raise) and isinstance(node.exc, ast.Call):
                if isinstance(node.exc.func, ast.Name) and node.exc.func.id == 'Unsupported':
                    unsupported_used = True
                    break

        self.assertTrue(unsupported_used, f"Unsupported exception is not used in {file_path}")

    def test_unsupported_exception_used_in_http_response_init(self):
        file_path = '../scrapy/http/response/__init__.py'
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        unsupported_used = False
        for node in ast.walk(tree):
            if isinstance(node, ast.Raise) and isinstance(node.exc, ast.Call):
                if isinstance(node.exc.func, ast.Name) and node.exc.func.id == 'Unsupported':
                    unsupported_used = True
                    break

        self.assertTrue(unsupported_used, f"Unsupported exception is not used in {file_path}")

    def test_unsupported_exception_used_in_feed_spiders(self):
        file_path = '../scrapy/spiders/feed.py'
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        unsupported_used = False
        for node in ast.walk(tree):
            if isinstance(node, ast.Raise) and isinstance(node.exc, ast.Call):
                if isinstance(node.exc.func, ast.Name) and node.exc.func.id == 'Unsupported':
                    unsupported_used = True
                    break

        self.assertTrue(unsupported_used, f"Unsupported exception is not used in {file_path}")

    def test_unsupported_exception_used_in_test_http_response(self):
        file_path = '../tests/test_http_response.py'
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        unsupported_used = False
        for node in ast.walk(tree):
            if isinstance(node, ast.Call):
                # Check if the call is assertRaisesRegex
                if isinstance(node.func, ast.Attribute) and node.func.attr == 'assertRaisesRegex':
                    # Check if the first argument is Unsupported
                    if isinstance(node.args[0], ast.Name) and node.args[0].id == 'Unsupported':
                        unsupported_used = True
                        break

        self.assertTrue(unsupported_used, "assertRaisesRegex with Unsupported exception is not used in test_http_response.py")


if __name__ == '__main__':
    unittest.main()
