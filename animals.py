class Animal(object):
    def __init__(self, name):
        self.name = name
        self.health = 100
    def walk(self, mult=1):
        self.health-=1*mult
        return self
    def run(self, mult=1):
        self.health-=5*mult
        return self
    def displayHealth(self):
        print self.health
        return self

class Dog(Animal):
    def __init__(self, name):
        super(Dog, self).__init__(name)
        self.health=150 
    def pet(self, mult=1):
        self.health+=5*mult
        return self 

class Dragon(Animal):
    def __init__(self, name):
        super(Dragon, self).__init__(name)
        self.health=170 
    def fly(self, mult=1):
        self.health-=10*mult
        return self
    def displayHealth(self):
        super(Dragon, self).displayHealth()
        print "I am a Dragon"
monster=Animal("Monster")
monster.walk(3).run(2).displayHealth()

rover=Dog("rover")
rover.walk(3).run(2).pet(1).displayHealth()

puff=Dragon("Puff")
puff.fly().displayHealth()
