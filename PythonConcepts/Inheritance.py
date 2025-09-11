class Animal:
    totalAnimal : int = 0

    def __init__(self, name, category, legsCount):
        self.name = name
        self.category = category
        self.legsCount = legsCount
        Animal.totalAnimal += 1
    
    def getKillAmount(self):
        pass

    def __del__(self):
        Animal.totalAnimal -= 1

    def __str__(self):
        return f"Animal: {self.name}, category: {self.category}, LegsCount: {self.legsCount}"

class Tiger(Animal):

    def __init__(self, name, category, legsCount, deerKilled):
        super().__init__(name, category, legsCount)
        self.deerKilled = deerKilled

    def getKillAmount(self):
        return self.deerKilled
    
    def __str__(self):
        text = super().__str__()
        text += f" Deer Killed: {self.deerKilled}"
        return text
    
    def __add__(self, other: "Tiger"):
        return Tiger(f"{self.name} - {other.name}", f"{self.category} - {other.category}", -1, -1)

class Bird(Animal):

    def __init__(self, name, category, legsCount, dragonFlyKilled):
        super().__init__(name, category, legsCount)
        self.dragonFlyKilled = dragonFlyKilled
    
    def getKillAmount(self):
        return self.dragonFlyKilled

    def __str__(self):
        text = super().__str__()
        text += f" Dragon Fly Killed: {self.dragonFlyKilled}"
        return text

tiger = Tiger("Tiger", "Mammal", 4, 2)
print(tiger)
bird = Bird("Bird", "Bird", 2, 5)
print(bird)

print("Kill Amount", tiger.getKillAmount())
print("Kill Amount", bird.getKillAmount())

tiger2 = Tiger("Tiger2", "Mammal2", 4, 5)

tigerResult = tiger + tiger2
print(tigerResult)

# Inheritance of class
# Super call
# Overriding str
# Operator Overloading