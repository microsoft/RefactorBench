import unittest
import os
import ast

class TestAnsibleImports(unittest.TestCase):

    def test_missing_required_lib_import_in_basic(self):
        file_path = '../lib/ansible/module_utils/basic.py'
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")
        
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        import_found = False
        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom) and node.module == 'ansible.module_utils.utils':
                for name in node.names:
                    if name.name == 'heuristic_log_sanitize':
                        import_found = True
                        break
        
        self.assertTrue(import_found, "Import 'heuristic_log_sanitize' not found in basic.py")

    def test_missing_required_lib_import_in_facts_packages(self):
        file_path = '../lib/ansible/module_utils/facts/packages.py'
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")
        
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        import_found = False
        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom) and node.module == 'ansible.module_utils.utils':
                for name in node.names:
                    if name.name == 'missing_required_lib':
                        import_found = True
                        break
        
        self.assertTrue(import_found, "Import 'missing_required_lib' not found in packages.py")

    def test_missing_required_lib_import_in_urls(self):
        file_path = '../lib/ansible/module_utils/urls.py'
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")
        
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        import_found = False
        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom) and node.module == 'ansible.module_utils.utils':
                for name in node.names:
                    if name.name == 'missing_required_lib':
                        import_found = True
                        break
        
        self.assertTrue(import_found, "Import 'missing_required_lib' not found in urls.py")

    def test_missing_required_lib_import_in_deb822_repository(self):
        file_path = '../lib/ansible/modules/deb822_repository.py'
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")
        
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        import_found = False
        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom) and node.module == 'ansible.module_utils.utils':
                for name in node.names:
                    if name.name == 'missing_required_lib':
                        import_found = True
                        break
        
        self.assertTrue(import_found, "Import 'missing_required_lib' not found in deb822_repository.py")

    def test_missing_required_lib_import_in_expect(self):
        file_path = '../lib/ansible/modules/expect.py'
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")
        
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        import_found = False
        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom) and node.module == 'ansible.module_utils.utils':
                for name in node.names:
                    if name.name == 'missing_required_lib':
                        import_found = True
                        break
        
        self.assertTrue(import_found, "Import 'missing_required_lib' not found in expect.py")

    def test_missing_required_lib_import_in_pip(self):
        file_path = '../lib/ansible/modules/pip.py'
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")
        
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        import_found = False
        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom) and node.module == 'ansible.module_utils.utils':
                for name in node.names:
                    if name.name == 'missing_required_lib':
                        import_found = True
                        break
        
        self.assertTrue(import_found, "Import 'missing_required_lib' not found in pip.py")

    def test_missing_required_lib_import_in_wait_for(self):
        file_path = '../lib/ansible/modules/wait_for.py'
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")
        
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        import_found = False
        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom) and node.module == 'ansible.module_utils.utils':
                for name in node.names:
                    if name.name == 'missing_required_lib':
                        import_found = True
                        break
        
        self.assertTrue(import_found, "Import 'missing_required_lib' not found in wait_for.py")

    def test_missing_required_lib_import_in_netconf_init(self):
        file_path = '../lib/ansible/plugins/netconf/__init__.py'
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")
        
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        import_found = False
        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom) and node.module == 'ansible.module_utils.utils':
                for name in node.names:
                    if name.name == 'missing_required_lib':
                        import_found = True
                        break
        
        self.assertTrue(import_found, "Import 'missing_required_lib' not found in __init__.py")

    def test_missing_required_lib_import_in_missing_required_lib_test(self):
        file_path = '../test/integration/targets/missing_required_lib/library/missing_required_lib.py'
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")
        
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        import_found = False
        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom) and node.module == 'ansible.module_utils.utils':
                for name in node.names:
                    if name.name == 'missing_required_lib':
                        import_found = True
                        break
        
        self.assertTrue(import_found, "Import 'missing_required_lib' not found in missing_required_lib.py")

    def test_missing_required_lib_import_in_test_heuristic_log_sanitize(self):
        file_path = '../test/integration/targets/module_utils/library/test_heuristic_log_sanitize.py'
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")
        
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        import_found = False
        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom) and node.module == 'ansible.module_utils':
                for name in node.names:
                    if name.name == 'utils':
                        import_found = True
                        break
        
        self.assertTrue(import_found, "Import 'utils' not found in test_heuristic_log_sanitize.py")
        
    def test_heuristic_log_sanitize_assignment_in_test_heuristic_log_sanitize(self):
        file_path = '../test/integration/targets/module_utils/library/test_heuristic_log_sanitize.py'
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")
        
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        assignment_found = False
        for node in ast.walk(tree):
            if isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Name) and target.id == 'heuristic_log_sanitize':
                        if isinstance(node.value, ast.Attribute):
                            if node.value.attr == 'heuristic_log_sanitize' and node.value.value.id == 'utils':
                                assignment_found = True
                                break
        
        self.assertTrue(assignment_found, "Assignment 'heuristic_log_sanitize = utils.heuristic_log_sanitize' not found in test_heuristic_log_sanitize.py")


    def test_missing_required_lib_import_in_network_cli(self):
        file_path = '../test/support/network-integration/collections/ansible_collections/ansible/netcommon/plugins/connection/network_cli.py'
        self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")
        
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        import_found = False
        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom) and node.module == 'ansible.module_utils.utils':
                for name in node.names:
                    if name.name == 'missing_required_lib':
                        import_found = True
                        break
        
        self.assertTrue(import_found, "Import 'missing_required_lib' not found in network_cli.py")

if __name__ == '__main__':
    unittest.main()
