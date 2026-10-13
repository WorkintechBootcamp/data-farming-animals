# pylint: disable=too-few-public-methods
''' İnek ve Tavuk'a ait parent class'a ait dosya'''

class Animal:
    """Bütün hayvanların ortak parent sınıfı. Energy 0'dan başlar."""

    def __init__(self):
        self.energy = 0

    def feed(self):
        """Hayvanı besler, energy 1 artar."""
        self.energy += 1
