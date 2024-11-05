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

    return image


def ft_zoom(image: Image):

    """take an object PIL.Image, zoom in and convert it to greyscale"""

    start_y = 100
    start_x = 450

    # convert to greyscale
    image = image.convert("L")

    # crop image
    image = image.crop((start_x, start_y, start_x + 400, start_y + 400))

    array = np.array(image).reshape(400, 400, 1)
    print(f"The shape of image is: {array.shape}")
    print(array)

    return image
