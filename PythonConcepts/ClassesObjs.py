class Animal:
    totalAnimal : int = 0

    def __init__(self, name, specie, legsCount):
        self.name = name
        self.specie = specie
        self.legsCount = legsCount
        Animal.totalAnimal += 1
    
    def __del__(self):
        Animal.totalAnimal -= 1

    def __str__(self):
        return f"Animal: {self.name}, Specie: {self.specie}, LegsCount: {self.legsCount}"

    
animal1 = Animal("Crocodile", "Reptile", 4)
animal2 = Animal("Dolphines", "Mammal", 0)
print(f"Animal Count: {Animal.totalAnimal}")

print(animal1)
del animal1

print(f"Animal Count: {Animal.totalAnimal}")