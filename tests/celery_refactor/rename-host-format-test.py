import unittest
import os
import ast

class TestCeleryUtilsNodenames(unittest.TestCase):

    def test_nodenames_file_exists(self):
        # Path to the file where the format_host function should be defined
        file_path = '../celery/utils/nodenames.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

    def test_format_host_function_exists(self):
        # Path to the file where the format_host function should be defined
        file_path = '../celery/utils/nodenames.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Check if format_host function is defined in nodenames.py
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        format_host_function = None

        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef) and node.name == 'format_host':
                format_host_function = node
                break

        self.assertIsNotNone(format_host_function, "Function 'format_host' not found in nodenames.py")

    def test_format_host_in_all_declaration(self):
        # Path to the file where the __all__ declaration should be checked
        file_path = '../celery/utils/nodenames.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Check if format_host is included in __all__ in nodenames.py
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        all_declaration = None

        for node in ast.walk(tree):
            if isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Name) and target.id == '__all__':
                        all_declaration = node.value
                        break

        self.assertIsNotNone(all_declaration, "__all__ declaration not found in nodenames.py")
        
        if isinstance(all_declaration, ast.List) or isinstance(all_declaration, ast.Tuple):
            elements = {element.s for element in all_declaration.elts if isinstance(element, ast.Str)}
            self.assertIn('format_host', elements, "'format_host' not found in __all__ declaration in nodenames.py")
        else:
            self.fail("__all__ is not a list or tuple in nodenames.py")
    
    def test_worker_imports_nodenames_functions(self):
        # Path to the file where the import should be checked
        file_path = '../celery/bin/worker.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Parse the worker.py file to check for the specific import
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        import_found = False

        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom):
                if node.module == 'celery.utils.nodenames':
                    imported_names = {alias.name for alias in node.names}
                    if {'default_nodename', 'format_host', 'node_format'}.issubset(imported_names):
                        import_found = True
                        break

        self.assertTrue(import_found, "'default_nodename', 'format_host', and 'node_format' not imported from 'celery.utils.nodenames' in worker.py")

    def test_format_host_not_called_in_worker(self):
        # Path to the file where the function call should be checked
        file_path = '../celery/bin/worker.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Parse the worker.py file to check if format_host is called
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        format_host_called = False

        for node in ast.walk(tree):
            if isinstance(node, ast.Call):
                if isinstance(node.func, ast.Name) and node.func.id == 'host_format':
                    format_host_called = True
                    break
                elif isinstance(node.func, ast.Attribute) and node.func.attr == 'host_format':
                    format_host_called = True
                    break

        self.assertFalse(format_host_called, "'host_format' should not be called in worker.py")
        
    def test_multi_imports_nodenames_functions(self):
        # Path to the file where the import should be checked
        file_path = '../celery/apps/multi.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Parse the multi.py file to check for the specific import
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        import_found = False

        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom):
                if node.module == 'celery.utils.nodenames':
                    imported_names = {alias.name for alias in node.names}
                    if {'gethostname', 'format_host', 'node_format', 'nodesplit'}.issubset(imported_names):
                        import_found = True
                        break

        self.assertTrue(import_found, "'gethostname', 'format_host', 'node_format', and 'nodesplit' not imported from 'celery.utils.nodenames' in multi.py")

    def test_format_host_not_called_in_multi(self):
        # Path to the file where the function call should be checked
        file_path = '../celery/apps/multi.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Parse the worker.py file to check if format_host is called
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        format_host_called = False

        for node in ast.walk(tree):
            if isinstance(node, ast.Call):
                if isinstance(node.func, ast.Name) and node.func.id == 'host_format':
                    format_host_called = True
                    break
                elif isinstance(node.func, ast.Attribute) and node.func.attr == 'host_format':
                    format_host_called = True
                    break

        self.assertFalse(format_host_called, "'host_format' should not be called in worker.py")
    
if __name__ == '__main__':
    unittest.main()
