import numpy as np
from myHoughLines import myHoughLines
from myHoughTransform import myHoughTransform

def myHoughLineSegments(img_threshold, nLines, rhoRes, thetaRes):
    # YOUR CODE HERE
    [img_hough, rhoScale, thetaScale] = myHoughTransform(img_threshold, rhoRes, thetaRes)
    [rhos, thetas] = myHoughLines(img_hough, nLines)
    
    segments = []
    y_idxs, x_idxs = np.nonzero(img_threshold)
    
    for k in range(nLines):
        theta = thetaScale[thetas[k]]
        rho = rhoScale[rhos[k]]
        
        # Find all edge points that belong to this line
        # We allow a small tolerance in rho matching
        point_rhos = x_idxs * np.cos(theta) + y_idxs * np.sin(theta)
        line_pts_mask = np.abs(point_rhos - rho) <= rhoRes
        
        if not np.any(line_pts_mask):
            continue
            
        line_x = x_idxs[line_pts_mask]
        line_y = y_idxs[line_pts_mask]
        
        # Sort points depending on the dominant axis to find segments
        if np.abs(np.sin(theta)) > np.abs(np.cos(theta)):
            sort_idx = np.argsort(line_x)
        else:
            sort_idx = np.argsort(line_y)
            
        line_x = line_x[sort_idx]
        line_y = line_y[sort_idx]
        
        # Group contiguous points into segments
        max_gap = 5 # max gap between pixels to be considered the same segment
        min_length = 20 # minimum pixel length of a segment
        
        start_idx = 0
        for i in range(1, len(line_x)):
            dist = np.sqrt((line_x[i] - line_x[i-1])**2 + (line_y[i] - line_y[i-1])**2)
            if dist > max_gap or i == len(line_x) - 1:
                end_idx = i - 1 if dist > max_gap else i
                seg_length = np.sqrt((line_x[end_idx] - line_x[start_idx])**2 + 
                                     (line_y[end_idx] - line_y[start_idx])**2)
                
                if seg_length >= min_length:
                    segments.append([line_x[start_idx], line_y[start_idx], 
                                     line_x[end_idx], line_y[end_idx]])
                start_idx = i

    return segments