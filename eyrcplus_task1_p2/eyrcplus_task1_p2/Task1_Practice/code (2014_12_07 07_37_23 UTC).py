import numpy as np
import cv2

img = cv2.imread('test_images/1.jpg')

#Teams can add other helper functions which can be \
#added here

def play(img):
    '''
    img-- a single test image as input argument
    letter -- returns the single character specifying the target that was 
    hit  eg. 'A', 'D', etc
    '''
    #add your code here
    return letter

if __name__ == "__main__":
    #checking output for single image
    img = cv2.imread('test_images/1.jpg')
    balloon_letter = play(img)
    print balloon_letter, " balloon in range"
    #checking output for all images
    alpha_list = []
    for file_number in range(1,11):
        file_name = "test_images/"+str(file_number)+".jpg"
        pic = cv2.imread(file_name)
        balloon_letter = play(pic)
        alpha_list.append(balloon_letter)
    print alpha_list
