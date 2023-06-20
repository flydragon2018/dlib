import xml.etree.ElementTree as etree

import json
import xmltodict

import os
import glob 

import re 

 
import xml.dom.minidom

import sys, xml.etree.ElementTree as ET



'''
# country_data.xml
<?xml version="1.0"?>
<data>
    <country name="Liechtenstein">
        <rank>1</rank>
        <year>2008</year>
        <gdppc>141100</gdppc>
        <neighbor name="Austria" direction="E"/>
        <neighbor name="Switzerland" direction="W"/>
    </country>
    <country name="Singapore">
        <rank>4</rank>
        <year>2011</year>
        <gdppc>59900</gdppc>
        <neighbor name="Malaysia" direction="N"/>
    </country>
    <country name="Panama">
        <rank>68</rank>
        <year>2011</year>
        <gdppc>13600</gdppc>
        <neighbor name="Costa Rica" direction="W"/>
        <neighbor name="Colombia" direction="E"/>
    </country>
</data>
'''

'''


import xml.etree.ElementTree as ET
tree = ET.parse('country_data.xml')
root = tree.getroot()

#root = ET.fromstring(country_data_as_string)

print(root.tag,root.attrib)
 
for child in root:
    print(child.tag, child.attrib)


#hildren are nested, and we can access specific child nodes by index:

root[0][1].text

#Element has some useful methods that help iterate recursively over all the sub-tree below it (its children, their children, and so on).
# For example, Element.iter():

for neighbor in root.iter('neighbor'):
    print(neighbor.attrib)

#Element.findall() finds only elements with a tag which are direct children of the current element.
# Element.find() finds the first child with a particular tag, 
# and Element.text accesses the element’s text content.
# Element.get() accesses the element’s attributes:


for country in root.findall('country'):
    rank = country.find('rank').text
    name = country.get('name')
    print(name, rank)

Liechtenstein 1
Singapore 4
Panama 68


ElementTree provides a simple way to build XML documents and write them to files. 
The ElementTree.write() method serves this purpose.

Once created, an Element object may be manipulated by directly changing its fields (such as Element.text), 
adding and modifying attributes (Element.set() method),
 as well as adding new children (for example with Element.append()).

for rank in root.iter('rank'):
    new_rank = int(rank.text) + 1
    rank.text = str(new_rank)
    rank.set('updated', 'yes')

tree.write('output.xml')

We can remove elements using Element.remove(). Let’s say we want to remove all countries with a rank higher than 50:

>>>
for country in root.findall('country'):
    # using root.findall() to avoid removal during traversal
    rank = int(country.find('rank').text)
    if rank > 50:
        root.remove(country)

tree.write('output.xml')

The SubElement() function also provides a convenient way to create new sub-elements for a given element:

>>>
a = ET.Element('a')
b = ET.SubElement(a, 'b')
c = ET.SubElement(a, 'c')
d = ET.SubElement(c, 'd')
ET.dump(a)
<a><b /><c><d /></c></a>


XPath support
This module provides limited support for XPath expressions for locating elements in a tree. 
The goal is to support a small subset of the abbreviated syntax; a full XPath engine is outside the scope of the module.

Example
Here’s an example that demonstrates some of the XPath capabilities of the module. 
We’ll be using the countrydata XML document from the Parsing XML section:

import xml.etree.ElementTree as ET

root = ET.fromstring(countrydata)

# Top-level elements
root.findall(".")

# All 'neighbor' grand-children of 'country' children of the top-level
# elements
root.findall("./country/neighbor")

# Nodes with name='Singapore' that have a 'year' child
root.findall(".//year/..[@name='Singapore']")

# 'year' nodes that are children of nodes with name='Singapore'
root.findall(".//*[@name='Singapore']/year")

# All 'neighbor' nodes that are the second child of their parent
root.findall(".//neighbor[2]")


Supported XPath syntax
Syntax

Meaning

tag

Selects all child elements with the given tag. For example, spam selects all child elements named spam, and spam/egg selects all grandchildren named egg in all children named spam. {namespace}* selects all tags in the given namespace, {*}spam selects tags named spam in any (or no) namespace, and {}* only selects tags that are not in a namespace.

Changed in version 3.8: Support for star-wildcards was added.

*

Selects all child elements, including comments and processing instructions. For example, */egg selects all grandchildren named egg.

.

Selects the current node. This is mostly useful at the beginning of the path, to indicate that it’s a relative path.

//

Selects all subelements, on all levels beneath the current element. For example, .//egg selects all egg elements in the entire tree.

..

Selects the parent element. Returns None if the path attempts to reach the ancestors of the start element (the element find was called on).

[@attrib]

Selects all elements that have the given attribute.

[@attrib='value']

Selects all elements for which the given attribute has the given value. The value cannot contain quotes.

[@attrib!='value']

Selects all elements for which the given attribute does not have the given value. The value cannot contain quotes.

New in version 3.10.

[tag]

Selects all elements that have a child named tag. Only immediate children are supported.

[.='text']

Selects all elements whose complete text content, including descendants, equals the given text.

New in version 3.7.

[.!='text']

Selects all elements whose complete text content, including descendants, does not equal the given text.

New in version 3.10.

[tag='text']

Selects all elements that have a child named tag whose complete text content, including descendants, equals the given text.

[tag!='text']

Selects all elements that have a child named tag whose complete text content, including descendants, does not equal the given text.

New in version 3.10.

[position]

Selects all elements that are located at the given position. The position can be either an integer (1 is the first position), the expression last() (for the last position), or a position relative to the last position (e.g. last()-1).

Predicates (expressions within square brackets) must be preceded by a tag name, an asterisk, or another predicate. position predicates must be preceded by a tag name.




'''

 
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



