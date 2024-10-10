import unittest
import os
import ast

class TestCeleryUtils(unittest.TestCase):

    def test_truncate_text_function_exists(self):
        # Path to the file where the truncate_text function should be defined
        file_path = '../celery/utils/text.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Check if truncate_text function is defined in text.py
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        truncate_text_function = None

        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef) and node.name == 'truncate_text':
                truncate_text_function = node
                break

        self.assertIsNotNone(truncate_text_function, "Function 'truncate_text' not found in text.py")

    def test_truncate_text_in_all(self):
        # Path to the file where the __all__ declaration should be defined
        file_path = '../celery/utils/text.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Check if truncate_text is included in __all__ in text.py
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        all_found = False
        truncate_text_in_all = False

        for node in ast.walk(tree):
            if isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Name) and target.id == '__all__':
                        all_found = True
                        if isinstance(node.value, ast.Tuple):
                            for element in node.value.elts:
                                if isinstance(element, ast.Str) and element.s == 'truncate_text':
                                    truncate_text_in_all = True
                                    break

        self.assertTrue(all_found, "__all__ declaration not found in text.py")
        self.assertTrue(truncate_text_in_all, "'truncate_text' not found in __all__ declaration in text.py")

    def test_import_truncate_text_in_saferepr(self):
        # Path to the file where the import should be checked
        file_path = '../celery/utils/saferepr.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Check if truncate_text is imported from text.py in saferepr.py
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        import_found = False

        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom):
                if node.module == 'text' and any(alias.name == 'truncate_text' for alias in node.names):
                    import_found = True
                    break

        self.assertTrue(import_found, "'truncate_text' not imported from 'text.py' in saferepr.py")

    def test_import_truncate_text_in_concurrency_base(self):
        # Path to the file where the import should be checked
        file_path = '../celery/concurrency/base.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Check if truncate_text is imported from celery.utils.text in base.py
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        import_found = False

        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom):
                if (node.module == 'celery.utils.text' and
                        any(alias.name == 'truncate_text' for alias in node.names)):
                    import_found = True
                    break

        self.assertTrue(import_found, "'truncate_text' not imported from 'celery.utils.text' in base.py")

    def test_import_remove_repeating_from_task_and_truncate_text_in_canvas(self):
        # Path to the file where the import should be checked
        file_path = '../celery/canvas.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Check if remove_repeating_from_task and truncate_text are imported from celery.utils.text in canvas.py
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        import_found = False
        truncate_text_found = False
        remove_repeating_found = False

        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom):
                if node.module == 'celery.utils.text':
                    imported_names = {alias.name for alias in node.names}
                    truncate_text_found = 'truncate_text' in imported_names
                    remove_repeating_found = 'remove_repeating_from_task' in imported_names
                    if truncate_text_found and remove_repeating_found:
                        import_found = True
                        break

        self.assertTrue(import_found, "'truncate_text' and 'remove_repeating_from_task' not imported from 'celery.utils.text' in canvas.py")

    def test_import_truncate_text_in_testing_manager(self):
        # Path to the file where the import should be checked
        file_path = '../celery/contrib/testing/manager.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Check if truncate_text is imported from celery.utils.text in manager.py
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        import_found = False

        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom):
                if node.module == 'celery.utils.text' and any(alias.name == 'truncate_text' for alias in node.names):
                    import_found = True
                    break

        self.assertTrue(import_found, "'truncate_text' not imported from 'celery.utils.text' in manager.py")

    def test_import_abbr_abbrtask_ensure_newlines_indent_pretty_truncate_text_in_test_text(self):
        # Path to the file where the import should be checked
        file_path = '../t/unit/utils/test_text.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Check if the specified functions are imported from celery.utils.text in test_text.py
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        import_found = False
        imported_functions = {
            'abbr', 'abbrtask', 'ensure_newlines',
            'indent', 'pretty', 'truncate_text'
        }

        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom):
                if node.module == 'celery.utils.text':
                    imported_names = {alias.name for alias in node.names}
                    if imported_functions.issubset(imported_names):
                        import_found = True
                        break

        self.assertTrue(import_found, (
            "'abbr', 'abbrtask', 'ensure_newlines', 'indent', "
            "'pretty', and 'truncate_text' not imported from "
            "'celery.utils.text' in test_text.py"
        ))
    
    def test_import_truncate_text_in_consumer(self):
        # Path to the file where the import should be checked
        file_path = '../celery/worker/consumer/consumer.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Check if truncate_text is imported from celery.utils.text in consumer.py
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        import_found = False

        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom):
                if node.module == 'celery.utils.text' and any(alias.name == 'truncate_text' for alias in node.names):
                    import_found = True
                    break

        self.assertTrue(import_found, "'truncate_text' not imported from 'celery.utils.text' in consumer.py")

    def test_saferepr_function_truncate_handling(self):
        # Path to the file where the _saferepr function should be defined
        file_path = '../celery/utils/saferepr.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Parse the saferepr.py file to find the _saferepr function
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        saferepr_function = None

        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef) and node.name == '_saferepr':
                saferepr_function = node
                break

        self.assertIsNotNone(saferepr_function, "Function '_saferepr' not found in saferepr.py")

        # Check the _saferepr function for correct usage of truncate_text and rest2.truncate
        truncate_text_found = False
        rest2_truncate_found = False
        truncate_text_confusion = False

        for node in ast.walk(saferepr_function):
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == 'truncate_text':
                truncate_text_found = True
            if isinstance(node, ast.Attribute) and node.attr == 'truncate':
                rest2_truncate_found = True
                if isinstance(node.value, ast.Name) and node.value.id == 'truncate_text':
                    truncate_text_confusion = True

        self.assertTrue(truncate_text_found, "'truncate_text' not used correctly in _saferepr function")
        self.assertTrue(rest2_truncate_found, "'rest2.truncate' not used in _saferepr function")
        self.assertFalse(truncate_text_confusion, "'truncate_text' confused with 'rest2.truncate' in _saferepr function")

    
if __name__ == '__main__':
    unittest.main()
