import matplotlib.pyplot as plt


def plot_images(img, opened_img, elem):
    fig, axes = plt.subplots(1, 2, figsize=(6, 4))
    axes[0].imshow(img, cmap="Greys_r")
    axes[1].imshow(opened_img, cmap="Greys_r")
    axes[0].set_title('Before')
    axes[1].set_title('After')
    fig.suptitle("Opening with a linear structuring element (length={}, alpha={})".format(elem.length, elem.alpha))
    plt.show()
