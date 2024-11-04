
def ft_filter(func, iterable):
    """Return an iterator yielding those items of iterable for
which function(item) is true.
If function is None, return the items that are true."""

    if func is None:
        return (element for element in iterable if element)
    return (element for element in iterable if func(element))

#
# def main():
#     test = ['a', 'B', 'c', 'D', 'test']
#
#     print(list(filter(str.islower, test)))
#     print(list(ft_filter(str.islower, test)))
#
#
# if __name__ == "__main__":
#     main()
