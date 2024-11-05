import numpy as np


def slice_me(family: list, start: int, end: int) -> list:

    """resize *family* based on *start* and *end* indexes
return sliced array"""

    try:
        a = np.array(family)
    except ValueError as e:
        print(e)
        return family
    print(f"My shape is : {a.shape}")

    b = a[start:end]
    print(f"My new shape is : {b.shape}")

    return b.tolist()

