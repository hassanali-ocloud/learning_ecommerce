from abc import ABCMeta, abstractmethod

class IAnimal(metaclass=ABCMeta):
    @abstractmethod
    def getName():
        pass

class Tiger(IAnimal):
    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name

class Proxy(IAnimal):
    def __init__(self, animalObj: IAnimal):
        self.animalObj = animalObj

    def getName(self, name):
        if name == "admin":
            print("Proxy get Name Success")
            self.animalObj.getName()
        else:
            print("Proxy blocking")


x = input("Specify your role: ")

tiger = Tiger("TigerMini")
proxy = Proxy(tiger)
proxy.getName(x)
