import xml.etree.ElementTree as etree

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



 


def remove_tag(root, tag_id_r):
    tags_elem = root.find("tags")
    target_tag = tags_elem.find(f"tag[@id='{tag_id_r}']")
    if target_tag:
        tags_elem.remove(target_tag)
    else:
        print(f"A tag with the id \"{tag_id_r}\" cannot be found.")


def main():
    tree = etree.parse("remove_demo.xml")
    root = tree.getroot()

    remove_tag(root, input("What is the id of the tag you want to remove? "))

    # Overwriting the input file. Are you sure that's a good idea?
    tree.write("removed_demo.xml", encoding="utf-8")


'''
path1="./afw/*.json"

path2="./*/*/*.json"

res1 = glob.glob(path1)

res2=glob.glob(path2)

res=res1+res2
print(len(res1),len(res2),len(res))


#main()
'''


