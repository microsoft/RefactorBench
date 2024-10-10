import unittest
import os
import ast

class TestFastAPIGetUtils(unittest.TestCase):

    def test_get_utils_file_exists(self):
        # Path to the file where the get_utils.py should be defined
        file_path = '../fastapi/openapi/get_utils.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

    def test_utils_file_does_not_exist(self):
        # Path to the file where the old utils.py should no longer be present
        file_path = '../fastapi/openapi/utils.py'

        # Check if the file does not exist
        self.assertFalse(os.path.exists(file_path), f"{file_path} should not exist")

    def test_generate_operation_id_warning(self):
        # Path to the file where the generate_operation_id function is defined
        file_path = '../fastapi/openapi/get_utils.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Parse the get_utils.py file to check for the generate_operation_id function and its warning
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        generate_operation_id_function = None
        warning_found = False

        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef) and node.name == 'generate_operation_id':
                generate_operation_id_function = node
                for body_node in node.body:
                    if isinstance(body_node, ast.Expr) and isinstance(body_node.value, ast.Call):
                        if (isinstance(body_node.value.func, ast.Attribute) and 
                            body_node.value.func.attr == 'warn' and
                            isinstance(body_node.value.args[0], ast.Str) and
                            "fastapi.openapi.get_utils.generate_operation_id() was deprecated, "
                            "it is not used internally, and will be removed soon" in body_node.value.args[0].s):
                            warning_found = True
                            break
                break

        self.assertIsNotNone(generate_operation_id_function, "Function 'generate_operation_id' not found in get_utils.py")
        self.assertTrue(warning_found, "The expected deprecation warning message is not found in the 'generate_operation_id' function")

    
    def test_extending_openapi_md_de_docs(self):
        file_path = '../docs/de/docs/how-to/extending-openapi.md'
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        with open(file_path, 'r') as file:
            content = file.read()
        
        self.assertNotIn('openapi.utils', content, f"'openapi.utils' found in {file_path}")
        self.assertIn('openapi.get_utils', content, f"'openapi.get_utils' not found in {file_path}")

    def test_extending_openapi_md_em_docs(self):
        file_path = '../docs/em/docs/how-to/extending-openapi.md'
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        with open(file_path, 'r') as file:
            content = file.read()

        self.assertNotIn('openapi.utils', content, f"'openapi.utils' found in {file_path}")
        self.assertIn('openapi.get_utils', content, f"'openapi.get_utils' not found in {file_path}")

    def test_extending_openapi_md_en_docs(self):
        file_path = '../docs/en/docs/how-to/extending-openapi.md'
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        with open(file_path, 'r') as file:
            content = file.read()

        self.assertNotIn('openapi.utils', content, f"'openapi.utils' found in {file_path}")
        self.assertIn('openapi.get_utils', content, f"'openapi.get_utils' not found in {file_path}")

    def test_tutorial001_py(self):
        file_path = '../docs_src/extending_openapi/tutorial001.py'
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        with open(file_path, 'r') as file:
            content = file.read()

        self.assertNotIn('openapi.utils', content, f"'openapi.utils' found in {file_path}")
        self.assertIn('openapi.get_utils', content, f"'openapi.get_utils' not found in {file_path}")

    def test_applications_py(self):
        file_path = '../fastapi/applications.py'
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        with open(file_path, 'r') as file:
            content = file.read()

        self.assertNotIn('openapi.utils', content, f"'openapi.utils' found in {file_path}")
        self.assertIn('openapi.get_utils', content, f"'openapi.get_utils' not found in {file_path}")

    def test_test_additional_responses_bad_py(self):
        file_path = '../tests/test_additional_responses_bad.py'
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        with open(file_path, 'r') as file:
            content = file.read()

        self.assertNotIn('openapi.utils', content, f"'openapi.utils' found in {file_path}")
        self.assertIn('openapi.get_utils', content, f"'openapi.get_utils' not found in {file_path}")


if __name__ == '__main__':
    unittest.main()
