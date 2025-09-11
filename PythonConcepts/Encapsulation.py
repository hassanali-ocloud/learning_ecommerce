class Animal:
    def __init__(self, name, category):
        self.__name = name
        self.__category = category
    
    @property
    def Name(self):
        return self.__name
    @property
    def Category(self):
        return self.__category
    
    @Name.setter
    def Name(self, value):
        self.__name = value
    @Category.setter
    def Category(self, value):
        self.__category = value

    @staticmethod
    def getAllCategories(objs:"Animal"):
        catLs = []
        for obj in objs:
            catLs.append(obj.Category)
        return catLs

animal_1 = Animal("Tiger", "Mammal")
animal_2 = Animal("Sparrow", "Bird")
animal_3 = Animal("Dophine", "Fish")

animal_1.Name = "Frog"
animal_2.Category = "Reptile"
print(Animal.getAllCategories([animal_1, animal_2, animal_3]))

        