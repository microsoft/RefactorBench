import unittest
import os
import ast

class TestVerifyReactorMigration(unittest.TestCase):

    def test_verify_reactor_class_exists(self):
        # Path to the file where the class should be located
        file_path = '../scrapy/utils/reactor.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Check if the class VerifyReactor is defined in reactor.py
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        class_found = False
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef) and node.name == 'VerifyReactor':
                class_found = True
                break

        self.assertTrue(class_found, "Class 'VerifyReactor' not found in reactor.py")

    def test_verify_reactor_methods_exist(self):
        # Path to the file where the class should be located
        file_path = '../scrapy/utils/reactor.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Check if the methods are defined in the VerifyReactor class
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        methods_found = {'verify_installed_reactor': False,
                         'verify_installed_asyncio_event_loop': False,
                         'is_asyncio_reactor_installed': False}

        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef) and node.name == 'VerifyReactor':
                for class_node in node.body:
                    if isinstance(class_node, ast.FunctionDef) and class_node.name in methods_found:
                        methods_found[class_node.name] = True

        for method, found in methods_found.items():
            self.assertTrue(found, f"Method '{method}' not found in VerifyReactor class")

    def test_defer_imports_verify_reactor(self):
        # Path to the defer file where the imports should be located
        defer_file_path = '../scrapy/utils/defer.py'

        # Check if the defer file exists
        self.assertTrue(os.path.exists(defer_file_path), f"{defer_file_path} does not exist")

        # Check if the import statement is correct
        with open(defer_file_path, 'r') as file:
            tree = ast.parse(file.read())

        imports_found = {
            '_get_asyncio_event_loop': False,
            'VerifyReactor': False
        }

        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom):
                if node.module == 'scrapy.utils.reactor':
                    for alias in node.names:
                        if alias.name in imports_found:
                            imports_found[alias.name] = True

        for imp, found in imports_found.items():
            self.assertTrue(found, f"Import '{imp}' from 'scrapy.utils.reactor' not found in defer.py")

    def test_crawler_imports_verify_reactor(self):
        # Path to the crawler file where the imports should be located
        crawler_file_path = '../scrapy/crawler.py'

        # Check if the crawler file exists
        self.assertTrue(os.path.exists(crawler_file_path), f"{crawler_file_path} does not exist")

        # Check if the import statement is correct
        with open(crawler_file_path, 'r') as file:
            tree = ast.parse(file.read())

        imports_found = {
            'install_reactor': False,
            'VerifyReactor': False
        }

        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom):
                if node.module == 'scrapy.utils.reactor':
                    for alias in node.names:
                        if alias.name in imports_found:
                            imports_found[alias.name] = True

        for imp, found in imports_found.items():
            self.assertTrue(found, f"Import '{imp}' from 'scrapy.utils.reactor' not found in crawler.py")

    def test_asyncio_docs_mention_verify_reactor(self):
        # Path to the docs file where the statement should be located
        docs_file_path = '../docs/topics/asyncio.rst'

        # Check if the docs file exists
        self.assertTrue(os.path.exists(docs_file_path), f"{docs_file_path} does not exist")

        # Check if the specific line is present in the file
        with open(docs_file_path, 'r') as file:
            content = file.read()

        self.assertIn(
            "if not VerifyReactor.is_asyncio_reactor_installed():",
            content,
            "Line 'if not VerifyReactor.is_asyncio_reactor_installed():' not found in asyncio.rst"
        )

    def test_utils_asyncio_imports_verify_reactor(self):
        # Path to the test_utils_asyncio file where the imports should be located
        test_utils_asyncio_file_path = '../tests/test_utils_asyncio.py'

        # Check if the test_utils_asyncio file exists
        self.assertTrue(os.path.exists(test_utils_asyncio_file_path), f"{test_utils_asyncio_file_path} does not exist")

        # Check if the import statement is correct
        with open(test_utils_asyncio_file_path, 'r') as file:
            tree = ast.parse(file.read())

        imports_found = {
            'install_reactor': False,
            'VerifyReactor': False,
            'set_asyncio_event_loop': False
        }

        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom):
                if node.module == 'scrapy.utils.reactor':
                    for alias in node.names:
                        if alias.name in imports_found:
                            imports_found[alias.name] = True

        for imp, found in imports_found.items():
            self.assertTrue(found, f"Import '{imp}' from 'scrapy.utils.reactor' not found in test_utils_asyncio.py")

    def test_shell_imports_verify_reactor(self):
        # Path to the shell file where the imports should be located
        shell_file_path = '../scrapy/shell.py'

        # Check if the shell file exists
        self.assertTrue(os.path.exists(shell_file_path), f"{shell_file_path} does not exist")

        # Check if the import statement is correct
        with open(shell_file_path, 'r') as file:
            tree = ast.parse(file.read())

        imports_found = {
            'VerifyReactor': False,
            'set_asyncio_event_loop': False
        }

        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom):
                if node.module == 'scrapy.utils.reactor':
                    for alias in node.names:
                        if alias.name in imports_found:
                            imports_found[alias.name] = True

        for imp, found in imports_found.items():
            self.assertTrue(found, f"Import '{imp}' from 'scrapy.utils.reactor' not found in shell.py")

    def test_crawler_class_has_verify_reactor_logic(self):
        # Path to the crawler file where the logic should be located
        crawler_file_path = '../scrapy/crawler.py'

        # Check if the crawler file exists
        self.assertTrue(os.path.exists(crawler_file_path), f"{crawler_file_path} does not exist")

        # Parse the crawler file to analyze the AST
        with open(crawler_file_path, 'r') as file:
            tree = ast.parse(file.read())

        class_found = False
        method_found = False
        logic_found = False

        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef) and node.name == 'Crawler':
                class_found = True
                for class_node in node.body:
                    if isinstance(class_node, ast.FunctionDef):
                        method_found = True
                        for method_node in ast.walk(class_node):
                            if isinstance(method_node, ast.If):
                                if isinstance(method_node.test, ast.Name) and method_node.test.id == 'reactor_class':
                                    for stmt in method_node.body:
                                        if isinstance(stmt, ast.Expr):
                                            if isinstance(stmt.value, ast.Call):
                                                if isinstance(stmt.value.func, ast.Attribute) and stmt.value.func.attr == 'verify_installed_reactor':
                                                    logic_found = True
                                                    break
                        if logic_found:
                            break

        self.assertTrue(class_found, "Class 'Crawler' not found in crawler.py")
        self.assertTrue(method_found, "No methods found in 'Crawler' class")
        self.assertTrue(logic_found, "VerifyReactor logic not found in any method of 'Crawler' class")
        
    def test_deferred_from_coro_has_verify_reactor_logic(self):
        # Path to the defer file where the logic should be located
        defer_file_path = '../scrapy/utils/defer.py'

        # Check if the defer file exists
        self.assertTrue(os.path.exists(defer_file_path), f"{defer_file_path} does not exist")

        # Parse the defer file to analyze the AST
        with open(defer_file_path, 'r') as file:
            tree = ast.parse(file.read())

        verify_reactor_prefix_found = True

        # Traverse the AST to find occurrences of is_asyncio_reactor_installed
        for node in ast.walk(tree):
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute):
                if node.func.attr == 'is_asyncio_reactor_installed':
                    # Check if the prefix is VerifyReactor
                    if not (isinstance(node.func.value, ast.Name) and node.func.value.id == 'VerifyReactor'):
                        verify_reactor_prefix_found = False
                        break

        self.assertTrue(verify_reactor_prefix_found, "Found 'is_asyncio_reactor_installed' not prefixed by 'VerifyReactor' in defer.py")
    def test_utils_asyncio_has_verify_reactor_logic(self):
        # Path to the test_utils_asyncio file where the logic should be located
        test_utils_asyncio_file_path = '../tests/test_utils_asyncio.py'

        # Check if the test_utils_asyncio file exists
        self.assertTrue(os.path.exists(test_utils_asyncio_file_path), f"{test_utils_asyncio_file_path} does not exist")

        # Parse the test_utils_asyncio file to analyze the AST
        with open(test_utils_asyncio_file_path, 'r') as file:
            tree = ast.parse(file.read())

        verify_reactor_prefix_found = True

        # Traverse the AST to find occurrences of is_asyncio_reactor_installed
        for node in ast.walk(tree):
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute):
                if node.func.attr == 'is_asyncio_reactor_installed':
                    # Check if the prefix is VerifyReactor
                    if not (isinstance(node.func.value, ast.Name) and node.func.value.id == 'VerifyReactor'):
                        verify_reactor_prefix_found = False
                        break

        self.assertTrue(verify_reactor_prefix_found, "Found 'is_asyncio_reactor_installed' not prefixed by 'VerifyReactor' in test_utils_asyncio.py")
    
    def test_shell_has_verify_reactor_logic(self):
        # Path to the shell file where the logic should be located
        shell_file_path = '../scrapy/shell.py'

        # Check if the shell file exists
        self.assertTrue(os.path.exists(shell_file_path), f"{shell_file_path} does not exist")

        # Parse the shell file to analyze the AST
        with open(shell_file_path, 'r') as file:
            tree = ast.parse(file.read())

        verify_reactor_prefix_found = True

        # Traverse the AST to find occurrences of is_asyncio_reactor_installed
        for node in ast.walk(tree):
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute):
                if node.func.attr == 'is_asyncio_reactor_installed':
                    # Check if the prefix is VerifyReactor
                    if not (isinstance(node.func.value, ast.Name) and node.func.value.id == 'VerifyReactor'):
                        verify_reactor_prefix_found = False
                        break

        self.assertTrue(verify_reactor_prefix_found, "Found 'is_asyncio_reactor_installed' not prefixed by 'VerifyReactor' in shell.py")

if __name__ == '__main__':
    unittest.main()
