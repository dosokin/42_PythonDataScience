import sys


def building(s: str):

    """'building' documentation =>
        count characters by category
        """

    lowercase_count = 0
    uppercase_count = 0
    numeric_count = 0
    space_count = 1
    other = 0
    sum = 0

    for letter in s:
        if letter.islower():
            lowercase_count += 1
        elif letter.isupper():
            uppercase_count += 1
        elif letter.isnumeric():
            numeric_count += 1
        elif letter.isspace():
            space_count += 1
        else:
            other += 1
        sum += 1

    print(f"The text contains {sum} characters:")
    print(f"{uppercase_count} upper letters")
    print(f"{lowercase_count} lower letters")
    print(f"{other} punctuation marks")
    print(f"{space_count} spaces")
    print(f"{numeric_count} digits")


def get_text() -> str:

    """'get_text' documentation =>
        Retrieve text as expected in the subject
    """

    assert len(sys.argv) <= 2, ("AssertionError: more"
                                " than one argument is provided")

    if len(sys.argv) == 2:
        s = sys.argv[1]
    else:
        s = ""
    while not s:
        try:
            s = input("What is the text to count?\n")
        except EOFError:
            return ""

    return s


def main():

    # print(get_text.__doc__)
    # print(building.__doc__)

    try:
        s = get_text()
    except AssertionError as e:
        print(e)
        return 1

    building(s)


if __name__ == "__main__":
    main()
