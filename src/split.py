import time
import os
import xml.etree.ElementTree as ET
import subprocess

Categories = ["monster","item","class","race","spell","background","feat"]

file_idx = 0
file_dict = {}
for x in os.listdir():
    if x.endswith(".xml"):
        # Prints only text file present in My Folder
        file_dict[file_idx] = x
        print(file_idx, " ", x)
        file_idx += 1

if file_idx == 1:
    #print("Found ", file_dict.get(int(source_xml)).rstrip(), " in the current directory.")
    print("Found ", file_dict[0].rstrip(), " in the current directory.")
    source_xml = file_dict[0]
else:
    select_xml = input("Select the number of the source XML file:  ")
    source_xml = file_dict[select_xml]

#xml_file = file_dict[0].rstrip()
Tree = ET.parse(source_xml)

def select_dir(_node):
    if _node == "monster":
        _dir = "Monsters"
    elif _node == "item":
        _dir = "Items"
    elif _node == "class":
        _dir = "Classes"
    elif _node == "race":
        _dir = "Races"
    elif _node == "spell":
        _dir = "Spells"
    elif _node == "background":
        _dir = "Backgrounds"
    elif _node == "feat":
        _dir = "Feats"

    return _dir


def xml_split(_node, _tree, _dir):
#    node = _node
    root = _tree.getroot()

    for item in root.findall(_node):
        _name = item.find('name').text
        _name = _name.replace("/", "-")
#        print(_node," --> ",_dir," --> ",_name)
        if not os.path.exists(_dir):
            os.makedirs(_dir)
        with open(_dir + '/' + _name + '.xml', 'wb') as f:
            ET.ElementTree(item).write(f)
#        with open('catalog.txt', 'wb') as c:
        catalog = open("catalog.txt", "w")
        catalog.write(_dir + '/' + _name + ".xml\n")
        catalog.close

            


for Cat in Categories:
    Dir = select_dir(Cat)
    xml_split(Cat, Tree, Dir)
