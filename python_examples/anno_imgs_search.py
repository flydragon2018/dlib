
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


anno_all= open("annotation_imgs.txt", "r")

 

#readlines into list directly
 
anno_all_data = anno_all.readlines()

#strip the '\n'
anno_imgs=[ x.strip('\n') for x in anno_all_data]

print(len(anno_all_data))
print(anno_all_data[:10])

print(len(anno_imgs))
print(anno_imgs[:10])
 
 


tree = ET.parse('300w_train.xml')
#tree = ET.parse('300w_test.xml')

root = tree.getroot()

#object type 
xml_imgs=root.findall('.//image')

print(len(xml_imgs))
print(xml_imgs[:10])


count=0
for img in xml_imgs:
    fn=img.get("file")
    print(fn)
    if fn in anno_imgs:
        print('\n\nimg file path matched!\n\n')
        count+=1

print(count)