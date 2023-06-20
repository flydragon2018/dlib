import json
import xmltodict

import os
import glob 

import re 

 
import xml.dom.minidom

import sys, xml.etree.ElementTree as ET

 
# get all files inside a specific folder
dir_path = r'./'
fns=[]
for path in os.scandir(dir_path):
    if path.is_file():
        #print(path.name)
        fns.append(path.name)

 
res = glob.glob(dir_path)

gfns=[]

for f in glob.glob(dir_path, recursive=True):
    gfns.append(f)


import pathlib

# folder path
dir_path = r'./'

# to store file names
pl_res = []

# construct path object
d = pathlib.Path(dir_path)

# iterate directory
for entry in d.iterdir():
    # check if it a file
    if entry.is_file():
        pl_res.append(entry)
 




'''
jn="261068_1.json"
xn="261068_1.xml"
file=open(jn,"r")
python_dict=json.load(file)


version
flags
shapes

"shapes": [
    {
      "label": "101",
      "points": [
        [
          418.54237288135596,
          234.3220338983051
        ]
      ],
      "group_id": null,
      "description": "",
      "shape_type": "point",
      "flags": {}
    },
    ...
    {
      "label": "box",
      "points": [
        [
          360.96268656716416,
          139.97014925373134
        ],
        [
          568.4253731343284,
          323.55223880597015
        ]
      ],
      "group_id": null,
      "description": "",
      "shape_type": "rectangle",
      "flags": {}
    }
    ]


imagePath: image_filename
imageData
imageHeight
imageWidth
'''

# info needed:  imagePath,  labels of Number and box in shapes.


# two different directory levels
#dir_path = r'./*/*.xml'
#dir_path = r'./*/*/*.xml'

 
def filter_anno_img_xml(in_path, out_path, anno_img_list):
    '''creates a new xml file stored at [out_path] with the desired landmark-points.
    The input xml [in_path] must be structured like the ibug annotation xml.'''
    in_file = open(in_path, "r")
    out = open(out_path, "w")
    
    doc=xml.dom.minidom.parse(in_path)
    
    images=doc.getElementsByTagName("image")

    boxes=doc.getElementsByTagName("box")

    #print(images)
    #print(boxes)

    ''' 
    for line in file.readlines():
        finds = re.findall(REG_PART, line)

        # find the part section
        if len(finds) <= 0:
            out.write(line)
        else:
            # we are inside the part section 
            # so we can find the part name and the landmark x, y coordinates
            name, x, y = re.findall(REG_NUM, line)

            # if is one of the point i'm looking for, write in the output file
            if int(name) in pointSet:
                out.write(f"      <part name='{name}' x='{x}' y='{y}'/>\n")

    out.close()
    '''
     


# keeping the annotated images only for train/test xml first
# then merge together.


#looping  xml file for face and neck data merging

train_labels ="box_train619.xml"
test_labels = "box_test619.xml"

train_face_xml = open(train_labels, "r")
train_faceneck_xml = open("box_train_faceneck619.xml", "w")


test_face_xml = open(test_labels, "r")
test_faceneck_xml = open("box_test_faceneck619.xml", "w")


#pointSet = set(parts)

#pointSet = set(ALL_LANDMARKS)


#The removeChild() method is the only way to remove a specified node.
#x = xmlDoc.getElementsByTagName("book")[0];

#x.parentNode.removeChild(x);

train_doc=xml.dom.minidom.parse(train_face_xml)
    
#images=doc.getElementsByTagName("image")

train_images=train_doc.getElementsByTagName("image")

train_boxes=train_doc.getElementsByTagName("box")


test_doc=xml.dom.minidom.parse(test_face_xml)
    
#images=doc.getElementsByTagName("image")

test_images=test_doc.getElementsByTagName("image")

test_boxes=test_doc.getElementsByTagName("box")



dir_path = r'./helen/*/*.xml'

res = glob.glob(dir_path)

'''
for f in res:
  print(f)
   
    for img in train_images:
        value = img.get(attribute)
        if value:
            print(value)
'''



root = ET.parse("box_train619.xml").getroot()
#iterator = root.getiterator("Item")

print(root)

iterator = root.iter("image")

# Loop using the iterator
# (Please use clear variable names!)
#for item in iterator:
#    print(item)
    # To find a sub-element with a text tag, use find()
    #old_symbol = item.find("image")
    # This is how you get its text field
    #text = old_symbol.text
    # Is 'UPS' in our text field?
    #print(text)


# Counting the instance of Node attribute with findall
NO_node = 0 ;
Name_attribute="30844800_1"
for instance in root.findall('dataset/image'):
    # Checking for the particular Node Attribute
    print(instance.get('value'))
    if Name_attribute in instance.get('name'):
        NO_node+=1;
 
# Printing Number of nodes
print ("total instance of given node attribute is : ", NO_node)


train_face_xml.close()
train_faceneck_xml.close()


test_face_xml.close()
test_faceneck_xml.close()
 

'''
import sys, xml.etree.ElementTree as ET
# Create the root of the ElementTree from file
root = ET.parse("thefile").getroot()
# Get an iterator for the root node
iterator = root.getiterator("Item")
# Loop using the iterator
# (Please use clear variable names!)
for item in iterator:
    # To find a sub-element with a text tag, use find()
    old_symbol = item.find("Symbol")
    # This is how you get its text field
    text = old_symbol.text
    # Is 'UPS' in our text field?
    if 'UPS' in text:
        # If so, remove the sub-element
        # remove() takes out nodes, not text
        item.remove(old_symbol)
        # Add a new sub-element to the item
        new_symbol = ET.SubElement(item, "Symbol")
        # Set its text field to the appropriate thing
        new_symbol.text = text[0:3]+"2009"
# Now get the full tree from the root
tree = ET.ElementTree(root)
# And write to file!
tree.write("out.xml")'
'''