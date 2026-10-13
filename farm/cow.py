''' Cow'a ait Animals'dan inheritance almış class '''

from farm.animal import Animal

class Cow(Animal):
    def talk(self):
        return "moo"
