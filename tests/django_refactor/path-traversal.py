import unittest
import ast

class TestPathTraversalException(unittest.TestCase):

    def test_pathtraversal_exception_exists(self):
        # Path to the file where PathTraversal is defined
        file_path = '../django/core/exceptions.py'

        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        # Check if the PathTraversal class is defined
        class_exists = any(
            isinstance(node, ast.ClassDef) and node.name == 'PathTraversal'
            for node in ast.walk(tree)
        )
        self.assertTrue(class_exists, "PathTraversal exception class is not defined")

    def test_pathtraversal_extends_suspiciousoperation(self):
        # Path to the file where PathTraversal is defined
        file_path = '../django/core/exceptions.py'

        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef) and node.name == 'PathTraversal':
                # Check if PathTraversal extends SuspiciousOperation
                bases = [base.id for base in node.bases if isinstance(base, ast.Name)]
                self.assertIn('SuspiciousOperation', bases, "PathTraversal does not extend SuspiciousOperation")
                return  # We found and checked the class, so we can stop here

        self.fail("PathTraversal class not found in the file")

    def test_get_available_name_raises_pathtraversal(self):
        # Path to the file containing the Storage class
        file_path = '../django/core/files/storage/base.py'

        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef) and node.name == 'Storage':
                for subnode in node.body:
                    if isinstance(subnode, ast.FunctionDef) and subnode.name == 'get_available_name':
                        # Check within all If statements for a raise statement with PathTraversal
                        raise_check = any(
                            isinstance(stmt, ast.If) and
                            any(
                                isinstance(substmt, ast.Raise) and
                                isinstance(substmt.exc, ast.Call) and
                                isinstance(substmt.exc.func, ast.Name) and
                                substmt.exc.func.id == 'PathTraversal'
                                for substmt in stmt.body
                            )
                            for stmt in subnode.body
                        )
                        self.assertTrue(raise_check, "PathTraversal exception is not raised in get_available_name")
                        return  # We found and checked the function, so we can stop here

        self.fail("get_available_name function not found in the Storage class")

    def test_generate_filename_raises_pathtraversal(self):
        # Path to the file containing the Storage class
        file_path = '../django/core/files/storage/base.py'

        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef) and node.name == 'Storage':
                for subnode in node.body:
                    if isinstance(subnode, ast.FunctionDef) and subnode.name == 'generate_filename':
                        # Check within all If statements for a raise statement with PathTraversal
                        raise_check = any(
                            isinstance(stmt, ast.If) and
                            any(
                                isinstance(substmt, ast.Raise) and
                                isinstance(substmt.exc, ast.Call) and
                                isinstance(substmt.exc.func, ast.Name) and
                                substmt.exc.func.id == 'PathTraversal'
                                for substmt in stmt.body
                            )
                            for stmt in subnode.body
                        )
                        self.assertTrue(raise_check, "PathTraversal exception is not raised in generate_filename")
                        return  # We found and checked the function, so we can stop here

        self.fail("generate_filename function not found in the Storage class")


    def test_usages_of_get_available_name_raise_exceptions(self):
        # List of files to check for usages of get_available_name
        files_to_check = [
            '../tests/file_storage/test_generate_filename.py',
            # Add more file paths as needed
        ]

        for file_path in files_to_check:
            with open(file_path, 'r') as f:
                tree = ast.parse(f.read())

            for node in ast.walk(tree):
                if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == 'get_available_name':
                    # Ensure that the usage is within a try-except block that catches either PathTraversal or SuspiciousFileOperation
                    try_except_check_pathtraversal = any(
                        isinstance(parent, ast.Try) and 
                        any(isinstance(handler.type, ast.Name) and handler.type.id == 'PathTraversal' for handler in parent.handlers)
                        for parent in ast.iter_parent_nodes(tree, node)
                    )

                    try_except_check_suspiciousfile = any(
                        isinstance(parent, ast.Try) and 
                        any(isinstance(handler.type, ast.Name) and handler.type.id == 'SuspiciousFileOperation' for handler in parent.handlers)
                        for parent in ast.iter_parent_nodes(tree, node)
                    )

                    self.assertTrue(
                        try_except_check_pathtraversal or try_except_check_suspiciousfile, 
                        f"Neither PathTraversal nor SuspiciousFileOperation is caught in usage of get_available_name in {file_path}"
                    )

    def test_usages_of_generate_filename_raise_pathtraversal(self):
        # List of files to check for usages of generate_filename
        files_to_check = [
            '../tests/file_storage/test_generate_filename.py',
            # Add more file paths as needed
        ]

        for file_path in files_to_check:
            with open(file_path, 'r') as f:
                tree = ast.parse(f.read())

            for node in ast.walk(tree):
                if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == 'generate_filename':
                    # Ensure that the usage is within a try-except block that catches PathTraversal
                    try_except_check = any(
                        isinstance(parent, ast.Try) and 
                        any(isinstance(handler.type, ast.Name) and handler.type.id == 'PathTraversal' for handler in parent.handlers)
                        for parent in ast.iter_parent_nodes(tree, node)
                    )
                    self.assertTrue(try_except_check, f"PathTraversal is not caught in usage of generate_filename in {file_path}")

    def test_safe_join_calls_pathtraversal(self):
        # Path to the file containing safe_join
        file_path = '../django/utils/_os.py'

        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef) and node.name == 'safe_join':
                # Check within all If statements for a raise statement with PathTraversal
                raise_check = any(
                    isinstance(stmt, ast.If) and
                    any(
                        isinstance(substmt, ast.Raise) and
                        isinstance(substmt.exc, ast.Call) and
                        isinstance(substmt.exc.func, ast.Name) and
                        substmt.exc.func.id == 'PathTraversal'
                        for substmt in stmt.body
                    )
                    for stmt in node.body
                )
                self.assertTrue(raise_check, "PathTraversal exception is not raised in safe_join")
                return  # We found and checked the function, so we can stop here

        self.fail("safe_join function not found in the file")


    def test_pathtraversal_in_exceptions_docs(self):
        # Path to the docs file where exceptions are listed
        file_path = '../docs/ref/exceptions.txt'

        with open(file_path, 'r') as file:
            content = file.read()

        # Check if 'PathTraversal' is mentioned in the file
        self.assertIn('PathTraversal', content, "PathTraversal is not mentioned in docs/ref/exceptions.txt")

    def test_os_utils_tests_imports_and_uses_pathtraversal(self):
        # Path to the tests/utils_tests/test_os_utils.py file
        file_path = '../tests/utils_tests/test_os_utils.py'

        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        # Check if PathTraversal is imported
        import_exists = any(
            isinstance(node, ast.ImportFrom) and 
            any(alias.name == 'PathTraversal' for alias in node.names)
            for node in ast.walk(tree)
        )
        self.assertTrue(import_exists, "PathTraversal is not imported in /tests/utils_tests/test_os_utils.py")

        pathtraversal_assert_raises = False

        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef) and node.name == 'SafeJoinTests':
                for subnode in node.body:
                    if isinstance(subnode, ast.FunctionDef):
                        # Look for self.assertRaises(PathTraversal)
                        for stmt in ast.walk(subnode):
                            if isinstance(stmt, ast.Call) and \
                               isinstance(stmt.func, ast.Attribute) and \
                               stmt.func.attr == 'assertRaises' and \
                               isinstance(stmt.args[0], ast.Name) and \
                               stmt.args[0].id == 'PathTraversal':
                                pathtraversal_assert_raises = True
                                break

        self.assertTrue(pathtraversal_assert_raises, "self.assertRaises(PathTraversal) is not found in SafeJoinTests in /tests/utils_tests/test_os_utils.py")


if __name__ == '__main__':
    unittest.main()
