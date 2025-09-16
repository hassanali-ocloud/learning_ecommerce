from poly_class import Directory, File

d0 = Directory("d0")

f0_0 = File("f0_0", 10)
f0_1 = File("f0_1", 20)
d0.add(f0_0)
d0.add(f0_1)

d1 = Directory("d1")
d0.add(d1)

d2 = Directory("d2")
f2_0 = File("f2_0", 99)
f2_1 = File("f2_1", 11)
f2_2 = File("f2_2", 100)
d2.add(f2_0)
d2.add(f2_1)
d2.add(f2_2)
d0.add(d2)

d1.display()
print(d1.get_size())

# dir0, dir1, dir2
## dir0 f0_0 (10) f_0_1 (20)
## dir1
## dir2 f2_0(99) f2_1(11) f2_2 (100)