''' Cow'a ait Animals'dan inheritance almış class '''

from farm.animal import Animal

class Cow(Animal):
    """İnek: Animal'dan miras alır, beslenince süt üretir."""

    def __init__(self):
        super().__init__()
        self.milk = 0

    def talk(self):
        """İneğin sesini döndürür."""
        return "moo"

    def feed(self):
        super().feed()
        self.milk += 2
