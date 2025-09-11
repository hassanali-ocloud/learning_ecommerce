class FileManager:
    def __init__(self):
        pass

    def write_to_file(self, filename, message):
        file = open(filename, "w")
        file.write(message)

    def read_to_file(self, filename):
        file = open(filename)
        return file.read()
    
manager = FileManager()
message = input("Please Enter the text you want to write: ")
manager.write_to_file("fileio.txt", message)
print(manager.read_to_file("fileio.txt"))