# face color analysis given eye center position

import sys
import os
import numpy as np
import cv2
import argparse
import time
from mtcnn.mtcnn import MTCNN
<<<<<<< HEAD

=======
import imutils
>>>>>>> 8a8112f87734651ff1b98b4acf9eaa0eb66724ed
detector = MTCNN()


# define HSV color ranges for eyes colors
<<<<<<< HEAD
class_name = ("Blue", "Blue Gray", "Brown", "Brown Gray", "Brown Black", "Green", "Green Gray", "Other")
EyeColor = {
    class_name[0] : ((166, 21, 50), (240, 100, 85)),
    class_name[1] : ((166, 2, 25), (300, 20, 75)),
    class_name[2] : ((2, 20, 20), (40, 100, 60)),
    class_name[3] : ((20, 3, 30), (65, 60, 60)),
    class_name[4] : ((0, 10, 5), (40, 40, 25)),
    class_name[5] : ((60, 21, 50), (165, 100, 85)),
    class_name[6] : ((60, 2, 25), (165, 20, 65))
=======
class_name = ("Blue", "Brown", "Black", "Green", "Other")
EyeColor = {
    class_name[0] : ((166, 21, 50), (240, 100, 85)),
    class_name[1] : ((2, 20, 20), (40, 100, 60)),
    class_name[2] : ((0, 10, 5), (40, 40, 25)),
    class_name[3] : ((60, 21, 50), (165, 100, 85))
>>>>>>> 8a8112f87734651ff1b98b4acf9eaa0eb66724ed
}

def check_color(hsv, color):
    if (hsv[0] >= color[0][0]) and (hsv[0] <= color[1][0]) and (hsv[1] >= color[0][1]) and \
    hsv[1] <= color[1][1] and (hsv[2] >= color[0][2]) and (hsv[2] <= color[1][2]):
        return True
    else:
        return False

# define eye color category rules in HSV space
def find_class(hsv):
<<<<<<< HEAD
    color_id = 7
=======
    color_id = 4
>>>>>>> 8a8112f87734651ff1b98b4acf9eaa0eb66724ed
    for i in range(len(class_name)-1):
        if check_color(hsv, EyeColor[class_name[i]]) == True:
            color_id = i

    return color_id

def eye_color(image):
    imgHSV = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    h, w = image.shape[0:2]
    imgMask = np.zeros((image.shape[0], image.shape[1], 1))
    
    result = detector.detect_faces(image)
    if result == []:
        print('Warning: Can not detect any face in the input image!')
        return
    print(result)
    bounding_box = result[0]['box']
    left_eye = result[0]['keypoints']['left_eye']
    right_eye = result[0]['keypoints']['right_eye']
    print(left_eye,right_eye)
    eye_distance = np.linalg.norm(np.array(left_eye)-np.array(right_eye))
    eye_radius = eye_distance/15 # approximate
   
    cv2.circle(imgMask, left_eye, int(eye_radius), (255,255,255), -1)
    cv2.circle(imgMask, right_eye, int(eye_radius), (255,255,255), -1)

    cv2.rectangle(image,
              (bounding_box[0], bounding_box[1]),
              (bounding_box[0]+bounding_box[2], bounding_box[1] + bounding_box[3]),
              (255,155,255),
              2)

    cv2.circle(image, left_eye, int(eye_radius), (0, 155, 255), 1)
    cv2.circle(image, right_eye, int(eye_radius), (0, 155, 255), 1)

    eye_class = np.zeros(len(class_name), np.float)

    for y in range(0, h):
        for x in range(0, w):
            if imgMask[y, x] != 0:
                eye_class[find_class(imgHSV[y,x])] +=1 

    main_color_index = np.argmax(eye_class[:len(eye_class)-1])
    total_vote = eye_class.sum()

    #print("\n\nDominant Eye Color: ", class_name[main_color_index])
    '''print("\n **Eyes Color Percentage **")
    for i in range(len(class_name)):
        print(class_name[i], ": ", round(eye_class[i]/total_vote*100, 2), "%")'''
    
    label = 'Dominant Eye Color: %s' % class_name[main_color_index]  
    cv2.putText(image, label, (left_eye[0]-10, left_eye[1]-40), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (155,255,0))
    cv2.imshow('EYE-COLOR-DETECTION', image)
    return class_name[main_color_index]

if __name__ == '__main__':
<<<<<<< HEAD
    imageInput = "test2.jpeg"
    image = cv2.imread(imageInput, cv2.IMREAD_COLOR)
=======
    imageInput = "test4.jpg"
    image = cv2.imread(imageInput, cv2.IMREAD_COLOR)
    image = imutils.resize(image, width=1000)
>>>>>>> 8a8112f87734651ff1b98b4acf9eaa0eb66724ed
    # detect color percentage
    print(eye_color(image))
    cv2.imwrite('result.jpg', image)    
    cv2.waitKey(0)
