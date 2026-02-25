import numpy as np

def myImageFilter(img0, filter):
    # YOUR CODE HERE

    # Notes: are you going to apply this filter with a convolution or correlation operation?

    # Pad input image based on size of filter

    # Apply filter on the image
    #   Make sure the output image is the same size as the input

    return imgOut


def myImageFFTFilter(img0, filter):

    # Pad the filter such that it has the same size as img0
    filterY, filterX = filter.shape
    c_filterY, c_filterX = filterY // 2, filterX // 2

    height, width = img0.shape
    c_height, c_width = height // 2, width // 2

    pad_height = c_height - c_filterY
    pad_width = c_width - c_filterX 
    bottom_pad_height = pad_height - 1
    bottom_pad_width = pad_width - 1

    if height % 2 != 0:
        bottom_pad_height += 1
    if width % 2 != 0:
        bottom_pad_width += 1

    filter_padded = np.pad(filter, [(pad_height, bottom_pad_height), (pad_width, bottom_pad_width)], mode='constant')

    # Transform image and filter into the frequency domain

    # Apply filter onto image

    # Transform result into image space domain
    #   and shift for correct orientation of origin

    return imgOut