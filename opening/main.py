import os
import numpy as np
from datetime import datetime
from tkinter import Tk
from tkinter.filedialog import askopenfilename, asksaveasfile

from src.utils import load_mono_image, load_binary_image, save_image
from src.element import StructuringElement
from src.opening import open_image_with_linear_element
from src.plots import plot_images


def run(path):
    print("OTWARCIE ELEMENTEM LINIJNYM\n")
    print("Wczytanie obrazu:")
    img_type = int(input('1. Binarny\t 2. Monochromatyczny:\nOpcja: '))
    if img_type == 1:
        img = load_binary_image(path)
        se_type = bool
    elif img_type == 2:
        img = load_mono_image(path)
        se_type = np.double
    else:
        raise ValueError("Enter '1' or '2'. Check the image you selected.")

    print("\nParametry elementu linijnego")
    length = int(input('Długość: '))
    alpha = int(input('Kąt nachylenia: '))

    structuring_element = StructuringElement(length, alpha, se_type)

    start_time = datetime.now()
    opened_image = open_image_with_linear_element(img, structuring_element.element)
    print('\nCZAS WYKONYWANIA OPERACJI: ', datetime.now() - start_time)

    plot_images(img, opened_image, structuring_element)

    root = Tk()
    file = asksaveasfile(parent=root, defaultextension=".jpg", filetypes=[("JPEG", "*.jpg"), ("PNG", "*.png"),
                                                                          ("All Files", "*.*")])
    save_image(opened_image, file)


def main():
    Tk().withdraw()
    path = askopenfilename(initialdir=os.curdir)
    if path is not None:
        run(path)


if __name__ == '__main__':
    main()
