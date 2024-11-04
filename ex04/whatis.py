import sys


def whatis():

    argv = sys.argv

    if len(argv) == 1:
        return

    assert len(argv) <= 2, "AssertionError: more than one argument is provided"

    try:
        n = int(argv[1])
    except:
        raise AssertionError("AssertionError: argument is not an integer")

    if n % 2:
        print("I'm Odd")
    else:
        print("I'm Even")


try:
    whatis()
except AssertionError as e:
    print(e)
