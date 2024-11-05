from load_image import ft_load
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt


def ft_zoom(image: Image):

    """take an object PIL.Image, zoom in and convert it to greyscale"""

    start_y = 100
    start_x = 450

    # convert to greyscale
    image = image.convert("L")

    # crop image
    image = image.crop((start_x, start_y, start_x + 400, start_y + 400))

    # print new image data
    bw_image = np.array(image).reshape(400, 400, 1)
    print(f"New shape after slicing: {bw_image.shape}")
    print(bw_image)

    return image


def main():
    image_path = "animal.jpeg"

    original_image = ft_load(image_path)
    if original_image is None:
        return

    zoomed_image = ft_zoom(original_image)
    if zoomed_image is None:
        return

    # add x y axis
    plt.imshow(zoomed_image.convert("RGB"))

    # display image
    plt.show()


if __name__ == "__main__":
    main()
