

import xml.etree.ElementTree as ET
from xml.etree.ElementTree import tostring
 
root = ET.parse('box_train619.xml')
print(root) 

tree=ET.parse('box_train619.xml')
tree = tree.getroot()
t = tostring(tree)
t = t.lower()
tree= ET.fromstring(t)

print(tree)

print(tree.attrib)

for imgs in root.findall('/images'):
    print(imgs.attrib)
    print(imgs.keys())

imglist=[]
for img in root.findall('//image'):
    print(img.attrib)
    print(type(img.attrib))
    print(img.keys())
    print(img.items())

    for k,v in img.items():
        if k=='file':
            imglist.append(v)


with open('train_imgs.txt', 'w') as f:
    for img in imglist:
        f.write(f"{img}\n")


test_root = ET.parse('box_test619.xml')

for imgs in test_root.findall('/images'):
    print(imgs.attrib)
    print(imgs.keys())

test_imglist=[]
for img in test_root.findall('//image'):
    print(img.attrib)
    print(type(img.attrib))
    print(img.keys())
    print(img.items())

    for k,v in img.items():
        if k=='file':
            test_imglist.append(v)


with open('test_imgs.txt', 'w') as f:
    for img in test_imglist:
        f.write(f"{img}\n")