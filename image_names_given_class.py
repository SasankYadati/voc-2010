
# coding: utf-8

# In[24]:


path_to_text = 'VOCdevkit/VOC2010/ImageSets/Main/' # path to the labels for different classes
path_to_images = 'VOCdevkit/VOC2010/JPEGImages/' # path to the images
files_classification = list()
files_classification.append('aeroplane')
files_classification.append('bicycle')
files_classification.append('bird')
files_classification.append('boat')
files_classification.append('bottle')
files_classification.append('bus')
files_classification.append('car')
files_classification.append('cat')
files_classification.append('chair')
files_classification.append('cow')
files_classification.append('diningtable')
files_classification.append('dog')
files_classification.append('horse')
files_classification.append('motorbike')
files_classification.append('person')
files_classification.append('pottedplant')
files_classification.append('sheep')
files_classification.append('sofa')
files_classification.append('train')
files_classification.append('tvmonitor')
files_classification = [x+'_trainval.txt' for x in files_classification]


# In[25]:


len(files_classification)


# In[26]:


def get_images_for_class(classname):
    images = list()
    with open(classname+'_trainval.txt', 'r') as f:
        content = f.read()
        content = content.split('\n')
        for img in content:
            img_name = img
            #print(img_name[12:])
            if img_name[12:] == ' 1':
                #print(img_name)
                images.append(img_name)
    images = [x[:11] for x in images]
    images = [x+'.jpg' for x in images]
    return images


# In[27]:

if __name__ == '_main__':
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

