import cv2
import numpy as np
import os

from myEdgeFilter import myEdgeFilter
from myHoughLines import myHoughLines
from myHoughLineSegments import myHoughLineSegments
from myHoughTransform import myHoughTransform

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


        """
        COMPLETE
        """

        # Save
        fname = '%s/%s_05segments.png' % (resultsdir, file)
        cv2.imwrite(fname, 255 * img_lines) 