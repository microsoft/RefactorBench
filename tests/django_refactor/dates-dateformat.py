import unittest
import ast
import os

class TestDatesMigration(unittest.TestCase):

    def setUp(self):
        # Paths to the old and new files
        self.dates_file_path = '../django/utils/dates.py' 
        self.dateformat_file_path = '../django/utils/dateformat.py'  
        self.widgets_file_path = '../django/forms/widgets.py' 
        self.widget_tests_file_path = '../tests/forms_tests/widget_tests/test_selectdatewidget.py' 

    def test_dates_file_deleted(self):
        # Check if dates.py file has been deleted
        self.assertFalse(os.path.exists(self.dates_file_path), "dates.py should be deleted")

    def test_dates_content_in_dateformat(self):
        with open(self.dateformat_file_path, 'r') as file:
            dateformat_tree = ast.parse(file.read())

        # Check that all necessary constants from dates.py are in dateformat.py
        necessary_constants = [
            'WEEKDAYS', 'WEEKDAYS_ABBR', 'MONTHS', 'MONTHS_3', 'MONTHS_AP', 'MONTHS_ALT'
        ]

        dateformat_names = {
            node.targets[0].id
            for node in ast.walk(dateformat_tree)
            if isinstance(node, ast.Assign) and isinstance(node.targets[0], ast.Name)
        }

        for const in necessary_constants:
            self.assertIn(const, dateformat_names, f"{const} not found in dateformat.py")

    def test_import_in_widgets(self):
        with open(self.widgets_file_path, 'r') as file:
            tree = ast.parse(file.read())

        imported_names = {
            alias.name for node in ast.walk(tree)
            if isinstance(node, ast.ImportFrom) and node.module == 'django.utils.dateformat'
            for alias in node.names
        }

        necessary_imports = [
            'MONTHS'
        ]

        for name in necessary_imports:
            self.assertIn(name, imported_names, f"{name} not imported from dateformat in widgets.py")

        # Ensure 'dates' is not imported
        dates_import_found = any(
            isinstance(node, ast.ImportFrom) and node.module == 'django.utils.dates'
            for node in ast.walk(tree)
        )
        self.assertFalse(dates_import_found, "dates should not be imported in widgets.py")

    def test_import_in_widget_tests(self):
        with open(self.widget_tests_file_path, 'r') as file:
            tree = ast.parse(file.read())

        imported_names = {
            alias.name for node in ast.walk(tree)
            if isinstance(node, ast.ImportFrom) and node.module == 'django.utils.dateformat'
            for alias in node.names
        }

        necessary_imports = [
            'MONTHS_AP'
        ]

        for name in necessary_imports:
            self.assertIn(name, imported_names, f"{name} not imported from dateformat in test_selectdatewidget.py")

        # Ensure 'dates' is not imported
        dates_import_found = any(
            isinstance(node, ast.ImportFrom) and node.module == 'django.utils.dates'
            for node in ast.walk(tree)
        )
        self.assertFalse(dates_import_found, "dates should not be imported in test_selectdatewidget.py")

if __name__ == '__main__':
    unittest.main()
