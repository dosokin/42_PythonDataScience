import numpy as np


def give_bmi(height: list[int | float], weight: list[int | float]) \
        -> list[int | float]:
    """return bmi based on given heights and weights"""

    if len(height) != len(weight):
        print("Error: height and weight lists are not the same size")
        return []

    h = np.array(height)
    w = np.array(weight)
    if h.min() > 0 and w.min() > 0:
        print("Error: negative height or weight")
        return []

    bmi = (w / (h * h)).tolist()

    return bmi


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """check if corresponding bmis are above limit"""

    values = np.array(bmi)

    bmi_above_limit = (values <= limit).tolist()

    return bmi_above_limit
