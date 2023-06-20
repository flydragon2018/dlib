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

'''
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
'''

anno= open("annotation_imgs.txt", "r")

anno_train= open("anno_train_imgs.txt", "r")

anno_test= open("anno_test_imgs.txt", "r")

#readlines into list directly
anno_data = anno.readlines()
train_data = anno_train.readlines()
test_data = anno_test.readlines()

new_anno_data=[]
for d in anno_data:
    #print(d)
    s=d[2:]
    #print(s)
    new_anno_data.append(s)

print(new_anno_data)


tree = ET.parse('box_train619.xml')
root = tree.getroot()

#tree level by '/'
# dataset/images/image/box
#                       part

cnt=0
 

for img in root.findall('.//image'):
    cnt+=1
   
    #print(img.attrib)
    
    f=img.attrib['file'] 
    print(f)
     
    for k in new_anno_data:
        kk=str(k).strip('\n')
        #print('\n')
        #print(k)
        if str(kk)==str(f):
            print(k,f)
            img.remove(img)
            print("node removed! \n")
    
    #for img in imgs:
    #    print(img.attrib)
        #if img.attrib['file'] in new_anno_data:
        #    imgs.remove(img)
    
    #if cnt==1:
    #   break
     
 

#ET.dump(root)


 
mydata = ET.tostring(root) 
myfile = open("removed_anno_train.xml", "w",encoding='utf-8')
# write() argument must be str, not bytes

myfile.write(mydata.decode('utf-8'))
 



anno.close()
anno_train.close()
anno_test.close()
