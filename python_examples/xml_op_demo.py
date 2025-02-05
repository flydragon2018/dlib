

import xml.etree.ElementTree as ET

# build a tree structure
root = ET.Element("html")

head = ET.SubElement(root, "head")

title = ET.SubElement(head, "title")
title.text = "Page Title"

body = ET.SubElement(root, "body")
body.set("bgcolor", "#ffffff")

body.text = "Hello, World!"

# wrap it in an ElementTree instance, and save as XML
tree = ET.ElementTree(root)
tree.write("page.xhtml")

elem =ET.Element("tag")
elem.attrib["first"] = "1"
elem.attrib["second"] = "2"

print(elem.attrib)
print(elem.keys())

print(elem.items())