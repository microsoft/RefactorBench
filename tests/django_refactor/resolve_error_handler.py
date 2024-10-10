import unittest
import ast


class TestResolveErrorHandler(unittest.TestCase):
    
    '''
    def test_function_definition(self):
        self.assertTrue(hasattr(URLResolver, 'resolve_error_handler'), "URLResolver class does not have resolve_error_handler method")
        
        method = getattr(URLResolver, 'resolve_error_handler')
        
        # Print diagnostic information
        print(f"Django version: {django.__version__}")
        print(f"URLResolver module: {URLResolver.__module__}")
        print(f"Method: {method}")
        print(f"Method source:\n{inspect.getsource(method)}")
        
        signature = inspect.signature(method)
        print(f"Signature: {signature}")
        
        # Check if 'log' parameter exists
        if 'log' in signature.parameters:
            self.assertEqual(signature.parameters['log'].default, False, "log parameter default value should be False")
        else:
            # If 'log' is not in the signature, fail the test and show the actual parameters
            self.fail(f"log parameter is missing in the function definition. Actual parameters: {list(signature.parameters.keys())}")
    '''

    def test_function_def(self):
        file_path = '../django/urls/resolvers.py'  

        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef) and node.name == 'resolve_error_handler':
                # Check if the function has the correct arguments
                args = [arg.arg for arg in node.args.args]
                self.assertIn('self', args, "Missing 'self' parameter")
                self.assertIn('view_type', args, "Missing 'view_type' parameter")
                
                # Check for the log parameter
                log_param = next((kw for kw in node.args.defaults if isinstance(kw, ast.NameConstant) and kw.value is False), None)
                self.assertIsNotNone(log_param, "log parameter with default False is missing")
                
                # Check the function body for log-related code
                log_check = any(
                    isinstance(stmt, ast.If) and 
                    isinstance(stmt.test, ast.Name) and 
                    stmt.test.id == 'log'
                    for stmt in node.body
                )
                self.assertTrue(log_check, "Missing log check in function body")
                
                return  

        self.fail("resolve_error_handler function not found in the file")

    def test_usages_have_log_true(self):
        files_to_check = [
            '../django/core/handlers/exception.py',
            '../django/core/checks/urls.py',
            '../tests/urlpatterns_reverse/tests.py',
        ]

        for file_path in files_to_check:
            with open(file_path, 'r') as f:
                tree = ast.parse(f.read())

            for node in ast.walk(tree):
                if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute):
                    if node.func.attr == 'resolve_error_handler':
                        if isinstance(node.func.value, ast.Name) and node.func.value.id in ['resolver', 'self', 'url_resolver']:
                            log_arg = next((kw for kw in node.keywords if kw.arg == 'log'), None)
                            self.assertIsNotNone(log_arg, f"log parameter missing in {file_path}")
                            self.assertTrue(
                                isinstance(log_arg.value, ast.NameConstant) and log_arg.value.value is True,
                                f"log is not True in {file_path}"
                            )
                            self.assertTrue(len(node.args) > 0, f"Missing status_code argument in {file_path}")

if __name__ == '__main__':
    unittest.main()