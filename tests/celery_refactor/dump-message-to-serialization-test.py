import unittest
import os
import ast

class TestCeleryDumpMessage(unittest.TestCase):

    def test_amqp_does_not_contain_dump_message(self):
        # Path to the file where dump_message should not be defined
        file_path = '../celery/bin/amqp.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Parse the amqp.py file to check for the dump_message function definition
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        dump_message_function = None

        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef) and node.name == 'dump_message':
                dump_message_function = node
                break

        self.assertIsNone(dump_message_function, "Function 'dump_message' should not be found in amqp.py")

    def test_serialization_contains_dump_message(self):
        # Path to the file where dump_message should be defined
        file_path = '../celery/utils/serialization.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Parse the serialization.py file to check for the dump_message function definition
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        dump_message_function = None

        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef) and node.name == 'dump_message':
                dump_message_function = node
                break

        self.assertIsNotNone(dump_message_function, "Function 'dump_message' not found in serialization.py")

    def test_amqp_imports_dump_message(self):
        # Path to the file where the import should be checked
        file_path = '../celery/bin/amqp.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Parse the amqp.py file to check for the specific import
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        import_found = False

        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom):
                if node.module == 'celery.utils.serialization':
                    imported_names = {alias.name for alias in node.names}
                    if 'dump_message' in imported_names:
                        import_found = True
                        break

        self.assertTrue(import_found, "'dump_message' not imported from 'celery.utils.serialization' in amqp.py")


if __name__ == '__main__':
    unittest.main()
