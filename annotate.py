
# coding: utf-8

# In[66]:


from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Conv3D
from keras.layers import Activation, Dropout, Flatten, Dense

import xml.etree.ElementTree as ET

anote = "VOCdevkit/VOC2010/Annotations/"
tree = ET.parse(anote+"2007_001340.xml")
root = tree.getroot()
filename = root.find('filename').text
width = int(root.find('size').find('width').text)
height = int(root.find('size').find('height').text)
height = int(root.find('size').find('height').text)
depth = 3
oblist= list()

#get object tag and its child
for object in root.iter('object'):
    obj_children=object.getchildren()
    ob = dict()
    for x in obj_children:
        if(x.tag!='bndbox'):
            ob[x.tag]=x.text
        else:
            for y in x.getchildren():
                ob[y.tag]=int(y.text)
    oblist.append(ob)
print(oblist)






