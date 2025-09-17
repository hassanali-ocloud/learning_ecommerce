from abc import ABCMeta, abstractmethod

class IFileSystem(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def add(self):
        pass
    
    @abstractmethod
    def display(self):
        pass

    @abstractmethod
    def get_size(self):
        pass

    @staticmethod
    def get_indent_str(indent_amount):
        indent_str = ""
        while indent_amount!=0:
            indent_str += " "
            indent_amount -= 1
        return indent_str

class Directory(IFileSystem):
    def __init__(self, name):
        self._name = name
        self.components: list[IFileSystem] = []

    @property
    def name(self):
        return self._name

    def add(self, obj):
        self.components.append(obj)

    def display(self, level: int = 0):      
        print(f"{IFileSystem.get_indent_str(level)}@ {self.name}")

        for component in self.components:
            component.display(level+2)

    def get_size(self):
        total_size: int = 0
        for component in self.components:
            total_size += component.get_size()
        return total_size

class File(IFileSystem):
    def __init__(self, name, size):
        self._name = name
        self._size = size
    
    @property
    def name(self):
        return self._name
    
    def add(self):
        pass

    def display(self, indent_amount):
        print(f"{IFileSystem.get_indent_str(indent_amount)}* {self._name}")

    def get_size(self):
        return self._size