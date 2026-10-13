''' Chicken'a ait Animals'dan inheritance almış class '''
from farm.animal import Animal

class Chicken(Animal):
    def __init__(self,gender):
        self.gender = gender
    def talk(self):
        if self.gender == "male":
            return "cock-a-doodle-doo"
        else:
            return "cluck cluck"
