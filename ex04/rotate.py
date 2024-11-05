from load_image import ft_load, ft_zoom
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np


def ft_rotate(image):
    array = np.array(image)

    new_array = np.array([])

    for x in range(400):
        for row in array:
            new_array = np.append(new_array, row[x])

    new_array = new_array.reshape(400, 400)

    print(f"New shape after Transpose: {new_array.shape}")
    print(new_array)

    image = Image.fromarray(new_array).convert("RGB")

    return image


def main():
    image_path = "animal.jpeg"

    original_image = ft_load(image_path)
    if original_image is None:
        return

    zoomed_image = ft_zoom(original_image)

    rotated_image = ft_rotate(zoomed_image)

    # add x y axis
    plt.imshow(rotated_image.convert("RGB"))

    # display image
    plt.show()


if __name__ == "__main__":
    main()
