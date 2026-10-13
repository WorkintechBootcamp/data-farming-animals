''' Chicken'a ait Animals'dan inheritance almış class '''
from farm.animal import Animal

class Chicken(Animal):
    """Tavuk: Animal'dan miras alır, cinsiyeti vardır, dişiler yumurta üretir."""

    def __init__(self,gender):
        super().__init__()
        self.gender = gender
        self.eggs = 0

    def talk(self):
        """Tavuğun cinsiyetine göre sesini döndürür."""
        if self.gender == "male":
            return "cock-a-doodle-doo"
        return "cluck cluck"

    def feed(self):
        super().feed()
        if self.gender == "female":
            self.eggs += 2
