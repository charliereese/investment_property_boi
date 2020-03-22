import unittest
import os, sys

# Add lib/ to module lookup path
parent_dir = os.path.join(sys.path[0], '../investment_property_boi')
sys.path.insert(1, parent_dir) 

# from mortgage import *

class InvestmentPropertyBoiTestCase(unittest.TestCase):

    def setUp(self):
       pass 

    def teardown(self):
        pass

    def test_working(self):
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()
