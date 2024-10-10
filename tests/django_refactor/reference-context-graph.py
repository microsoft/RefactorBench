import unittest
import ast

class TestReferenceContextInAddDependency(unittest.TestCase):

    def test_reference_context_import_in_loader(self):
        file_path = '../django/db/migrations/loader.py'
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        import_found = False
        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom) or isinstance(node, ast.Import):
                if any(alias.name == 'ReferenceContext' for alias in node.names):
                    import_found = True
                    break

        self.assertTrue(import_found, f"ReferenceContext not imported in {file_path}")

    def test_reference_context_import_in_executor(self):
        file_path = '../tests/migrations/test_executor.py'
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        import_found = False
        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom) or isinstance(node, ast.Import):
                if any(alias.name == 'ReferenceContext' for alias in node.names):
                    import_found = True
                    break

        self.assertTrue(import_found, f"ReferenceContext not imported in {file_path}")
    
    def test_reference_context_import_in_graph(self):
        file_path = '../tests/migrations/test_graph.py'
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        import_found = False
        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom) or isinstance(node, ast.Import):
                if any(alias.name == 'ReferenceContext' for alias in node.names):
                    import_found = True
                    break

        self.assertTrue(import_found, f"ReferenceContext not imported in {file_path}")

    def test_reference_context_import_in_autodetector(self):
        file_path = '../tests/migrations/test_autodetector.py'
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        import_found = False
        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom) or isinstance(node, ast.Import):
                if any(alias.name == 'ReferenceContext' for alias in node.names):
                    import_found = True
                    break

        self.assertTrue(import_found, f"ReferenceContext not imported in {file_path}")
    
    def test_reference_context_import_not_in_deletion(self):
        file_path = '../django/db/models/deletion.py'
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        import_found = False
        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom) or isinstance(node, ast.Import):
                if any(alias.name == 'ReferenceContext' for alias in node.names):
                    import_found = True
                    break

        self.assertFalse(import_found, f"ReferenceContext should not be imported in {file_path}")

    def test_add_dependency_uses_reference_context_in_loader(self):
        file_path = '../django/db/migrations/loader.py'
        self._check_reference_context_usage(file_path)

    def test_add_dependency_uses_reference_context_in_executor(self):
        file_path = '../tests/migrations/test_executor.py'
        self._check_reference_context_usage(file_path)

    def test_add_dependency_uses_reference_context_in_graph(self):
        file_path = '../tests/migrations/test_graph.py'
        self._check_reference_context_usage(file_path)

    def test_add_dependency_uses_reference_context_in_autodetector(self):
        file_path = '../tests/migrations/test_autodetector.py'
        self._check_reference_context_usage(file_path)

    def _check_reference_context_usage(self, file_path):
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        class_found = False
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef):
                class_found = True
                for method in node.body:
                    if isinstance(method, ast.FunctionDef) and method.name == 'add_dependency':
                        self._check_reference_context_in_function(method, file_path, node.name)

        if not class_found:
            self.fail(f"No classes found in {file_path}")

    def _check_reference_context_in_function(self, function_node, file_path, class_name):
        reference_context_found = False
        for inner_node in ast.walk(function_node):
            if isinstance(inner_node, ast.Call):
                if isinstance(inner_node.func, ast.Name) and inner_node.func.id == 'ReferenceContext':
                    reference_context_found = True
                elif isinstance(inner_node.func, ast.Attribute) and inner_node.func.attr == 'ReferenceContext':
                    reference_context_found = True

        self.assertTrue(reference_context_found, f"ReferenceContext not used in add_dependency method in class {class_name} in {file_path}")

if __name__ == '__main__':
    unittest.main()
