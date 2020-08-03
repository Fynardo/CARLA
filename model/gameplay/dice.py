import random

class Dice:
    def __init__(self, size=10, modifier=0):
        self.size = size
        self.modifier = modifier

    @property
    def lower(self):
        return self.modifier + 1

    @property
    def upper(self):
        return self.size + self.modifier

    @property
    def faces(self):
        return list(range(self.modifier+1, self.size + self.modifier + 1))
    
    def roll(self):
        return random.randint(1, self.size) + self.modifier
