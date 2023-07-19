import numpy as np


def dilate_image(img, element):
    dilated_img = np.zeros_like(img)
    element_height, element_width = element.shape
    pad_height = element_height // 2
    pad_width = element_width // 2
    padded_img = np.pad(img, ((pad_height, pad_height), (pad_width, pad_width)), mode='constant')

    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            window = padded_img[i:i + element_height, j:j + element_width]
            dilated_img[i, j] = np.max(window * element)

    return dilated_img


def erode_image(img, element):
    eroded_img = np.zeros_like(img)
    element_height, element_width = element.shape
    pad_height = element_height // 2
    pad_width = element_width // 2
    padded_img = np.pad(img, ((pad_height, pad_height), (pad_width, pad_width)), mode='constant')

    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            window = padded_img[i:i + element_height, j:j + element_width]
            eroded_img[i, j] = np.min(window[element > 0])

    return eroded_img


def open_image_with_linear_element(img, element):
    open_img = erode_image(img, element)
    open_img = dilate_image(open_img, element)

    return open_img
