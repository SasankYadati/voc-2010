from shutil import copy2
from xml.dom.minidom import parseString
import xml.etree.ElementTree as ET
import os

count=0
def create_class_images(class_name,final_name):
    src = 'VOCdevkit_2/VOC2010/JPEGImages/'
    dest = 'VOCdevkit_2/VOC2010/JPEGImages3/'+class_name
    copy2(src+final_name+'.jpg',dest)
      
x=os.listdir("VOCdevkit_2/VOC2010/Annotations")
len_x=len(x)

for i in range(len_x):
    anote = "VOCdevkit_2/VOC2010/Annotations/"
    tree = ET.parse(anote+x[i])
    root = tree.getroot()
    
    file = open(anote+x[i],'r')

    data = file.read()
    file.close()
    dom = parseString(data)

    #print(x[2323])
    #print(x[i])
    object_number=len(dom.getElementsByTagName('object'))
    x[i]=x[i][:-4]
    if(object_number==1):
        count=count+1
        for object in root.iter('object'):
            obj_children=object.getchildren()
            for child in obj_children:
                if(child.tag=='name'):
                    classname=child.text

        create_class_images(classname,x[i])
    
print(count)
