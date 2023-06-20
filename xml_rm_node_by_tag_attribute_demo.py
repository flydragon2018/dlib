from xml.etree import ElementTree as ET

xml = """<groups>
<group>
    <group_components>
        <id item="1">14742</id>
        <id item="1">121727</id>
        <id item="0">541971</id>
    </group_components>
    </group>
<group>
    <group_components>
        <id item="1">10186</id>
        <id item="1">10553</id>
        <id item="1">10644</id>
        <id item="0">434639</id>
    </group_components>
</group>
</groups>
"""
root = ET.fromstring(xml)
for grp_comp in root.findall('.//group_components'):
    for _id in list(grp_comp):
        if _id.attrib['item'] == "1":
            grp_comp.remove(_id)
ET.dump(root)

# create a new XML file with the results
mydata = ET.tostring(root) 
myfile = open("removed_node_by_tagattribute_demo.xml", "w",encoding='utf-8')
# write() argument must be str, not bytes

myfile.write(mydata.decode('utf-8'))