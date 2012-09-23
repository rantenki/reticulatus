"""Test STL"""
from reticulatus.geo.stl import STL
import os
import unittest


class TestSTL(unittest.TestCase):
    """Test the STL"""

    def test_20mm_cube(self):
        stl = STL(os.path.join(os.path.dirname(__file__),'20mmbox.stl'))
        #stl.debug = True

        type = stl.type()
        print "Type is: ", type
        if type == "binary":
            print "Length is: ", stl.length()
            print "Header:"
            print stl.header()
        self.assertEquals(type, 'binary')
        stl.read()


    def test_my_head(self):
        stl = STL(os.path.join(os.path.dirname(__file__),'derekhead.stl'))
        type = stl.type()
        print "Type is: ", type
        if type == "binary":
            print stl.header()
            print "Length is: ", stl.length()
        stl.read()
        self.assertEquals(type, 'binary')
        self.assertEquals(stl.length, 33326)

