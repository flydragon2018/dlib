# Python program to read
# json file
  
  
import json


'''

SON OBJECT	PYTHON OBJECT
object	dict
array	list
string	str
null	None
number (int)	int
number (real)	float
true	True
false	False
'''

  
# Opening JSON file
f = open('anno_data/afw/261068_1.json')
  
# returns JSON object as 
# a dictionary
data = json.load(f)
  
# Iterating through the json
# list
for i in data:
    print(i)
    
    #labels: face box lefttop/rightdown,  neck points
    if i=='shapes':
        for s in data[i]:
            print(s)
            if s['label']=='box':
                label='box'
                x,y=s['points'][0]
                xx,yy=s['points'][1]
                left=x
                top=y
                width=xx-x
                height=yy-y
                print(label,left,top,width,height)
            else:
                label='part'
                name=s['label']
                x,y=s['points'][0]
                print(label,name, x,y)



    if i=='imagePath':
        p=data[i]
        print(f"\nimage path: :{p}")
         
# Closing file
f.close()