import unittest
import os
import ast

class TestAnsibleImports(unittest.TestCase):

    def test_import_in_ansible_collector(self):
        # Path to the file where ansible_collector.py should be checked
        file_path = '../lib/ansible/module_utils/facts/ansible_collector.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Check if the specific text string exists in the file
        search_string = "ansible.module_utils.facts.compat.PrefixFactNamespace(prefix='ansible_')"
        with open(file_path, 'r') as file:
            file_content = file.read()

        # Check if the search string is present in the file content
        self.assertIn(search_string, file_content, f"'{search_string}' not found in ansible_collector.py")


    def test_import_in_compat(self):
        # Path to the file where compat.py should be checked
        file_path = '../lib/ansible/module_utils/facts/compat.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Check if PrefixFactNamespace is imported from ansible.module_utils.facts.compat
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        import_found = False
        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom):
                if (node.module == 'ansible.module_utils.facts.namespace' and
                        any(alias.name == 'PrefixFactNamespace' for alias in node.names)):
                    import_found = True
                    break

        self.assertFalse(import_found, "PrefixFactNamespace imported from 'ansible.module_utils.facts.namespace' in compat.py")

    def test_import_in_facter(self):
        # Path to the file where facter.py should be checked
        file_path = '../lib/ansible/module_utils/facts/other/facter.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Check if PrefixFactNamespace is imported from ansible.module_utils.facts.compat
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        import_found = False
        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom):
                if (node.module == 'ansible.module_utils.facts.compat' and
                        any(alias.name == 'PrefixFactNamespace' for alias in node.names)):
                    import_found = True
                    break

        self.assertTrue(import_found, "PrefixFactNamespace not imported from 'ansible.module_utils.facts.compat' in facter.py")

    def test_import_in_ohai(self):
        # Path to the file where ohai.py should be checked
        file_path = '../lib/ansible/module_utils/facts/other/ohai.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Check if PrefixFactNamespace is imported from ansible.module_utils.facts.compat
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        import_found = False
        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom):
                if (node.module == 'ansible.module_utils.facts.compat' and
                        any(alias.name == 'PrefixFactNamespace' for alias in node.names)):
                    import_found = True
                    break

        self.assertTrue(import_found, "PrefixFactNamespace not imported from 'ansible.module_utils.facts.compat' in ohai.py")

    def test_import_in_setup(self):
        # Path to the file where setup.py should be checked
        file_path = '../lib/ansible/modules/setup.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Check if PrefixFactNamespace is imported from ansible.module_utils.facts.compat
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        import_found = False
        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom):
                if (node.module == 'ansible.module_utils.facts.compat' and
                        any(alias.name == 'PrefixFactNamespace' for alias in node.names)):
                    import_found = True
                    break

        self.assertTrue(import_found, "PrefixFactNamespace not imported from 'ansible.module_utils.facts.compat' in setup.py")
        
    def test_import_in_test_ansible_collector(self):
        # Path to the file where test_ansible_collector.py should be checked
        file_path = '../test/units/module_utils/facts/test_ansible_collector.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Parse the file and check if 'from ansible.module_utils.facts import compat' exists
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        import_found = False
        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom):
                if node.module == 'ansible.module_utils.facts' and any(alias.name == 'compat' for alias in node.names):
                    import_found = True
                    break

        self.assertTrue(import_found, "'from ansible.module_utils.facts import compat' not found in test_ansible_collector.py")

    def test_ns_in_test_ansible_collector(self):
        # Path to the file where test_ansible_collector.py should be checked
        file_path = '../test/units/module_utils/facts/test_ansible_collector.py'

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Check if 'from ansible.module_utils.facts import compat' exists in the file
        search_string = "ns = compat.PrefixFactNamespace('ansible_facts', 'ansible_')"
        with open(file_path, 'r') as file:
            file_content = file.read()

        # Check if the search string is present in the file content
        self.assertIn(search_string, file_content, f"'{search_string}' not found in test_ansible_collector.py")


if __name__ == '__main__':
    unittest.main()
