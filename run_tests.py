"""
Bamboo Test Runner
"""

import unittest
import xmlrunner

if __name__ == '__main__':
    targets = ['randtest']
    for target in targets:
        test_suite = unittest.defaultTestLoader.discover(target)
        runner = xmlrunner.XMLTestRunner(output=f"output/test-{target}")
        runner.run(test_suite)
