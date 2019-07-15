#!/usr/bin/env python

from random import randint, sample, uniform
from acme import Product

ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']

def generate_products(num_products=30):
    products = []
    for i in range(num_products):
        name = sample(ADJECTIVES, 1)[0] + ' ' + sample(NOUNS, 1)[0]
        price = randint(5, 100)
        weight = randint(5, 100)
        flammability = uniform(0,2.5)
        products.append(Product(name=name, price=price, weight=weight, flammability=flammability))

    return products


    
def inventory_report(products):
    names = len(products)
    for _ in products:
        prod_prices = []
        prod_prices.append(_.price)
        weights = []
        weights.append(_.weight)
        flammability_vals = []
        flammability_vals.append(_.flammability)
        
    mean_price = sum(prod_prices)/len(prod_prices)
    mean_weight = sum(weights)/len(weights)
    mean_flammability = sum(flammability_vals)/len(flammability_vals)
    
    print(f"ACME CORPORATION OFFICIAL INVENTORY REPORT\n"
          f"Unique Product Names: {names}\n"
          f"Average Prices: {mean_price}\n"
          f"Average Weights: {mean_weight}\n"
          f"Average Flammability: {mean_flammability}")

if __name__ == '__main__':
    inventory_report(generate_products())
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    