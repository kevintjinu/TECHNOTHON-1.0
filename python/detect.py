import numpy as np
from matplotlib import pyplot as plt
import cv2
import time
from get_val import get_vals
'''
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 2100)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1600)
cap.set(cv2.CAP_PROP_FPS, 30)

x, y, w, h = 950, 300, 200, 200
sum = 0

while True:
    success, image = cap.read()
    img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    crop_img = img[y:y + h, x:x + w]

    crop_img, img_plot, hb_vals = get_vals(crop_img)

    cv2.imshow('Crop', crop_img)
    cv2.imshow('Graph', img_plot)
    
    for i in hb_vals:
        sum = i + sum
    if (sum/len(hb_vals)) > 60 and (sum/len(hb_vals)) <100:
        break
    #print(f"The Value is {(sum/len(hb_vals))}")
#cv2.imshow(temp_img)    
cap.release()
cv2.destroyAllWindows()

print(f"The Value is {round(sum/len(hb_vals),2)} bpms")
'''

def values():
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 2100)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1600)
    cap.set(cv2.CAP_PROP_FPS, 30)

    x, y, w, h = 950, 300, 200, 200

    while True:
        success, image = cap.read()
        img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        crop_img = img[y:y + h, x:x + w]

        crop_img, img_plot, hb_vals = get_vals(crop_img)

        #cv2.imshow('Crop', crop_img)
        #cv2.imshow('Graph', img_plot)
        
        count = 0
        sum = 0

        for i in hb_vals:
            sum = i + sum
            if i != 0:
                count = count + 1

        if count == len(hb_vals):
            #if (sum/len(hb_vals)) > 60 and (sum/len(hb_vals)) <100:
            break
        #print(f"The Value is {(sum/len(hb_vals))}")
        #cv2.imshow(temp_img)
        #print(f"COUNT = {count}")
        #print(f"len(hb_values) = {len(hb_vals)}")  

    cap.release()
    cv2.destroyAllWindows()

    #print(f"The Value is {round(sum/len(hb_vals),2)} bpms")
    return hb_vals, round(sum/len(hb_vals),2)
