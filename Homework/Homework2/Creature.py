class Creature:
    def __init__(self, name):
        self.name = name
        print("Creature " + self.name + " created.")
    
    def talk(self):
        print("My name is " + self.name + " and I am a " + type(self).__name__ + self.makeSound())
    
    def makeSound(self):
        return ""

# a = Creature("Bill")

# a.talk()

# a.makeSound()