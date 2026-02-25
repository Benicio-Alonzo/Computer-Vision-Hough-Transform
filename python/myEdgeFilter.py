import numpy as np
from scipy import signal    # For signal.gaussian function
import cv2

from myImageFilter import myImageFilter, myImageFFTFilter

def myEdgeFilter(img0, sigma):
    # YOUR CODE HERE

    # Get size of filter from sigma

    # Create a 1D Gaussian filter, normalized to prevent intensity changes
    # gaussFilter = np.reshape(signal.windows.gaussian())

    # Create a 1D derivative filter

    # Create the 2D Sobel X and Sobel Y filters, from the respective seperable fitlers

    # Apply your Sobel X and Y filters on the input image

    # Later in Q3.5: Apply your Sobel X and Y filters on the input image using Fourier Transform

    # Code for visualizing your results
    # cv2.imshow("Sobel X", imgX)
    # cv2.waitKey(0)

    # Compute the gradient angles and the edge magnitude image

    # Apply NMS considering gradient edges to thin out the lines (suppress noisy edge points)

    # Return final image
    return imgOut