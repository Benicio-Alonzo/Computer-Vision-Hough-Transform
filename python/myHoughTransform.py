import numpy as np

def myHoughTransform(img, rhoRes, thetaRes):
    # YOUR CODE HERE
    rows, cols = img.shape
    max_rho = np.ceil(np.sqrt(rows**2 + cols**2))

    # rhoScale =
    # We use 0 to max_rho. Negative rhos will be captured when theta is shifted by pi.
    rhoScale = np.arange(0, max_rho, rhoRes)
    
    # thetaScale =
    thetaScale = np.arange(0, 2 * np.pi, thetaRes)

    # img_hough =
    # Create accumulator based on resolution shape
    img_hough = np.zeros((len(rhoScale), len(thetaScale)), dtype=np.int32)

    # Fill in your accumulator for all edge points in image (non zero value pixels)
    #   Multiple ways to do this
    y_idxs, x_idxs = np.nonzero(img)

    for j, theta in enumerate(thetaScale):
        # Calculate rho for all edge points at this theta
        rhos = x_idxs * np.cos(theta) + y_idxs * np.sin(theta)
        
        # Only consider positive rhos within our scale bounds
        valid_idx = (rhos >= 0) & (rhos < max_rho)
        rhos_valid = rhos[valid_idx]
        
        # Map valid rhos to indices
        rho_idxs = np.round(rhos_valid / rhoRes).astype(int)
        
        # Ensure indices stay within array bounds
        rho_idxs = rho_idxs[rho_idxs < len(rhoScale)]
        
        # Increment accumulator
        np.add.at(img_hough, (rho_idxs, j), 1)

    # Return the accumulator (hough image)
    return [img_hough, rhoScale, thetaScale]