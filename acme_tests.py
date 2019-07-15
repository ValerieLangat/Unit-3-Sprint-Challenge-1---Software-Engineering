#!/usr/bin/env python

import unittest 
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS 

class AcmeProductTests(unittest.TestCase):
    def test_default_product_price(self):
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)
        
    def test_default_product_weight(self):
        """"Default weights at 20."""
        prod = Product('Test Product')
        self.assertEqual(prod.weight, 20)
        
    def test_explode(self):
        """Testing explode option"""
        prod = Product('Test Product')
        self.assertEqual(prod.flammability, 0.5)
        
class AcmeReportTests(unittest.TestCase):
    def test_default_num_products(self):
        self.assertEqual(len(generate_products()), 30)
        
        
    def test_legal_names(self):
        """Maybe?"""
        items = generate_products()
        for product in items:
            initial = product.name.split()[0]
            secondary = product.name.split()[1]
            self.assertIn(initial,ADJECTIVES)
            self.assertIn(secondary,NOUNS)

        
if __name__ == '__main__':
    unittest.main()
    
    

