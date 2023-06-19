

import xml.etree.ElementTree as ET
from xml.etree.ElementTree import tostring
 
root = ET.parse('neck_5_train.xml')
print(root) 

tree=ET.parse('neck_5_train.xml')
tree = tree.getroot()
t = tostring(tree)
t = t.lower()
tree= ET.fromstring(t)

print(tree)

print(tree.attrib)

for imgs in root.findall('/images'):
    print(imgs.attrib)
    print(imgs.keys())

for img in root.findall('//image'):
    print(img.attrib)
    print(type(img.attrib))
    print(img.keys())
    print(img.items())