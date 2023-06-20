from xml.dom.minidom import parse
import os
import pandas as pd

import xml.etree.ElementTree as ET

'''
dataset
   images
      image
           box
           part
           part

<images>
  <image file='lfpw/trainset/image_0457.png' width='350' height='464'>
<box top='78' left='74' width='138' height='196'>
      <part name='00' x='55' y='141'/>
      <part name='01' x='59' y='161'/>

Use ElementTree lib to pull out the child nodes. This might help you.

import xml.etree.ElementTree as ET
tree = ET.parse("file.xml")
root = tree.getroot()
for child in root:
  print({x.tag for x in root.findall(child.tag+"/*")})

x.parentNode.removeChild(x);

'''

def etree_to_dict(t):
    if type(t) is ET.ElementTree: return etree_to_dict(t.getroot())
    return {
        **t.attrib,
        'text': t.text,
        **{e.tag: etree_to_dict(e) for e in t}
    }

def nested_dict_pairs_iterator(dict_obj):
    ''' This function accepts a nested dictionary as argument
        and iterate over all values of nested dictionaries
    '''
    # Iterate over all key-value pairs of dict argument
    for key, value in dict_obj.items():
        # Check if value is of dict type
        if isinstance(value, dict):
            # If value is dict then iterate over all its values
            for pair in  nested_dict_pairs_iterator(value):
                yield (key, *pair)
        else:
            # If value is not dict type then yield the value
            yield (key, value)

#root_dict = etree_to_dict(myet.root)
#for pair in nested_dict_pairs_iterator(root_dict):
#   print(pair)





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



tree=ET.parse('box_train619.xml')
root=tree.getroot()

print(root.tag)
print(root.attrib)

for elem in tree.iter():
    print(elem.tag, elem.text)

#only first level child.
for child in root:
    print(child.tag, child.attrib)
 
 


    
    '''
    if child.tag=='image':
        imgfile = child.getAttributeNode('file')
        print(imgfile)
        
        if imgfile not in new_anno_data:
            print("not annotated, removing\n")
            child.parentNode.removeChild(child)

        '''
     
#xmltowrite = ET.tostring(root)
# bytes type


# str type
#print(xmltowrite)
xmltowrite = ET.tostring(root).decode("Utf-8")
with open('unanno_removed_train.xml', 'w') as j:
    j.write(xmltowrite) 

#save result


#all_elem=[elem.tag for elem in root.iter()]

#print(all_elem[:100])

#printing all in string
#print(ET.tostring(root, encoding='utf8').decode('utf8'))


'''
You can expand the use of the iter() function to help with finding particular elements of interest. 
root.iter() will list all subelements under the root that match the element specified. 
Here, you will list all attributes of the movie element in the tree:
 

for image in root.iter('image'):
    print(image.attrib)
     

for box in root.iter('box'):
    print(box.attrib)




 
dir_path = os.path.dirname(os.path.realpath(__file__))

data_records = []

with parse(f'{dir_path}/box_train619.xml') as xml_doc:


    root = xml_doc.documentElement
    
    images = root.getElementsByTagName('image')

    for img in images:
        

        data = {}
        file_node = img.getAttributeNode('file')
        data['file'] = file_node.value
        width_node = img.getAttributeNode('width')
        data['width'] = width_node.value
        height_node = img.getAttributeNode('height')
        data['height'] = height_node.value

        #box_node=img.getElementsByTagName('box')
        #print(box_node)
      
        btop=box_node.getAttributeNode('top')
        data['box_top']=btop.value
        bleft=box_node.getAttributeNode('left')
        data['box_left']=bleft.value
        bwidth=box_node.getAttributeNode('width')
        data['box_width']=bwidth.value
        bheight=box_node.getAttributeNode('height')
        data['box_height']=bheight.value
     


 
        data_records.append(data)
print(data_records)
df = pd.DataFrame(data_records)
print(df)

df.to_csv("box_train619.csv",index=False)



with open(f"{dir_path}/test_new.xml", "w") as new_xml_handle:
    with parse(f'{dir_path}/test.xml') as xml_doc:
        root = xml_doc.documentElement
        records = root.getElementsByTagName('record')

        for r in records:
            r.setAttribute('testAttr', 'New Attribute')
        xml_doc.writexml(new_xml_handle)

'''