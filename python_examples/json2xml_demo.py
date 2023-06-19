import json
import xmltodict

jn="261068_1.json"
xn="261068_1.xml"
file=open(jn,"r")
python_dict=json.load(file)

'''
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

for k,v in python_dict.items():
    print(k)

xml_file=open(xn,"w")
xmltodict.unparse(python_dict,output=xml_file,full_document=False)
xml_file.close()