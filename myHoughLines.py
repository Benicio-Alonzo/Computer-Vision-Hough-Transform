import numpy as np
import cv2  # For cv2.dilate function

def myHoughLines(img_hough, nLines):
    # YOUR CODE HERE

    # Perform NMS or apply cv2.dilate...
    #   Multiple ways to ensure suppression of noisy votes

    # Find largest nLines using npy argpartition

    # return [rhos, thetas]
