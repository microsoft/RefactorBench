import unittest
import os
import ast

class TestTornadoMigration(unittest.TestCase):

    def test_getNewIoLoop_used_in_gen_test(self):
        # Path to the file to check for the function usage
        file_path = '../tornado/test/gen_test.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Read and parse the content of gen_test.py
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        getNewIoLoop_found = False
        get_new_ioloop_found = False

        # Check for the usage of self.getNewIoLoop() and self.get_new_ioloop()
        for node in ast.walk(tree):
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute):
                if node.func.attr == 'getNewIoLoop':
                    getNewIoLoop_found = True
                elif node.func.attr == 'get_new_ioloop':
                    get_new_ioloop_found = True

        self.assertTrue(getNewIoLoop_found, "self.getNewIoLoop() not found in gen_test.py")
        self.assertFalse(get_new_ioloop_found, "self.get_new_ioloop() found in gen_test.py, but it should not be present")


    def test_AsyncTestCase_getNewIoLoop_in_ast(self):
        # Path to the file to check for AST usage
        file_path = '../tornado/testing.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Parse the content of testing.py as an AST
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        # Check for AsyncTestCase.getNewIoLoop
        AsyncTestCase_getNewIoLoop_found = False

        for node in ast.walk(tree):
            if isinstance(node, ast.Attribute):
                if node.attr == 'getNewIoLoop' and isinstance(node.value, ast.Name) and node.value.id == 'AsyncTestCase':
                    AsyncTestCase_getNewIoLoop_found = True

        self.assertTrue(AsyncTestCase_getNewIoLoop_found, "AsyncTestCase.getNewIoLoop not found in testing.py")

    def test_self_getNewIoLoop_in_ast(self):
        # Path to the file to check for AST usage
        file_path = '../tornado/testing.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Parse the content of testing.py as an AST
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        # Check for self.getNewIoLoop()
        self_getNewIoLoop_found = False

        for node in ast.walk(tree):
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute):
                if node.func.attr == 'getNewIoLoop':
                    if isinstance(node.func.value, ast.Name) and node.func.value.id == 'self':
                        self_getNewIoLoop_found = True

        self.assertTrue(self_getNewIoLoop_found, "self.getNewIoLoop() not found in testing.py")

    def test_def_getNewIoLoop_in_ast(self):
        # Path to the file to check for AST usage
        file_path = '../tornado/testing.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Parse the content of testing.py as an AST
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        # Check for def getNewIoLoop(self)
        def_getNewIoLoop_found = False
        def_get_new_ioloop_found = False

        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                if node.name == 'getNewIoLoop':
                    def_getNewIoLoop_found = True
                elif node.name == 'get_new_ioloop':
                    def_get_new_ioloop_found = True

        self.assertTrue(def_getNewIoLoop_found, "def getNewIoLoop(self) not found in testing.py")
        self.assertFalse(def_get_new_ioloop_found, "def get_new_ioloop(self) found in testing.py, but it should not be present")

if __name__ == '__main__':
    unittest.main()