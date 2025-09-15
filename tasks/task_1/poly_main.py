from poly_class import Directory, File

dir_0 = Directory("dir_0")

file_1 = File("file_1", 1)
file_2 = File("file_2", 1)
dir_0.add(file_1)
dir_0.add(file_2)

dir_1 = Directory("dir_1")
file_3 = File("file_3", 1)
file_4 = File("file_4", 1)
dir_1.add(file_3)
dir_1.add(file_4)

dir_1_1 = Directory("dir_1_1")
file_5 = File("file_5", 1)
dir_1_1.add(file_5)
dir_1.add(dir_1_1)

dir_0.add(dir_1)
# dir_0.display()

dir_0.display()
print(dir_1.get_size())