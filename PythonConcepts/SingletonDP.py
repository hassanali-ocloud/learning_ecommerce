class AnimalSingleton():
    __instance = None

    @staticmethod
    def get_instance():
        if AnimalSingleton.__instance == None:
            print("No Instance Found")
        else:
            return AnimalSingleton.__instance
        
    def __init__(self, name):
        if AnimalSingleton.__instance != None:
            print("Instance already created. Using Old Instance")
        else:
            self.name = name
            AnimalSingleton.__instance = self
    
    def getName(self):
        return AnimalSingleton.__instance.name


animalInstance = AnimalSingleton("TigerMini")
animalInstance2 = AnimalSingleton("BearMini")
print(animalInstance.getName())
print(animalInstance2.getName())
