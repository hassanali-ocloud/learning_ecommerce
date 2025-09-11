import xml.dom.minidom

domtree = xml.dom.minidom.parse("10_XmlData.xml")
group = domtree.documentElement

animals = group.getElementsByTagName("animal")

for animal in animals:
    print("Animal")
    if animal.hasAttribute("id"):
        print(f"Id: {animal.getAttribute("id")}")

newAnimal = domtree.createElement("animal")
newAnimal.setAttribute("id", "6")

name = domtree.createElement("name")
name.appendChild(domtree.createTextNode("Sparrow"))

category = domtree.createElement("category")
category.appendChild(domtree.createTextNode("Bird"))

weight = domtree.createElement("weight")
weight.appendChild(domtree.createTextNode("10"))

newAnimal.appendChild(name)
newAnimal.appendChild(category)
newAnimal.appendChild(weight)

group.appendChild(newAnimal)

animals = group.getElementsByTagName("animal")

domtree.writexml(open("10_XmlData.xml", "w"))
    