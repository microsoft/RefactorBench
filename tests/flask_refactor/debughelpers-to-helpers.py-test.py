import unittest
import os
import ast

class TestHelpersFunctions(unittest.TestCase):

    def test_attach_enctype_error_multidict_exists(self):
        # Path to the file where the function should be located
        file_path = '../src/flask/helpers.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Check if the function is defined in helpers.py
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        function_found = False
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef) and node.name == 'attach_enctype_error_multidict':
                function_found = True
                break

        self.assertTrue(function_found, "Function 'attach_enctype_error_multidict' not found in helpers.py")

    def test_dump_loader_info_exists(self):
        # Path to the file where the function should be located
        file_path = '../src/flask/helpers.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Check if the function is defined in helpers.py
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        function_found = False
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef) and node.name == '_dump_loader_info':
                function_found = True
                break

        self.assertTrue(function_found, "Function '_dump_loader_info' not found in helpers.py")

    def test_explain_template_loading_attempts_exists(self):
        # Path to the file where the function should be located
        file_path = '../src/flask/helpers.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Check if the function is defined in helpers.py
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        function_found = False
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef) and node.name == 'explain_template_loading_attempts':
                function_found = True
                break

        self.assertTrue(function_found, "Function 'explain_template_loading_attempts' not found in helpers.py")

    def test_functions_not_in_debughelpers(self):
        # Path to the debughelpers.py file
        file_path = '../src/flask/debughelpers.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Check if the functions are NOT defined in debughelpers.py
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        functions_to_check = [
            'attach_enctype_error_multidict',
            '_dump_loader_info',
            'explain_template_loading_attempts'
        ]

        for function_name in functions_to_check:
            function_found = False
            for node in ast.walk(tree):
                if isinstance(node, ast.FunctionDef) and node.name == function_name:
                    function_found = True
                    break
            self.assertFalse(function_found, f"Function '{function_name}' should not be in debughelpers.py but was found.")

    def test_helpers_py_imports(self):
        # Path to the helpers.py file
        file_path = '../src/flask/helpers.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Check if the specified imports are present in helpers.py
        with open(file_path, 'r') as file:
            content = file.read()

        expected_imports = [
            "from __future__ import annotations",
            "import importlib.util",
            "import os",
            "import sys",
            "import typing as t",
            "from datetime import datetime",
            "from functools import lru_cache",
            "from functools import update_wrapper",
            "import werkzeug.utils",
            "from werkzeug.exceptions import abort as _wz_abort",
            "from werkzeug.utils import redirect as _wz_redirect",
            "from werkzeug.wrappers import Response as BaseResponse",
            "from .blueprints import Blueprint",
            "from .debughelpers import DebugFilesKeyError",
            "from .globals import _cv_request",
            "from .globals import current_app",
            "from .globals import request",
            "from .globals import request_ctx",
            "from .globals import session",
            "from jinja2.loaders import BaseLoader",
            "from .signals import message_flashed",
            "from .sansio.app import App",
            "if t.TYPE_CHECKING:  # pragma: no cover",
            "from .sansio.scaffold import Scaffold",
            "from .wrappers import Response, Request"
        ]

        for expected_import in expected_imports:
            self.assertIn(expected_import, content, f"Import '{expected_import}' not found in helpers.py")

if __name__ == '__main__':
    unittest.main()
