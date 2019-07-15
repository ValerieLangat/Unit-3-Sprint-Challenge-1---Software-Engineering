from random import randint

class Product:
    
    def __init__(self, name, price=10, weight=20, flammability=0.5):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = randint(1000000, 9999999)
        
    def stealability(self):
        stealing = self.price/self.weight
        if stealing < 0.5:
            return 'Not So Stealable...'
        if (stealing >= 0.5) & (stealing < 1.0):
            return 'Kinda Stealable'
        return 'Very Stealable'
        
    def explode(self):
        pyro = self.weight*self.flammability
        if pyro >= 50:
            return '...BABOOM!'
        if pyro >= 10:
            return '...boom!'
        return '...fizzle.'
    
class BoxingGlove(Product):
    def __init__(self, name, price=10, weight=10, flammability =0.5):
        super().__init__(self, price, weight, flammability)
        
    def explode(self):
        return '...its a glove.'
    def punch(self):
        if self.weight >= 15:
            return 'OUCH!'
        if self.weight >= 5:
            return 'Hey that hurt!'
        return 'That tickles!'
    
    