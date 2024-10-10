import unittest
import ast

class TestTimeZoneFunctionsInClass(unittest.TestCase):

    def test_functions_in_any_class(self):
        # Path to the file containing the classes with the timezone functions
        file_path = '../django/forms/utils.py'

        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        functions_found_in_class = {
            'from_current_timezone': False,
            'to_current_timezone': False
        }

        # Walk through the AST tree to find any class and check its methods
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef):  # Look for class definitions
                for class_node in node.body:
                    if isinstance(class_node, ast.FunctionDef):
                        if class_node.name in functions_found_in_class:
                            functions_found_in_class[class_node.name] = True

        self.assertTrue(functions_found_in_class['from_current_timezone'], 
                        "'from_current_timezone' method not found within any class")
        self.assertTrue(functions_found_in_class['to_current_timezone'], 
                        "'to_current_timezone' method not found within any class")

    def test_class_imported_in_other_files(self):
        # Path to the file containing the classes with the timezone functions
        class_file = '../django/forms/utils.py'
        class_names = []

        with open(class_file, 'r') as file:
            tree = ast.parse(file.read())
        
        # Collect all class names
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef):
                class_names.append(node.name)
        
        self.assertTrue(class_names, "No classes found in the utils.py file.")

        # List of files to check for the import
        files_to_check = [
            '../django/forms/fields.py',
            '../django/forms/widgets.py',
            # Add more file paths as needed
        ]

        for file_path in files_to_check:
            with open(file_path, 'r') as file:
                tree = ast.parse(file.read())

            class_imported = any(
                self._is_class_imported_in_file(tree, class_name)
                for class_name in class_names
            )

            self.assertTrue(class_imported, f"None of the classes '{', '.join(class_names)}' imported in {file_path}")

    def test_from_current_timezone_called_using_class(self):
        # Path to the file containing the classes with the timezone functions
        class_file = '../django/forms/utils.py'
        class_names = []

        with open(class_file, 'r') as file:
            tree = ast.parse(file.read())
        
        # Collect all class names
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef):
                class_names.append(node.name)

        self.assertTrue(class_names, "No classes found in the utils.py file.")

        # List of files to check for the function calls
        files_to_check = [
            '../django/forms/fields.py',
            # Add more file paths as needed
        ]

        for file_path in files_to_check:
            with open(file_path, 'r') as file:
                tree = ast.parse(file.read())

            function_called = False

            # Check for function calls using the class name
            for node in ast.walk(tree):
                if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute):
                    if node.func.attr == 'from_current_timezone':
                        if isinstance(node.func.value, ast.Name) and node.func.value.id in class_names:
                            function_called = True
                            break

            self.assertTrue(function_called, f"Function 'from_current_timezone' not called using any of the classes '{', '.join(class_names)}' in {file_path}")

    def test_to_current_timezone_called_using_class(self):
        # Path to the file containing the classes with the timezone functions
        class_file = '../django/forms/utils.py'
        class_names = []

        with open(class_file, 'r') as file:
            tree = ast.parse(file.read())
        
        # Collect all class names
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef):
                class_names.append(node.name)

        self.assertTrue(class_names, "No classes found in the utils.py file.")

        # List of files to check for the function calls
        files_to_check = [
            '../django/forms/widgets.py',
            '../django/forms/fields.py',
            # Add more file paths as needed
        ]

        for file_path in files_to_check:
            with open(file_path, 'r') as file:
                tree = ast.parse(file.read())

            function_called = False

            # Check for function calls using the class name
            for node in ast.walk(tree):
                if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute):
                    if node.func.attr == 'to_current_timezone':
                        if isinstance(node.func.value, ast.Name) and node.func.value.id in class_names:
                            function_called = True
                            break

            self.assertTrue(function_called, f"Function 'to_current_timezone' not called using any of the classes '{', '.join(class_names)}' in {file_path}")

    def _is_class_imported_in_file(self, tree, class_name):
        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom):
                for alias in node.names:
                    if alias.name == class_name:
                        return True
            elif isinstance(node, ast.Import):
                for alias in node.names:
                    if alias.name.split('.')[-1] == class_name:
                        return True
        return False

if __name__ == '__main__':
    unittest.main()
