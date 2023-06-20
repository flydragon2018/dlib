import xml.etree.ElementTree as etree


#lib.xml 
'''
<root>
  <tag_folders>
    <folder id="1">Stars</folder>
    <folder id="2">Planet</folder>
    <folder id="3">Satellite</folder>
  </tag_folders>
  <tags>
    <tag>
      <name>Earth</name>
    </tag>
    <tag id="2">
      <name>Sun</name>
    </tag>
    <tag id="29">
      <name>Moon</name>
    </tag>
  </tags>
</root>



def remove_tag(root, tag_id_r):
    tags_elem = root.find("tags")
    target_tag = tags_elem.find(f"tag[@id='{tag_id_r}']")
    if target_tag:
        tags_elem.remove(target_tag)
    else:
        print(f"A tag with the id \"{tag_id_r}\" cannot be found.")


def main():
    tree = etree.parse("lib.xml")
    root = tree.getroot()

    remove_tag(root, input("What is the id of the tag you want to remove? "))

    # Overwriting the input file. Are you sure that's a good idea?
    tree.write("lib.xml", encoding="utf-8")

elems = """<?xml version="1.0" ?>
<root>
  <tag_folders>
    <folder id="1">Stars</folder>
    <folder id="2">Planet</folder>
    <folder id="3">Satellite</folder>
  </tag_folders>
  <tags>
    <tag>
      <name>Earth</name>
    </tag>
    <tag id="2">
      <name>Sun</name>
    </tag>
    <tag id="29">
      <name>Moon</name>
    </tag>
   </tags>
</root>
""" #note that the xml has been fixed

from lxml import etree
doc = etree.XML(elems)
to_del = doc.xpath('//name["Moon"]/parent::tag[@id="29"]')
for td in to_del:
    td.getparent().remove(td)    
print(etree.tostring(doc, pretty_print=True, xml_declaration=True).decode())

'''