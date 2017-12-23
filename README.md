# voc-2010
Classification, Detection on VOC2010
<br>
This project is done as a part of AI Hackathon 2017, PES University.
<br>

We've written helper functions in classes_with_objects.py, confusion_matrix.py, annotate.py, image_names_given_class.py and create_class_directories.py
# Task 1 : Classification
Our objective now is to classify an image into one of given 20 classes.

## Our Architecture :<br>
CONV_LAYER<br>
______________
CONV_LAYER<br>
POOLING<br><br>
______________
CONV_LAYER<br>
______________
CONV_LAYER<br>
POOLING<br><br>
______________
CONV_LAYER<br>
______________
DENSE_LAYER<br>
______________
DENSE_LAYER<br>
______________
DENSE_LAYER(O/P Layer)<br>

We trained the above model on roughly about 14,000 images across 20 classes. We were able to achieve ~ 64% accuracy. We saved the weights to enable future predictions on new images. We also wrote code to compute different metrics confusion matrix.<br>


# Task 2 : Detection
To perform detection, we are using a pre trained model that uses MoblieNet and SingleShotDetection (by Google). This model is finetuned on VOC dataset. The advantage of SSD is that is lightweight and resource efficient. Of course, this comes at the cost of accuracy.

PEACE AMONG THE WORLDS. \/  
