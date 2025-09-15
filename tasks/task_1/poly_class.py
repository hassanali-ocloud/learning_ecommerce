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
        self.dirs: list[Directory] = []
        self.files: list[File] = []

    @property
    def name(self):
        return self._name

    def add(self, obj):
        if type(obj) == File:
            self.files.append(obj)
        elif type(obj) == Directory:
            self.dirs.append(obj)

    def display(self, level: int = 0, is_root: bool = True):      
        if is_root:
            print(f"{IFileSystem.get_indent_str(level)}@ {self.name}")

        for file in self.files:
            file.display(level)
        for dir in self.dirs:
            print(f"{IFileSystem.get_indent_str(level)}@ {dir.name}")
            dir.display(level+2, False)

    def get_size(self):
        total_size: int = 0
        for file in self.files:
            total_size += file.get_size()
        for dir in self.dirs:
            total_size += dir.get_size()
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
        

# Create Interface File System
## There functions -> add, display, size
## Override them

# Create Directory class from I
## Here override add and thus calling it creates a folder
## Here override display and it will show us the contents of this folder
## Here override size and it will calculate the size of all files in that folder

# Create File class
## Here create func, creates a file with its size.
## Here get size func, will provide us size