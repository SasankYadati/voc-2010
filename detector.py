import os
import glob
def detect(class_name, images):
    for img in images:
        os.system("python deep_learning_object_detection.py	--prototxt MobileNetSSD_deploy.prototxt.txt	--model MobileNetSSD_deploy.caffemodel --image " + img)

if __name__=='__main__':
    choice = 'dog'
    while(choice!="EXIT"):
        choice = input("Enter class name : ")
        class_images = glob.glob("images/" + choice + '/' + "*.jpg")
        detect(choice, class_images)
