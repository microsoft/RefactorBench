import unittest
import os
import ast
import json

class TestCeleryRetryDocumentation(unittest.TestCase):

    def test_autoretry_file_does_not_exist(self):
        # Path to the file that should not exist
        file_path = '../celery/app/autoretry.py'

        # Check if the file does not exist
        self.assertFalse(os.path.exists(file_path), f"{file_path} should not exist")

    def test_retry_file_exists(self):
        # Path to the file that should exist
        file_path = '../celery/app/retry.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

    def test_docs_reference_does_not_contain_autoretry(self):
        # Path to the documentation file that should be checked
        docs_path = '../docs/reference/index.rst'

        # Check if the documentation file exists
        self.assertTrue(os.path.exists(docs_path), f"{docs_path} does not exist")

        # Read the content of the documentation file
        with open(docs_path, 'r') as file:
            content = file.read()

        # Ensure 'celery.app.autoretry' is not in the documentation
        self.assertNotIn('celery.app.autoretry', content, "'celery.app.autoretry' found in docs/reference/index.rst")

        # Ensure 'celery.app.retry' is in the documentation
        self.assertIn('celery.app.retry', content, "'celery.app.retry' not found in docs/reference/index.rst")

    def test_base_imports_add_autoretry_behaviour(self):
        # Path to the file that should be checked
        file_path = '../celery/app/base.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Parse the base.py file to check for the specific import
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        import_found = False

        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom):
                if node.module == 'retry':
                    imported_names = {alias.name for alias in node.names}
                    if 'add_autoretry_behaviour' in imported_names:
                        import_found = True
                        break

        self.assertTrue(import_found, "'from .retry import add_autoretry_behaviour' not found in base.py")

    def test_autoretry_rst_deleted(self):
        # Path to the documentation file that should be deleted
        rst_path = '../docs/reference/celery.app.autoretry.rst'

        # Check if the file does not exist
        self.assertFalse(os.path.exists(rst_path), f"{rst_path} should be deleted")

    def test_retry_rst_added(self):
        # Path to the new documentation file that should be added
        rst_path = '../docs/reference/celery.app.retry.rst'

        # Check if the file exists
        self.assertTrue(os.path.exists(rst_path), f"{rst_path} should exist")
        
    def test_bandit_json_contains_retry_and_not_autoretry(self):
        # Path to the bandit.json file that should be checked
        bandit_path = '../bandit.json'

        # Check if the bandit.json file exists
        self.assertTrue(os.path.exists(bandit_path), f"{bandit_path} does not exist")

        # Read the content of the bandit.json file as text
        with open(bandit_path, 'r') as file:
            content = file.read()

        # Check that "celery/app/retry.py" is in the content
        self.assertIn("celery/app/retry.py", content, "'celery/app/retry.py' not found in bandit.json")

        # Check that "celery/app/autoretry.py" is not in the content
        self.assertNotIn("celery/app/autoretry.py", content, "'celery/app/autoretry.py' should not be found in bandit.json")



if __name__ == '__main__':
    unittest.main()
