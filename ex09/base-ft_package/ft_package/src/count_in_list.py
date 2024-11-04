def count_in_list(lst: list, searched: str) -> int:

    count = 0

    for element in lst:
        if element == searched:
            count += 1

    return count
