from abc import ABCMeta, abstractmethod

class IAnimal(metaclass=ABCMeta):
    @abstractmethod
    def getName():
        pass

    @abstractmethod
    def getCategory():
        pass

class Tiger(IAnimal):
    def __init__(self, name, category):
        self.name = name
        self.category = category

    def getName(self):
        return self.name
    
    def getCategory(self):
        return self.category
    
class AnimalFactory:
    @staticmethod
    def build_animal(animalType, x, y):
        if (animalType == "Tiger"):
            return Tiger(x, y)

x = input("Specify the name of Animal: ")
y = input("Specify the category of Animal: ")

animal = AnimalFactory.build_animal(x, x, y)
print(animal.getName())
print(animal.getCategory())