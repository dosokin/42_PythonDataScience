import numpy as np
from PIL import Image


def open_image(path: str):

    """open image and return it"""

    try:
        image = Image.open(path)
    except FileNotFoundError as e:
        raise e
    return image


def ft_load(path: str) -> Image or None:

    """loads an image, prints its format, and its pixels
content in RGB format"""

    try:
        image = open_image(path)
    except FileNotFoundError:
        print("Error\nerror opening given file")
        return None

    try:
        array = np.array(image)
    except ValueError:
        print("Error\n\
        unable to convert image's binary to array")
        return None

    print(f"The shape of image is: {array.shape}")
    print(array)

    return image
