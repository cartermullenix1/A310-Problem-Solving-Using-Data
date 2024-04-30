from Creature import Creature

class Cow(Creature):
    def __init__(self, name):
        super().__init__(name)
    
    def makeSound(self):
        return ": Moo."
        
# a = Cow("George")

# a.talk()