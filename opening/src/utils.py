import numpy as np
from PIL import Image
import matplotlib.pyplot as plt


def load_mono_image(path):
    img = Image.open(path)
    if img.mode != "L":
        img = img.convert("L")
    img = np.array(img, dtype=np.uint8) / 255.0
    img = img.astype(np.double)
    return img


def load_binary_image(path):
    img = Image.open(path)
    if img.mode != "1":
        img = img.convert("1")
    img = np.array(img, dtype=bool)
    return img


def save_image(img, file):
    if file:
        plt.imsave(file.name, img, cmap='gray')
