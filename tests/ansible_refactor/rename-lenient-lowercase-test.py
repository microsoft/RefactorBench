import unittest
import os
import ast

class TestAnsibleFunctionRename(unittest.TestCase):

    def test_lenient_lowercase_renamed_to_lowercase_of_list(self):
        # Path to the file where lenient_lowercase should be renamed to lowercase_of_list
        file_path = '../lib/ansible/module_utils/common/text/formatters.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Check if lenient_lowercase is renamed to lowercase_of_list
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        lenient_lowercase_function = None
        lowercase_of_list_function = None

        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                if node.name == 'lenient_lowercase':
                    lenient_lowercase_function = node
                elif node.name == 'lowercase_of_list':
                    lowercase_of_list_function = node

        self.assertIsNone(lenient_lowercase_function, "Function 'lenient_lowercase' should have been renamed")
        self.assertIsNotNone(lowercase_of_list_function, "Function 'lowercase_of_list' not found in formatters.py")

    def test_lowercase_of_list_imported_in_basic(self):
        # Path to the file where lowercase_of_list should be imported
        file_path = '../lib/ansible/module_utils/basic.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Check if lowercase_of_list is imported
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        lowercase_of_list_imported = False

        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom):
                if node.module == 'ansible.module_utils.common.text.formatters':
                    for name in node.names:
                        if name.name == 'lowercase_of_list':
                            lowercase_of_list_imported = True

        self.assertTrue(lowercase_of_list_imported, "Function 'lowercase_of_list' not imported in basic.py")
        
    def test_test_file_renamed(self):
        # Paths to the old and new test files
        old_test_file = '../test/units/module_utils/common/text/formatters/test_lenient_lowercase.py'
        new_test_file = '../test/units/module_utils/common/text/formatters/test_lowercase_of_list.py'

        # Check that the old test file does not exist
        self.assertFalse(os.path.exists(old_test_file), f"{old_test_file} should not exist")

        # Check that the new test file exists
        self.assertTrue(os.path.exists(new_test_file), f"{new_test_file} does not exist")
        
    def test_test_file_content_updated(self):
        # Path to the new test file
        test_file = '../test/units/module_utils/common/text/formatters/test_lowercase_of_list.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(test_file), f"{test_file} does not exist")

        # Open and read the file
        with open(test_file, 'r', encoding='utf-8') as file:
            source_code = file.read()

        # Check that 'lenient_lowercase' is not in the file
        self.assertNotIn('lenient_lowercase', source_code, "Found reference to 'lenient_lowercase' in the test file")

        # Check that 'lowercase_of_list' is in the file
        self.assertIn('lowercase_of_list', source_code, "'lowercase_of_list' not found in the test file")

        # Check that comments have been updated
        self.assertNotIn('Test that lenient_lowercase()', source_code, "Old comment referring to 'lenient_lowercase' found")
        self.assertIn('Test that lowercase_of_list()', source_code, "Comment referring to 'lowercase_of_list' not found")




if __name__ == '__main__':
    unittest.main()
