
import lxml.etree 
import xml.etree.ElementTree as etree

import json
import xmltodict

import os
import glob 

import re 

import copy
 
import xml.dom.minidom

import sys, xml.etree.ElementTree as ET

tree = ET.parse('box_train619.xml')
root = tree.getroot()

'''
from bs4 import BeautifulSoup
 
# Reading data from the xml file
with open('dict.xml', 'r') as f:
    data = f.read()
 
# Passing the data of the xml
# file to the xml parser of
# beautifulsoup
bs_data = BeautifulSoup(data, 'xml')
 
# A loop for replacing the value
# of attribute `test` to WHAT !!
# The tag is found by the clause
# `bs_data.find_all('child', {'name':'Frank'})`
for tag in bs_data.find_all('child', {'name':'Frank'}):
    tag['test'] = "WHAT !!"
 
 
# Output the contents of the
# modified xml file
print(bs_data.prettify())

import xml.etree.ElementTree as ET
 
# This is the parent (root) tag
# onto which other tags would be
# created
data = ET.Element('chess')
 
# Adding a subtag named `Opening`
# inside our root tag
element1 = ET.SubElement(data, 'Opening')
 
# Adding subtags under the `Opening`
# subtag
s_elem1 = ET.SubElement(element1, 'E4')
s_elem2 = ET.SubElement(element1, 'D4')
 
# Adding attributes to the tags under
# `items`
s_elem1.set('type', 'Accepted')
s_elem2.set('type', 'Declined')
 
# Adding text between the `E4` and `D5`
# subtag
s_elem1.text = "King's Gambit Accepted"
s_elem2.text = "Queen's Gambit Declined"
 
# Converting the xml data to byte object,
# for allowing flushing data to file
# stream
b_xml = ET.tostring(data)
 
# Opening a file under the name `items2.xml`,
# with operation mode `wb` (write + binary)
with open("GFG.xml", "wb") as f:
    f.write(b_xml)

'''


'''
# Find element to copy 
member1 = tree.find("member")

# Create a copy
member2 = copy.deepcopy(member1)

# Append the copy 
root.append(member2)
'''

def remove_tag(root, elem, file_path):
    p_node=elem.parentNode.nodeName
    tags_elem = root.find(p_node)
    target_tag = tags_elem.find(f"{elem}[@file='{file_path}']")
    if target_tag:
        tags_elem.remove(target_tag)
    else:
        print(f"A tag with the file \"{tile_path}\" cannot be found.")



root2=copy.deepcopy(root)

print("original root info:")
print(root.tag,root.attrib)

print("copied root info:")
print(root2.tag,root2.attrib)

print(root[:])
print(root[2][0])

print(root[2][0].tag,root[2][0].attrib)

print("child of image:")
for child in root[2][0]:
    print(child.tag, child.attrib)


''' 
for child in root:
    print(child.tag, child.attrib)
    for u in child:
        print(u.tag,u.attrib)
        for k in u:
            print(k.tag,k.attrib)
            for w in k:
                print(w.tag,w.attrib)
'''
 

# Converting the xml data to byte object,
# for allowing flushing data to file
# stream

# demo remove child nodes 

'''
x = xmlDoc.getElementsByTagName("title")[0];
y = x.childNodes[0];
x.removeChild(y);
''' 


#parentnode remove child node directly,demo 
root2[2].remove(root2[2][0])

'''
dataset
       name
       comment
       images
            image
                 box 
                    part
                    part 
'''

root3=ET.Element("dataset")

# remove batch nodes 
for child in root:
    print(child.tag, child.attrib)
    elem=ET.SubElement(root3,child.tag)
    for a in child.attrib:
        elem.set(a)
    
    for gchild in child:
        print(gchild.tag,gchild.attrib)
        g_elem=ET.SubElement(elem,gchild.tag)

        for k,v in gchild.attrib.items():
            print(k,v)
            g_elem.set(k,v)
        
        for ggchild in gchild:
                print(ggchild.tag,ggchild.attrib)
                gg_elem=ET.SubElement(g_elem,ggchild.tag)

                for k,v in ggchild.attrib.items():
                    print(k,v)
                    gg_elem.set(k,v)
                
                for gggchild in ggchild:
                    print(gggchild.tag,gggchild.attrib)

                    ggg_elem=ET.SubElement(gg_elem,gggchild.tag)

                    for k,v in gggchild.attrib.items():
                        print(k,v)
                        ggg_elem.set(k,v)

from xml.dom import minidom

xmlstr = minidom.parseString(ET.tostring(root3)).toprettyxml(indent="   ")

#b_xml = ET.tostring(root3)
 
# Opening a file under the name `items2.xml`,
# with operation mode `wb` (write + binary)
with open("root3_dataset.xml", "w") as f:
    #f.write(b_xml.decode('utf-8'))
    f.write(xmlstr)

#decode('utf-8')