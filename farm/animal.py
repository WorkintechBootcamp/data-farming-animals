''' İnek ve Tavuk'a ait parent class'a ait dosya'''

class Animal:
    def __init__(self):
        self.energy = 0

    def feed(self):
        self.energy += 1
