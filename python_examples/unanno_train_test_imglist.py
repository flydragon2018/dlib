import json
import xmltodict

import os
import glob 

import re 

 
 

# 1. preprocessed  train_test imglist, annotation imglist  txt files
# 2. get the unannotated imagelist
# 3. based on the unannotated imagelist, to remove unannotated images from train/test xml
# 4. then merge original face with annotated neck to train/test xml 

'''
# opening the file in read mode
my_file = open("file1.txt", "r")
  
# reading the file
data = my_file.read()
  
# replacing end of line('/n') with ' ' and
# splitting the text it further when '.' is seen.
data_into_list = data.replace('\n', ' ').split(".")
  
# printing the data
print(data_into_list)
my_file.close()
'''

anno= open("annotation_imgs.txt", "r")

train= open("train_imgs.txt", "r")

test= open("test_imgs.txt", "r")
  
# reading the file
'''
anno_data = anno.read()
train_data = train.read()
test_data = test.read()
'''

#readlines into list directly
anno_data = anno.readlines()
train_data = train.readlines()
test_data = test.readlines()


# replacing end of line('/n') with ',' and
# splitting the text it further when '.' is seen.
#anno_list = anno_data.replace('\n', ' ') 
#train_list = train_data.replace('\n', ' ') 
#test_list = test_data.replace('\n', ' ') 

 
 

#print(anno_list)
#print(train_list)
#print(test_list)

# printing the data
#print(data_list)


#remove unannotated imgs from train/test
def intersection_set(lst1, lst2):
    return list(set(lst1) & set(lst2))

def intersection_loop(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3

print(len(train_data),len(test_data),len(anno_data))


# notice:  original xml imgfile info without leading ./
#          the annotated imgfile with them
# so need to  process anno_data here to be consistent 


new_anno_data=[]
for d in anno_data:
    print(d)
    s=d[2:]
    print(s)
    new_anno_data.append(s)





anno_train_list=intersection_loop(new_anno_data,train_data)

anno_test_list=intersection_loop(new_anno_data,test_data)

print(len(anno_train_list),len(anno_test_list))

unanno_train_list=list(set(train_data) -set(anno_train_list))  
unanno_test_list=list(set(test_data) - set(anno_test_list))  

print(len(train_data),len(test_data))
print(len(unanno_train_list),len(unanno_test_list))
 
#save result
with open('anno_train_imgs.txt', 'w') as f:
    for img_str in anno_train_list:

        #print(img_str)

        f.write(f"{img_str}")

with open('anno_test_imgs.txt', 'w') as f:
    for img_str in anno_test_list:
        #print(img_str)
        f.write(f"{img_str}")


#save result
with open('unanno_train_imgs.txt', 'w') as f:
    for img_str in unanno_train_list:

        #print(img_str)

        f.write(f"{img_str}")

with open('unanno_test_imgs.txt', 'w') as f:
    for img_str in unanno_test_list:
        #print(img_str)
        f.write(f"{img_str}")



#print(len(anno_train_list),len(anno_test_list))
 
 

anno.close()
train.close()
test.close()