import numpy as np
from scipy import signal    # For signal.gaussian function
import cv2

from myImageFilter import myImageFilter, myImageFFTFilter

def myEdgeFilter(img0, sigma):
    # YOUR CODE HERE

    # Get size of filter from sigma
    hsize = int(2 * np.ceil(3 * sigma) + 1)

    # Create a 1D Gaussian filter, normalized to prevent intensity changes
    gauss_1d = signal.windows.gaussian(hsize, std=sigma).reshape(1, -1)
    gauss_1d = gauss_1d / np.sum(gauss_1d)

    # Create a 1D derivative filter
    deriv_1d = np.arange(-hsize // 2 + 1, hsize // 2 + 1).reshape(1, -1)

    # Create the 2D Sobel X and Sobel Y filters, from the respective seperable fitlers
    sobelX_filter = np.dot(gauss_1d.T, deriv_1d)
    sobelY_filter = np.dot(deriv_1d.T, gauss_1d)

    # Apply your Sobel X and Y filters on the input image
    imgX = myImageFilter(img0, sobelX_filter)
    imgY = myImageFilter(img0, sobelY_filter)
    cv2.imwrite('../results/sobelX.png', 255 * np.abs(imgX) / np.max(np.abs(imgX)))
    cv2.imwrite('../results/sobelY.png', 255 * np.abs(imgY) / np.max(np.abs(imgY)))

    # Later in Q3.5: Apply your Sobel X and Y filters on the input image using Fourier Transform
    imgX = myImageFFTFilter(img0, sobelX_filter)
    imgY = myImageFFTFilter(img0, sobelY_filter)
    cv2.imwrite('../results/sobelX_fft.png', 255 * np.abs(imgX) / np.max(np.abs(imgX)))
    cv2.imwrite('../results/sobelY_fft.png', 255 * np.abs(imgY) / np.max(np.abs(imgY)))

    # Code for visualizing your results
    # cv2.imshow("Sobel X", imgX)
    # cv2.waitKey(0)

    # Compute the gradient angles and the edge magnitude image
    imgOut = np.sqrt(imgX**2 + imgY**2)
    
    # Calculate angle in degrees and map to [0, 180)
    angle = np.arctan2(imgY, imgX) * 180 / np.pi
    angle[angle < 0] += 180

    # Apply NMS considering gradient edges to thin out the lines (suppress noisy edge points)
    # Quantize angles to 0, 45, 90, 135 degrees (represented as 0, 1, 2, 3)
    angle_quant = np.round(angle / 45.0) % 4

    # Shift images using np.roll to get neighbor values
    mag_e = np.roll(imgOut, -1, axis=1)
    mag_w = np.roll(imgOut, 1, axis=1)
    mag_ne = np.roll(np.roll(imgOut, -1, axis=0), -1, axis=1)
    mag_sw = np.roll(np.roll(imgOut, 1, axis=0), 1, axis=1)
    mag_n = np.roll(imgOut, -1, axis=0)
    mag_s = np.roll(imgOut, 1, axis=0)
    mag_nw = np.roll(np.roll(imgOut, -1, axis=0), 1, axis=1)
    mag_se = np.roll(np.roll(imgOut, 1, axis=0), -1, axis=1)

    # Check NMS conditions along the gradient direction
    cond0 = (angle_quant == 0) & (imgOut >= mag_e) & (imgOut >= mag_w)
    cond1 = (angle_quant == 1) & (imgOut >= mag_ne) & (imgOut >= mag_sw)
    cond2 = (angle_quant == 2) & (imgOut >= mag_n) & (imgOut >= mag_s)
    cond3 = (angle_quant == 3) & (imgOut >= mag_nw) & (imgOut >= mag_se)

    # Keep pixels that are local maxima along their gradient direction
    imgOut = imgOut * (cond0 | cond1 | cond2 | cond3)

    # Return final image
    return imgOut