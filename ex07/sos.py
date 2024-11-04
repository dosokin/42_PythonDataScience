import sys


def char_to_morse(c: str) -> str:

    """convert a char to morse code"""

    nested_morse = {
        " ": "/ ",
        "A": ".- ",
        "B": "-... ",
        "C": "-.-. ",
        "D": "-.. ",
        "E": ". ",
        "F": "..-. ",
        "G": "--. ",
        "H": ".... ",
        "I": ".. ",
        "J": ".--- ",
        "K": "-.- ",
        "L": ".-.. ",
        "M": "-- ",
        "N": "-. ",
        "O": "--- ",
        "P": ".--. ",
        "Q": "--.- ",
        "R": ".-. ",
        "S": "... ",
        "T": "- ",
        "U": "..- ",
        "V": "...- ",
        "W": ".-- ",
        "X": "-..- ",
        "Y": "-.-- ",
        "Z": "--.. ",
        "0": "----- ",
        "1": ".---- ",
        "2": "..--- ",
        "3": "...-- ",
        "4": "....- ",
        "5": "..... ",
        "6": "-.... ",
        "7": "--... ",
        "8": "---.. ",
        "9": "----. ",
    }

    morsed_char = nested_morse.get(c.upper())

    if not morsed_char:
        raise AssertionError("AssertionError: the arguments are bad")

    return morsed_char


def main():
    try:
        assert len(sys.argv) == 2, "AssertionError: the arguments are bad"
        print("".join(char_to_morse(c) for c in sys.argv[1]))
    except AssertionError as e:
        print(e)


if __name__ == "__main__":
    main()
