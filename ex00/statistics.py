def ft_mean(elements, to_print=False):
    """calculate the mean"""
    mean = sum(elements) / len(elements)
    if to_print:
        print(f"mean : {mean}")
    return mean


def ft_median(elements):
    """calculate the median"""
    elements.sort()
    median = elements[int(len(elements) / 2)]
    print(f"median : {median}")
    return median


def ft_quartile(elements):
    """calculate the quartile"""
    quartile = [float(elements[int(len(elements) / 4)]),
                float(elements[int(len(elements) / 4 * 3)])]
    elements.sort()
    print(f"quartile : {quartile}")
    return quartile


def ft_std(elements):
    """calculate the standard deviation"""

    variance = ft_var(elements)

    std = variance**(1/2)

    print(f"std : {std}")

    return std


def ft_var(elements, to_print=False):
    """calculate the variance"""

    # calculate mean
    mean = ft_mean(elements)

    # get difference for each element
    diffs = [max(a, mean) - min(a, mean) for a in elements]

    # get squares of differences
    squared_diff = [diff * diff for diff in diffs]

    # sum of squared differences divided by length
    variance = sum(squared_diff) / len(elements)

    if to_print:
        print(f"var : {variance}")

    return variance


def ft_statistics(*args: any, **kwargs: any) -> None:

    """get statistics from the given list of numbers"""

    try:
        elements = [float(element) for element in args]
    except ValueError:
        print("ERROR")
        return

    if not len(elements):
        for _ in kwargs:
            print("ERROR")
        return

    for k in kwargs:
        instruction = kwargs[k]
        if instruction == 'mean':
            ft_mean(elements, True)
        elif instruction == 'median':
            ft_median(elements)
        elif instruction == 'quartile':
            ft_quartile(elements)
        elif instruction == 'std':
            ft_std(elements)
        elif instruction == 'var':
            ft_var(elements, True)
