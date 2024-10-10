import unittest
import os
import ast

class TestCeleryAnnotationsUtils(unittest.TestCase):

    def test_annotations_utils_file_exists(self):
        # Path to the file where the resolve_all function should be defined
        file_path = '../celery/app/annotations_utils.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

    def test_resolve_all_function_exists(self):
        # Path to the file where the resolve_all function should be defined
        file_path = '../celery/app/annotations_utils.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Check if resolve_all function is defined in annotations_utils.py
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        resolve_all_function = None

        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef) and node.name == 'resolve_all':
                resolve_all_function = node
                break

        self.assertIsNotNone(resolve_all_function, "Function 'resolve_all' not found in annotations_utils.py")

    def test_resolve_all_in_all_declaration(self):
        # Path to the file where the __all__ declaration should be checked
        file_path = '../celery/app/annotations_utils.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Check if resolve_all is included in __all__ in annotations_utils.py
        with open(file_path, 'r') as file:
            content = file.read()

        # Look for the exact __all__ declaration
        expected_all_declaration = "__all__ = ('resolve_all')"
        self.assertIn(expected_all_declaration, content, f"{expected_all_declaration} not found in annotations_utils.py")

    def test_import_first_match_and_first_match_any(self):
        # Path to the file where the import should be checked
        file_path = '../celery/app/annotations_utils.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Parse the annotations_utils.py file to check for the specific import
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        import_found = False

        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom):
                if node.module == 'celery.app.annotations':
                    imported_names = {alias.name for alias in node.names}
                    if {'_first_match', '_first_match_any'}.issubset(imported_names):
                        import_found = True
                        break

        self.assertTrue(import_found, "'_first_match' and '_first_match_any' not imported from 'celery.app.annotations' in annotations_utils.py")

    def test_annotations_all_declaration(self):
        # Path to the file where the __all__ declaration should be checked
        file_path = '../celery/app/annotations.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Check if __all__ includes 'MapAnnotation' and 'prepare' in annotations.py
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        all_found = False
        mapannotation_in_all = False
        prepare_in_all = False

        for node in ast.walk(tree):
            if isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Name) and target.id == '__all__':
                        all_found = True
                        if isinstance(node.value, ast.Tuple) or isinstance(node.value, ast.List):
                            elements = {element.s for element in node.value.elts if isinstance(element, ast.Str)}
                            mapannotation_in_all = 'MapAnnotation' in elements
                            prepare_in_all = 'prepare' in elements
                            break

        self.assertTrue(all_found, "__all__ declaration not found in annotations.py")
        self.assertTrue(mapannotation_in_all, "'MapAnnotation' not found in __all__ declaration in annotations.py")
        self.assertTrue(prepare_in_all, "'prepare' not found in __all__ declaration in annotations.py")

    def test_mapannotation_class_exists(self):
        # Path to the file where the MapAnnotation class should be defined
        file_path = '../celery/app/annotations.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Parse the annotations.py file to check for the MapAnnotation class
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        mapannotation_class = None

        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef) and node.name == 'MapAnnotation':
                mapannotation_class = node
                break

        self.assertIsNotNone(mapannotation_class, "Class 'MapAnnotation' not found in annotations.py")

    def test_prepare_function_exists(self):
        # Path to the file where the prepare function should be defined
        file_path = '../celery/app/annotations.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Parse the annotations.py file to check for the prepare function
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        prepare_function = None

        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef) and node.name == 'prepare':
                prepare_function = node
                break

        self.assertIsNotNone(prepare_function, "Function 'prepare' not found in annotations.py")

    def test_first_match_and_first_match_any_assignments(self):
        # Path to the file where the assignments should be checked
        file_path = '../celery/app/annotations.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Parse the annotations.py file to check for _first_match and _first_match_any assignments
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        first_match_assignment = None
        first_match_any_assignment = None

        for node in ast.walk(tree):
            if isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Name):
                        if target.id == '_first_match' and isinstance(node.value, ast.Call):
                            if isinstance(node.value.func, ast.Name) and node.value.func.id == 'firstmethod':
                                if (len(node.value.args) == 1 and 
                                    isinstance(node.value.args[0], ast.Str) and 
                                    node.value.args[0].s == 'annotate'):
                                    first_match_assignment = node
                        elif target.id == '_first_match_any' and isinstance(node.value, ast.Call):
                            if isinstance(node.value.func, ast.Name) and node.value.func.id == 'firstmethod':
                                if (len(node.value.args) == 1 and 
                                    isinstance(node.value.args[0], ast.Str) and 
                                    node.value.args[0].s == 'annotate_any'):
                                    first_match_any_assignment = node

        self.assertIsNotNone(first_match_assignment, "'_first_match = firstmethod('annotate')' not found in annotations.py")
        self.assertIsNotNone(first_match_any_assignment, "'_first_match_any = firstmethod('annotate_any')' not found in annotations.py")


if __name__ == '__main__':
    unittest.main()
