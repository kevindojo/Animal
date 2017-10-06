class Animal(object):
    def __init__(self, name):
        self.name = name
        self.health = 100
    def walk(self):
        print "!walking"
        self.health = self.health - 1
        return self
    def run(self):
        print "!!!running"
        self.health = self.health -5
        return self
    def displayHealth(self):
        print "My name is: " + self.name
        print "I have: " + str(self.health) + "health left!"

animal1 =Animal("BeastBoy")
animal1.walk().walk().walk().run().run().displayHealth()


class Dog(Animal):
    def __init__(self, name):
        super(Dog, self).__init__(name)
        self.health = 150

    def pet(self):
        print "pet pet"
        self.pet = self.health + 5
        return self

dog1 = Dog("cat")
dog1.walk().walk().walk().run().pet().displayHealth()

class Dragon(Animal):
    def __init__(self, name):
        super(Dragon, self).__init__(name)
        self.health = 170

    def fly(self):
        print "fly fly"
        self.health = self.health - 10
        return self

    def displayHealth(self):
        print "I'm a Dragon"
        super(Dragon,self).displayHealth()

dragon = Dragon("toothless")
dragon.fly().displayHealth()






# paw =Animal("pup", 150)
# paw.walk().walk().walk().run().run().displayHealth()

# paw =Dog("pup", 150)
# paw.pet().walk().walk().walk().run().run().displayHealth()