#!/usr/bin/python3
""" Import unittest and created a class for unit test """
import os
from datetime import datetime
import unittest
from models.amenity import Amenity
import models.amenity


class TestAmenityDocumentation(unittest.TestCase):
    """ Create a tests for the Amenity class in documentation
    and requirements """

    def test_style_pep8_model(self):
        """ PEP8 python style """
        style_model = os.system("pep8 models/amenity.py")
        self.assertEqual(style_model, 0)

    def test_style_pep8(self):
        """ PEP8 python style """
        style_test = os.system("pep8 tests/test_models/test_amenity.py")
        self.assertEqual(style_test, 0)

    def test_shebang(self):
        """ Test shebang in the front line """
        with open("models/amenity.py", mode='r') as _file:
            readShebang = _file.read()
            lines = readShebang.splitlines()
            self.assertEqual(lines[0], '#!/usr/bin/python3')

    def test_shebang_test(self):
        """ Test shebang in the front line in test file """
        with open("tests/test_models/test_amenity.py", mode='r') as _file:
            readShebang = _file.read()
            lines = readShebang.splitlines()
            self.assertEqual(lines[0], '#!/usr/bin/python3')

    def test_module_doc(self):
        """ Module with sufficient documentation """
        self.assertTrue(len(models.amenity.__doc__) != 0)

    def test_class_doc(self):
        """ Class with sufficient documentation """
        self.assertTrue(len(Amenity.__doc__) != 0)


class TestAmenity(unittest.TestCase):
    """ Create a tests for the class Amenity in edge cases """
    pass
