import cv2
import numpy as np
import os

from myEdgeFilter import myEdgeFilter
from myHoughLineSegments import myHoughLineSegments

datadir    = '../data'      # the directory containing the images
resultsdir = '../results'   # the directory for dumping results

# parameters
sigma     = 2
threshold = 0.11
rhoRes    = 2
thetaRes  = np.pi / 180
nLines    = 15
# end of parameters

for file in os.listdir(datadir):
    if file.endswith('.jpg'):
        file = os.path.splitext(file)[0]
        
        # read in images
        img = cv2.imread('%s/%s.jpg' % (datadir, file))
        
        # Converting it to grayscale if a color image
        if (img.ndim == 3):
            img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        img = np.float32(img) / 255

        # implement edge filter (Sobel x and Sobel y filters)
        img_edge = myEdgeFilter(img, sigma)

        # apply threhsold to clean up the edge image
        img_threshold = np.float32(img_edge > threshold)

        # ==========================================
        # COMPLETE: Get custom segments and OpenCV segments
        # ==========================================
        
        # Retrieve segments from your custom function
        my_segments = myHoughLineSegments(img_threshold, nLines, rhoRes, thetaRes)
        
        # Retrieve segments from OpenCV for comparison
        cv_lines = cv2.HoughLinesP(np.uint8(255 * img_threshold), rhoRes, thetaRes, \
                                   threshold=50, minLineLength=50, maxLineGap=5)

        # Create a color image to draw the lines on
        img_lines = np.dstack([img,img,img])

        # Display custom segments in RED (thickness 2 to make them stand out)
        for seg in my_segments:
            cv2.line(img_lines, (int(seg[0]), int(seg[1])), (int(seg[2]), int(seg[3])), (0, 0, 255), 2)

        # Display OpenCV line segments in GREEN (thickness 1)
        if cv_lines is not None:
            for line in cv_lines:
                coords = line[0]
                cv2.line(img_lines, (coords[0], coords[1]), (coords[2], coords[3]), (0, 255, 0), 1)

        # Save
        fname = '%s/%s_05segments.png' % (resultsdir, file)
        cv2.imwrite(fname, 255 * img_lines) 
        print(f"Saved segments image to: {fname}")