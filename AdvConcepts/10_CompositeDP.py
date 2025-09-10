from abc import ABCMeta, abstractmethod

class IJungle(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, noOfAnimals, name):
        pass

    @abstractmethod
    def print_no_of_animals():
        pass

class Animals:
    def __init__(self):
        self.animals = []
    
    def add(self, animal):
        self.animals.append(animal)
    
    def print_animals_data(self):
        print("Animals Data: ")
        for x in self.animals:
            print(f"Category: {x.name}")
            print(f"No Of Animals: {x.noOfAnimals}")

class Reptiles(IJungle):
    def __init__(self, noOfAnimals, name):
        self.name = name
        self.noOfAnimals = noOfAnimals

    def print_no_of_animals(self):
        print(f"No Of Reptiles: f{self.noOfAnimals}")

class Mammals(IJungle):
    def __init__(self, noOfAnimals, name):
        self.name = name
        self.noOfAnimals = noOfAnimals

    def print_no_of_animals(self):
        print(f"No Of Mammals: f{self.noOfAnimals}")
        
reptiles = Reptiles(20, "Reptiles")
mammals = Mammals(20, "Mammals")
animals = Animals()
animals.add(reptiles)
animals.add(mammals)
animals.print_animals_data()

