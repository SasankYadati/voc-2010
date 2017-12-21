
# coding: utf-8

# In[15]:


from shutil import copy2
from image_names_given_class import get_images_for_class


# In[16]:


path_to_images = 'VOCdevkit/VOC2010/JPEGImages/'
path_to_text = 'VOCdevkit/VOC2010/ImageSets/Main/' # path to the labels for different classes
aeroplane_images = get_images_for_class(path_to_text+'aeroplane')
bicycle_images = get_images_for_class(path_to_text+'bicycle')
bird_images = get_images_for_class(path_to_text+'bird')
boat_images = get_images_for_class(path_to_text+'boat')
bottle_images = get_images_for_class(path_to_text+'bottle')
bus_images = get_images_for_class(path_to_text+'bus')
car_images = get_images_for_class(path_to_text+'car')
cat_images = get_images_for_class(path_to_text+'cat')
chair_images = get_images_for_class(path_to_text+'chair')
cow_images = get_images_for_class(path_to_text+'cow')
diningtable_images = get_images_for_class(path_to_text+'diningtable')
dog_images = get_images_for_class(path_to_text+'dog')
horse_images = get_images_for_class(path_to_text+'horse')
motorbike_images = get_images_for_class(path_to_text+'motorbike')
person_images = get_images_for_class(path_to_text+'person')
pottedplant_images = get_images_for_class(path_to_text+'pottedplant')
sheep_images = get_images_for_class(path_to_text+'sheep')
sofa_images = get_images_for_class(path_to_text+'sofa')
train_images = get_images_for_class(path_to_text+'train')
tvmonitor_images = get_images_for_class(path_to_text+'tvmonitor')


# In[22]:


def create_class_images(class_name):
    '''
    has daddy issues
    may or may not perform reliably
    '''
    
    src = 'VOCdevkit/VOC2010/JPEGImages/'
    class_imgs = get_images_for_class(path_to_text+class_name)
    
    dest = 'VOCdevkit/VOC2010/JPEGImages2/'+class_name

    for img in class_imgs:
        copy2(src+img,dest)
    
    


# In[23]:


create_class_images('aeroplane')


# In[24]:


create_class_images('bicycle')
create_class_images('bird')
create_class_images('boat')
create_class_images('bottle')
create_class_images('bus')
create_class_images('car')
create_class_images('cat')
create_class_images('chair')
create_class_images('cow')
create_class_images('diningtable')
create_class_images('dog')
create_class_images('horse')
create_class_images('motorbike')
create_class_images('person')
create_class_images('pottedplant')
create_class_images('sheep')
create_class_images('sofa')
create_class_images('train')
create_class_images('tvmonitor')

