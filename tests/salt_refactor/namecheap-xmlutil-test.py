import unittest
import os
import ast

class TestXmlUtilFunctions(unittest.TestCase):

    def test_xml_to_dict_in_xmlutil(self):
        file_path = '../salt/utils/xmlutil.py'
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        xml_to_dict_found = any(isinstance(node, ast.FunctionDef) and node.name == 'xml_to_dict' for node in ast.walk(tree))

        self.assertTrue(xml_to_dict_found, f"Function 'xml_to_dict' not found in {file_path}, but it should be present")

    def test_atts_to_dict_in_xmlutil(self):
        file_path = '../salt/utils/xmlutil.py'
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        atts_to_dict_found = any(isinstance(node, ast.FunctionDef) and node.name == 'atts_to_dict' for node in ast.walk(tree))

        self.assertTrue(atts_to_dict_found, f"Function 'atts_to_dict' not found in {file_path}, but it should be present")

    def test_string_to_value_in_xmlutil(self):
        file_path = '../salt/utils/xmlutil.py'
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        string_to_value_found = any(isinstance(node, ast.FunctionDef) and node.name == 'string_to_value' for node in ast.walk(tree))

        self.assertTrue(string_to_value_found, f"Function 'string_to_value' not found in {file_path}, but it should be present")

    def test_xml_to_dict_not_in_namecheap(self):
        file_path = '../salt/utils/namecheap.py'
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        xml_to_dict_found = any(isinstance(node, ast.FunctionDef) and node.name == 'xml_to_dict' for node in ast.walk(tree))

        self.assertFalse(xml_to_dict_found, f"Function 'xml_to_dict' found in {file_path}, but it should not be present")

    def test_atts_to_dict_not_in_namecheap(self):
        file_path = '../salt/utils/namecheap.py'
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        atts_to_dict_found = any(isinstance(node, ast.FunctionDef) and node.name == 'atts_to_dict' for node in ast.walk(tree))

        self.assertFalse(atts_to_dict_found, f"Function 'atts_to_dict' found in {file_path}, but it should not be present")

    def test_string_to_value_not_in_namecheap(self):
        file_path = '../salt/utils/namecheap.py'
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        string_to_value_found = any(isinstance(node, ast.FunctionDef) and node.name == 'string_to_value' for node in ast.walk(tree))

        self.assertFalse(string_to_value_found, f"Function 'string_to_value' found in {file_path}, but it should not be present")

if __name__ == '__main__':
    unittest.main()
