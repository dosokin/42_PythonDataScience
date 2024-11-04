from ft_filter import ft_filter
import sys


def get_word_len_limit() -> int:

    """get the minimum authorized length for a word from the second argument"""

    try:
        return int(sys.argv[2])
    except Exception:
        raise AssertionError("AssertionError: the arguments are bad")


def get_word_list() -> list:

    """get the word list from the first argument"""

    return sys.argv[1].split(' ')


def filter_words(word_list: list, word_len_limit: int) -> list:

    """return the filtered list of words based on the
minimum length provided"""

    return list(ft_filter(lambda a: len(a) > word_len_limit, word_list))


def main():

    try:
        assert len(sys.argv) == 3, "AssertionError: the arguments are bad"
        word_len_limit = get_word_len_limit()
        word_list = get_word_list()
        print(filter_words(word_list, word_len_limit))
    except AssertionError as e:
        print(e)


if __name__ == "__main__":
    main()
