
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
#remove leadind ./
anno_imgs=[ x.strip('\n')[2:] for x in anno_all_data]

 

print(len(anno_imgs))
print(anno_imgs[:10])
 
 
def data_from_json(anno_file):
    # shapes:labels aboutt neck points and bbox,  imagePath: image filename
    f=open(anno_file)
    data=json.load(f)
    bbox=[]
    neck=[]
    cnt=0
    for i in data:
        #print(i)
       
        #labels: face box lefttop/rightdown,  neck points
        if i=='shapes':
            for s in data[i]:
                print(s)
                if s['label']=='box':
                    if len(s['points'])<2:
                        print("!!!!!!!!!!!!!!!!")
                        print("wrong annotation")
                        cnt+=1
                    else:

                        label='box'
                        x,y=s['points'][0]
                        xx,yy=s['points'][1]
                        left=x
                        top=y
                        width=xx-x
                        height=yy-y
                        print(label,left,top,width,height)
                        bbox.append([label,left,top,int(width),int(height)])
                else:
                    label='part'
                    name=s['label']
                    x,y=s['points'][0]
                    print(label,name, x,y)
                    neck.append([label,name, int(x),int(y)])



        if i=='imagePath':
            imgname=data[i]
            print(f"\nimage path: {imgname}")
     
    f.close()
    return bbox, neck, imgname, cnt




'''
#root 
dataset
       images
             image
                  box
                     part
                     part
                     ///
                  box
             image

             #
             #
             #

        images
dataset
                      

'''

#tree = ET.parse('300w_test.xml')
#tree = ET.parse('anno_train.xml')

tree = ET.parse('300w_test.xml')
root = tree.getroot()


neck_root=ET.Element("dataset")

count=0

wrong_anno=0

wrong_files=[]

# root  dataset
# child  images
# gchild  image 
# ggchild box
# gggchild part

for child in root:
    print("111")
    print(child.tag, child.attrib)
    elem=ET.SubElement(neck_root,child.tag)
    for a in child.attrib:
        elem.set(a)
    
    #only "images" node has child nodes "image"
    for gchild in child:
        print("222")
        print(gchild.tag,gchild.attrib)
        #g_elem=ET.SubElement(elem,gchild.tag)
        
        #get attribute
        fn=gchild.get('file')
        print(fn)
        #flag= fn in anno_all_data 

        flag= fn in anno_imgs
 
        print(flag)
        
        p1=fn.rindex('/')
        p2=fn.rindex('.')
        js_fn= fn[:p2] +'.json'

        print(js_fn)
         
        if flag:

            bbox,neck, imgname,wrong_n=data_from_json(js_fn)
            print("annotation ")
            print(wrong_n)
            if wrong_n:
                wrong_anno+=1
                wrong_files.append([fn,js_fn])
            count+=1
            print("image is annotated.\n")
            g_elem=ET.SubElement(elem,gchild.tag)
            # first box node
            # change the box data by annoated data 
            




            #add image attribute 
            for k,v in gchild.attrib.items():
                print(k,v)
                g_elem.set(k,v)
          

            
            for ggchild in gchild:
                print("333")
                print(ggchild.tag,ggchild.attrib)

                #box node
                gg_elem=ET.SubElement(g_elem,ggchild.tag)

                #add box attributes 
                    
                for k,v in ggchild.attrib.items():
                    print(k,v)
                    gg_elem.set(k,v)

                    '''  
                    for part in neck:
                        p,num,x,y =part
                        # new tags all "part" 
                        gg_elem=ET.SubElement(g_elem,ggchild.tag)
                        part_dict={"name": num, "x": x ,"y": y}
                        gg_elem.set("name",num) 
                        gg_elem.set("x",x) 
                        gg_elem.set("y",y)  
                    ''' 




                #update box if annotated
                if len(bbox)==1:
                    print(bbox) 

                       
                    label,left_v,top_v,width_v,height_v=bbox[0]
                    box_dict={"top":str(int(top_v)),"left":str(int(left_v)),"width":str(width_v), "height":str(height_v)}

                    #notice  attribute values should be str type, otherwise, serialization error.

                    for k,v in box_dict.items():
                        print(k,v)
                        gg_elem.set(k,v) 
                        

                
                # add parts 0-67
                for gggchild in ggchild:
                    print("444")
                    print(gggchild.tag,gggchild.attrib)
                        
                    print(type(gggchild.tag))
                    ggg_elem=ET.SubElement(gg_elem,gggchild.tag)

                    for k,v in gggchild.attrib.items():
                        print(k,v)
                        ggg_elem.set(k,v)
                   
                
                # add the neck points 101-135
                for part in neck:
                    p,num,x,y =part
                    # new tags all "part" 
                    ggg_elem=ET.SubElement(gg_elem,p)
                    part_dict={"name": str(num), "x": str(x) ,"y": str(y)}

                    for k,v in part_dict.items():
                        print(k,v)
                        ggg_elem.set(k,v)
                







print("wrong anno:", wrong_anno)
print(wrong_files)
print(count)
 

from xml.dom import minidom

xmlstr = minidom.parseString(ET.tostring(neck_root)).toprettyxml(indent="   ")

##xmlstr = ET.tostring(neck_root)

#b_xml = ET.tostring(root3)
 
# Opening a file under the name `items2.xml`,
# with operation mode `wb` (write + binary)
 
#with open("faceneck_anno_train.xml", "w") as f:
with open("faceneck_anno_test.xml", "w") as f:
    #f.write(b_xml.decode('utf-8'))
    f.write(xmlstr)

 