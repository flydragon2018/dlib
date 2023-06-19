import json
import xmltodict

import os
import glob 

import re 

 
# get all files inside a specific folder
dir_path = r'./'
fns=[]
for path in os.scandir(dir_path):
    if path.is_file():
        #print(path.name)
        fns.append(path.name)

 
res = glob.glob(dir_path)

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
 




'''
jn="261068_1.json"
xn="261068_1.xml"
file=open(jn,"r")
python_dict=json.load(file)


version
flags
shapes

"shapes": [
    {
      "label": "101",
      "points": [
        [
          418.54237288135596,
          234.3220338983051
        ]
      ],
      "group_id": null,
      "description": "",
      "shape_type": "point",
      "flags": {}
    },
    ...
    {
      "label": "box",
      "points": [
        [
          360.96268656716416,
          139.97014925373134
        ],
        [
          568.4253731343284,
          323.55223880597015
        ]
      ],
      "group_id": null,
      "description": "",
      "shape_type": "rectangle",
      "flags": {}
    }
    ]


imagePath: image_filename
imageData
imageHeight
imageWidth
'''

# info needed:  imagePath,  labels of Number and box in shapes.


dir_path = r'./afw/*.json'

 

res = glob.glob(dir_path)

for f in res:
    print(f)
    print(type(f))
    p=f.rindex('/')

    xn=f[p+1:-4]+"xml"
    print(xn)
    out_xn=f[:p+1]+xn
    print(out_xn)

    
    jf=open(f,"r")
    
     
    pd=json.load(jf)
    xml_file=open(out_xn,"w")
    xmltodict.unparse(pd,output=xml_file,full_document=False)
    xml_file.close()
    jf.close()
    

dir_path = r'./helen/*/*.json'

res = glob.glob(dir_path)

for f in res:
    print(f)
    print(type(f))
    p=f.rindex('/')

    xn=f[p+1:-4]+"xml"
    print(xn)
    out_xn=f[:p+1]+xn
    print(out_xn)

    
    jf=open(f,"r")
    
     
    pd=json.load(jf)
    xml_file=open(out_xn,"w")
    xmltodict.unparse(pd,output=xml_file,full_document=False)
    xml_file.close()
    jf.close()
         
 
 