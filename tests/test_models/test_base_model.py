#!/usr/bin/python3
"""
Import unittest and created a class for unit test
"""

import os
import unittest
from models.base_model import BaseModel
import models.base_model

class TestBaseDocumentation(unittest.TestCase):
    """ Create a tests for the base class in documentation
    and requirements """
    def test_readme(self):
        """ Created a readme and that exists """
        theReadme = os.getcwd()
        readmeOne = theReadme + '/README.md'
        readmeTwo = os.path.exists(readmeOne)
        self.assertTrue(readmeTrue, True)
        with open(readmeOne, mode='r') as _file:
            readShebang = _file.read()
            self.assertTrue(len(readShebang) != 0)

    def test_style_pep8_model(self):
        """ PEP8 python style """
        style_model = os.system("pep8 models/base_model.py")
        self.assertEqual(style_model, 0)

    def test_style_pep8(self):
        """ PEP8 python style """
        style_test = os.system("pep8 tests/test_base_model.py")
        self.assertEqual(style_test, 0)

    def test_shebang(self):
        """ Test shebang in the front line """
        with open("models/base_model.py", mode='r') as _file:
            readShebang = _file.read()
            lines = readShebang.splitlines()
            self.assertEqual(lines[0], '#!/usr/bin/python3')

    def test_shebang_test(self):
        """ Test shebang in the front line in test file """
        with open("tests/test_base_model.py", mode='r') as _file:
            readShebang = _file.read()
            lines = readShebang.splitlines()
            self.assertEqual(lines[0], '#!/usr/bin/python3')

    def test_module_doc(self):
        """ Module with sufficient documentation """
        self.assertTrue(len(models.base_model.__doc__) != 0)

    def test_class_doc(self):
        """ Class with sufficient documentation """
        self.assertTrue(len(BaseModel.__doc__) != 0)

    def test_methods_doc(self):
        """ Methods with sufficient documentation """
        self.assertTrue(len(BaseModel.save.__doc__) != 0)
        self.assertTrue(len(BaseModel.to_dict.__doc__) != 0)
