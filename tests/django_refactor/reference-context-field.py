import unittest
import ast

class TestReferenceContextIntegration(unittest.TestCase):

    def test_reference_context_class_exists(self):
        # File containing the ReferenceContext class
        file_path = '../django/db/migrations/utils.py'

        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        class_found = any(
            isinstance(node, ast.ClassDef) and node.name == 'ReferenceContext'
            for node in ast.walk(tree)
        )

        self.assertTrue(class_found, "ReferenceContext class not found in the specified file")

    def test_field_references_argument_in_FieldOperation(self):
        # Path to the file where FieldOperation class is defined
        file_path = '../django/db/migrations/operations/fields.py'

        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        # Walk the AST to find instances where field_references is called
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef) and node.name == 'FieldOperation':
                for class_node in ast.walk(node):
                    if isinstance(class_node, ast.FunctionDef):
                        for inner_node in ast.walk(class_node):
                            if isinstance(inner_node, ast.Call):
                                # Check if it's calling field_references
                                if (
                                    (isinstance(inner_node.func, ast.Name) and inner_node.func.id == 'field_references') or
                                    (isinstance(inner_node.func, ast.Attribute) and inner_node.func.attr == 'field_references')
                                ):
                                    # Check the first argument
                                    first_arg = inner_node.args[0]
                                    if not self._is_reference_context_instance(tree, first_arg):
                                        self.fail(f"field_references does not take ReferenceContext instance as an argument in {file_path}")

    def test_field_references_argument_in_CreateModel(self):
        # Path to the file where CreateModel class is defined
        file_path = '../django/db/migrations/operations/models.py'

        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        # Walk the AST to find instances where field_references is called
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef) and node.name == 'CreateModel':
                for class_node in ast.walk(node):
                    if isinstance(class_node, ast.FunctionDef):
                        for inner_node in ast.walk(class_node):
                            if isinstance(inner_node, ast.Call):
                                # Check if it's calling field_references
                                if (
                                    (isinstance(inner_node.func, ast.Name) and inner_node.func.id == 'field_references') or
                                    (isinstance(inner_node.func, ast.Attribute) and inner_node.func.attr == 'field_references')
                                ):
                                    # Check the first argument
                                    first_arg = inner_node.args[0]
                                    if not self._is_reference_context_instance(tree, first_arg):
                                        self.fail(f"field_references does not take ReferenceContext instance as an argument in {file_path}")

    def _is_reference_context_instance(self, tree, node):
        """ Check if a node is or resolves to a ReferenceContext instance """
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == 'ReferenceContext':
            return True
        elif isinstance(node, ast.Name):
            # Look for the assignment or initialization of this variable
            for assign_node in ast.walk(tree):
                if isinstance(assign_node, ast.Assign):
                    for target in assign_node.targets:
                        if isinstance(target, ast.Name) and target.id == node.id:
                            return self._is_reference_context_instance(tree, assign_node.value)
        return False

    def test_reference_context_import_in_files(self):
        files_to_check = [
            '../django/db/migrations/operations/fields.py',
            '../django/db/migrations/operations/models.py',
        ]

        for file_path in files_to_check:
            with open(file_path, 'r') as file:
                tree = ast.parse(file.read())

            import_found = self._is_reference_context_imported(tree)

            self.assertTrue(import_found, f"ReferenceContext not imported in {file_path}")

    def _is_reference_context_imported(self, tree):
        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom):
                if any(alias.name == 'ReferenceContext' for alias in node.names):
                    return True
            elif isinstance(node, ast.Import):
                if any(alias.name == 'ReferenceContext' for alias in node.names):
                    return True
        return False

if __name__ == '__main__':
    unittest.main()
