import numpy as np
from PIL import Image


def ft_invert(array) -> np.ndarray:

    print("Inverts the color of the image received.")

    array = 255 - array

    image = Image.fromarray(array)

    image.show()

    return array


def ft_red(array) -> np.ndarray:

    print("Red filter on the image received.")

    copy = array.ravel()

    pixels_to_turn_black = [x for x in range(copy.size) if x % 3]
    for pixel in pixels_to_turn_black:
        copy[pixel] = 0

    image = Image.fromarray(array)
    image.show()

    return array


def ft_green(array) -> np.ndarray:

    print("Green filter on the image received.")

    copy = array.ravel()

    pixels_to_turn_black = [x for x in range(copy.size) if (x - 1) % 3]
    for pixel in pixels_to_turn_black:
        copy[pixel] = 0

    image = Image.fromarray(array)
    image.show()

    return array


def ft_blue(array) -> np.ndarray:

    print("Blue filter on the image received.")

    copy = array.ravel()

    to_turn_black = [x for x in range(copy.size) if x % 3 == 1 or x % 3 == 0]
    for pixel in to_turn_black:
        copy[pixel] = 0

    image = Image.fromarray(array)
    image.show()

    return array


def ft_grey(array) -> np.ndarray:

    print("Grey scale filter on the image received")

    for row in array:
        for pixel in row:
            pix = pixel.max()
            for i in range(3):
                pixel[i] = pix

    image = Image.fromarray(array)
    image.show()

    return array
