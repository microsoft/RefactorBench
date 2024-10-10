import unittest
import os
import ast

class TestScrapyMigration(unittest.TestCase):

    def test_scrapy_command_class_exists(self):
        # Path to the file where the ScrapyCommand class should be defined
        file_path = '../scrapy/commands/__init__.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Check if the class is defined in __init__.py
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        class_found = False
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef) and node.name == 'ScrapyCommand':
                class_found = True
                break

        self.assertTrue(class_found, "Class 'ScrapyCommand' not found in __init__.py")

    def test_scrapy_command_has_short_description(self):
        # Path to the file where the ScrapyCommand class should be defined
        file_path = '../scrapy/commands/__init__.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Check if the class and function are defined in __init__.py
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        class_node = None
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef) and node.name == 'ScrapyCommand':
                class_node = node
                break

        self.assertIsNotNone(class_node, "Class 'ScrapyCommand' not found in __init__.py")

        # Check if short_description function exists
        function_found = False
        for node in class_node.body:
            if isinstance(node, ast.FunctionDef) and node.name == 'short_description':
                function_found = True
                break

        self.assertTrue(function_found, "Function 'short_description' not found in ScrapyCommand class")

    def test_scrapy_command_has_long_description(self):
        # Path to the file where the ScrapyCommand class should be defined
        file_path = '../scrapy/commands/__init__.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Check if the class and function are defined in __init__.py
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        class_node = None
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef) and node.name == 'ScrapyCommand':
                class_node = node
                break

        self.assertIsNotNone(class_node, "Class 'ScrapyCommand' not found in __init__.py")

        # Check if long_description function exists
        function_found = False
        for node in class_node.body:
            if isinstance(node, ast.FunctionDef) and node.name == 'long_description':
                function_found = True
                break

        self.assertTrue(function_found, "Function 'long_description' not found in ScrapyCommand class")
        
    def check_command_has_short_description(self, file_path):
        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Check if the Command class and short_description function are defined
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        class_node = None
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef) and node.name == 'Command':
                class_node = node
                break

        self.assertIsNotNone(class_node, f"Class 'Command' not found in {file_path}")

        function_found = False
        for node in class_node.body:
            if isinstance(node, ast.FunctionDef) and node.name == 'short_description':
                function_found = True
                break

        self.assertTrue(function_found, f"Function 'short_description' not found in Command class in {file_path}")


    def test_all_command_files(self):
        files_to_check = [
            'bench.py', 'check.py', 'crawl.py', 'edit.py',
            'fetch.py', 'genspider.py', 'list.py', 'parse.py', 'runspider.py',
            'settings.py', 'shell.py', 'startproject.py', 'version.py', 'view.py'
        ]

        base_path = '../scrapy/commands/'

        for file_name in files_to_check:
            with self.subTest(file=file_name):
                file_path = os.path.join(base_path, file_name)
                self.check_command_has_short_description(file_path)
                
    def check_command_has_long_description(self, file_path):
        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Check if the Command class and short_description function are defined
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        class_node = None
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef) and node.name == 'Command':
                class_node = node
                break

        self.assertIsNotNone(class_node, f"Class 'Command' not found in {file_path}")

        function_found = False
        for node in class_node.body:
            if isinstance(node, ast.FunctionDef) and node.name == 'long_description':
                function_found = True
                break

        self.assertTrue(function_found, f"Function 'long_description' not found in Command class in {file_path}")


    def test_all_long_command_files(self):
        files_to_check = [
            'edit.py',
            'fetch.py', 'runspider.py',
            'shell.py',  'view.py'
        ]

        base_path = '../scrapy/commands/'

        for file_name in files_to_check:
            with self.subTest(file=file_name):
                file_path = os.path.join(base_path, file_name)
                self.check_command_has_long_description(file_path)
                
    def test_view_command_test_methods(self):
        # Path to the test file
        file_path = '../tests/test_commands.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Parse the test file
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        class_node = None
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef) and node.name == 'ViewCommandTest':
                class_node = node
                break

        self.assertIsNotNone(class_node, "Class 'ViewCommandTest' not found in test_commands.py")

        method_node = None
        for node in class_node.body:
            if isinstance(node, ast.FunctionDef) and node.name == 'test_methods':
                method_node = node
                break

        self.assertIsNotNone(method_node, "Function 'test_methods' not found in ViewCommandTest class")

        # Check if 'command.short_description' and 'command.long_description' are present
        short_desc_found = False
        long_desc_found = False

        for node in ast.walk(method_node):
            if isinstance(node, ast.Attribute):
                if isinstance(node.value, ast.Name) and node.value.id == 'command':
                    if node.attr == 'short_description':
                        short_desc_found = True
                    if node.attr == 'long_description':
                        long_desc_found = True

        self.assertTrue(short_desc_found, "'command.short_description' not found in test_methods of ViewCommandTest")
        self.assertTrue(long_desc_found, "'command.long_description' not found in test_methods of ViewCommandTest")
        
    def test_cmdline_short_long_description_usage(self):
        # Path to the file to check
        file_path = '../scrapy/cmdline.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Parse the file
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        short_desc_found = False
        long_desc_found = False
        invalid_short_desc_found = False
        invalid_long_desc_found = False

        for node in ast.walk(tree):
            # Check for invalid short_desc() or long_desc()
            if isinstance(node, ast.Call):
                if isinstance(node.func, ast.Name):
                    if node.func.id == 'short_desc':
                        invalid_short_desc_found = True
                    elif node.func.id == 'long_desc':
                        invalid_long_desc_found = True

            # Check for valid cmdclass.short_description() or cmd.long_description()
            if isinstance(node, ast.Attribute):
                if isinstance(node.value, ast.Name) and node.value.id in ['cmdclass', 'cmd']:
                    if node.attr == 'short_description':
                        short_desc_found = True
                    elif node.attr == 'long_description':
                        long_desc_found = True

        # Assert that short_desc() or long_desc() are not found
        self.assertFalse(invalid_short_desc_found, "Found 'short_desc()' in scrapy/cmdline.py which should not be used")
        self.assertFalse(invalid_long_desc_found, "Found 'long_desc()' in scrapy/cmdline.py which should not be used")

        # Assert that cmdclass.short_description() and cmd.long_description() are found
        self.assertTrue(short_desc_found, "cmdclass.short_description() or cmd.short_description() not found in scrapy/cmdline.py")
        self.assertTrue(long_desc_found, "cmd.long_description() or cmdclass.long_description() not found in scrapy/cmdline.py")


if __name__ == '__main__':
    unittest.main()
