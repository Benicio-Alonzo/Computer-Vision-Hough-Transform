import numpy as np
import cv2  # For cv2.dilate function

def myHoughLines(img_hough, nLines):
    # YOUR CODE HERE

    # Perform NMS or apply cv2.dilate...
    #   Multiple ways to ensure suppression of noisy votes
    kernel = np.ones((3, 3), np.uint8)
    dilated = cv2.dilate(np.float32(img_hough), kernel)
    
    # Create a mask of local maxima
    peaks = (img_hough == dilated) & (img_hough > 0)
    img_hough_nms = img_hough * peaks

    # Find largest nLines using npy argpartition
    flat_hough = img_hough_nms.flatten()
    # argpartition puts the highest nLines at the end of the array
    flat_indices = np.argpartition(flat_hough, -nLines)[-nLines:]
    
    # Sort these top indices in descending order so the strongest line is first
    flat_indices = flat_indices[np.argsort(-flat_hough[flat_indices])]

    # Convert flat indices back to 2D coordinates
    rhos, thetas = np.unravel_index(flat_indices, img_hough_nms.shape)

    # return [rhos, thetas]
    return [rhos, thetas]