import math
import sys


def print_progress_bar(progress: int, total: int):

    """print the progress bar"""

    if progress:
        ratio = total / progress
        percentage = f"{math.ceil(100 / ratio)}%".ljust(4, ' ')
        print(f"\r{percentage}|", end="")
    else:
        print(f"{0}%  |", end=" ")
        ratio = 32

    for i in range(32):
        if i < 32 / ratio:
            print("██", end="")
        else:
            print("  ", end="")

    print(f"| {progress + 1} / {total}", end="")
    sys.stdout.flush()


def ft_tqdm(lst: range) -> None:

    """Decorate an iterable object, returning an iterator which acts exactly
like the original iterable, but prints a dynamically updating
progressbar every time a value is requested.

Returns
-------
out  : decorated iterator.
"""

    total = len(lst)
    for i in lst:
        print_progress_bar(i, total)
        yield i
