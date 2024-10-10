import unittest
import os
import ast

class TestScrapyMigration(unittest.TestCase):

    def test_xmliter_has_log_parameter(self):
        # Path to the file where the xmliter function is defined
        file_path = '../scrapy/utils/iterators.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Check if the xmliter function has a log boolean parameter
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        function_found = False
        log_param_found = False
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef) and node.name == 'xmliter':
                function_found = True
                for arg in node.args.args:
                    if arg.arg == 'log':
                        if isinstance(arg.annotation, ast.Name) and arg.annotation.id == 'bool':
                            log_param_found = True
                            break
                break

        self.assertTrue(function_found, "Function 'xmliter' not found in iterators.py")
        self.assertTrue(log_param_found, "Parameter 'log: bool' not found in 'xmliter' function")
        
    def test_tests_py_imports_updated(self):
        # Path to the test file
        tests_file_path = '../tests/test_utils_iterators.py' 

        # Check if the test file exists
        self.assertTrue(os.path.exists(tests_file_path), f"Test file {tests_file_path} does not exist")

        # Check if the import statement for xmliter is correct
        with open(tests_file_path, 'r') as file:
            tree = ast.parse(file.read())

        import_found = False
        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom):
                if node.module == 'scrapy.utils.iterators' and \
                   any(alias.name == 'xmliter' for alias in node.names):
                    import_found = True
                    break

        self.assertTrue(import_found, "Import 'from scrapy.utils.iterators import xmliter' not found in test_utils_iterators.py")
    
    def test_xmliter_calls_have_log_parameter(self):
        # Path to the test file where xmliter should be called with log parameter
        test_file_path = '../tests/test_utils_iterators.py'

        # Check if the test file exists
        self.assertTrue(os.path.exists(test_file_path), f"{test_file_path} does not exist")

        # Check if all xmliter calls have log=False parameter
        with open(test_file_path, 'r') as file:
            tree = ast.parse(file.read())

        xmliter_calls = [
            node for node in ast.walk(tree)
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == 'xmliter'
        ]

        for call in xmliter_calls:
            log_param_found = False
            for kw in call.keywords:
                if kw.arg == 'log' and isinstance(kw.value, ast.Constant) and kw.value.value is False:
                    log_param_found = True
                    break
            self.assertTrue(log_param_found, f"xmliter call at line {call.lineno} does not have 'log=False'")


if __name__ == '__main__':
    unittest.main()
