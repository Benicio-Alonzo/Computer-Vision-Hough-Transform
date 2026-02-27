import numpy as np

def myImageFilter(img0, filter):

    # Notes: are you going to apply this filter with a convolution or correlation operation?
    # This implementation applies the filter via correlation.

    # Pad input image based on size of filter
    # Using 'edge' mode to ensure pixels lying outside have the same intensity as the nearest pixel
    filt_h, filt_w = filter.shape
    pad_h = filt_h // 2
    pad_w = filt_w // 2
    img_padded = np.pad(img0, ((pad_h, pad_h), (pad_w, pad_w)), mode='edge')

    # Apply filter on the image
    # Make sure the output image is the same size as the input
    img_h, img_w = img0.shape
    imgOut = np.zeros_like(img0, dtype=np.float32)

    # Vectorized correlation: looping over filter dimensions
    for i in range(filt_h):
        for j in range(filt_w):
            imgOut += img_padded[i : i + img_h, j : j + img_w] * filter[i, j]

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
    img_fft = np.fft.fft2(img0)
    filter_fft = np.fft.fft2(filter_padded)

    # Apply filter onto image
    result_fft = img_fft * filter_fft

    # Transform result into image space domain
    # and shift for correct orientation of origin
    imgOut_complex = np.fft.ifft2(result_fft)
    imgOut_shifted = np.fft.fftshift(imgOut_complex)

    # Retrieve real components
    imgOut = np.real(imgOut_shifted)

    return imgOut