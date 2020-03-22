import unittest
import os, sys

# Add lib/ to module lookup path
parent_dir = os.path.join(sys.path[0], '../investment_property_boi')
sys.path.insert(1, parent_dir) 

from investment_property_boi import *

class InvestmentPropertyBoiTestCase(unittest.TestCase):

    def setUp(self):
       self.investment_property = InvestmentProperty()

    def teardown(self):
        pass

    def test_can_instantiate_investment_property(self):
        self.assertIsInstance(self.investment_property, InvestmentProperty)

if __name__ == '__main__':
    unittest.main()
