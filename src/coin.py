from random import choice

class Coin:
    def __init__(self):
        self.states = ['H', 'T']
    
    def flip(self):
        return choice(self.states)