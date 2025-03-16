import string
from ft_filter import ft_filter


def is_needle(haystack: str):
    """ is_needle() returns a lambda func to test if needle
    is in haystack"""
    return lambda needle: needle in haystack


def not_printable():
    """not printable() returns a lambda func to test if
    the char is not printable"""
    return lambda char: char not in string.printable


def is_greater(size: int):
    """is_greater() returns a lambda func to test if the
    the word's length is greater than the size"""
    return lambda word: len(word) > size


def parse_string(S: str) -> None:
    """The parse_string() func tests the string for punctuation
    and non-printable chars. If either are found, the func
    raises an AssertionError"""
    is_punctuation = is_needle(string.punctuation)

    punctuation_list = list(ft_filter(is_punctuation, S))
    invisible_list = list(ft_filter(not_printable(), S))

    assert len(punctuation_list) == 0 \
        and len(invisible_list) == 0, "the arguments are bad"


def filterstring(S: str, N: int) -> list:
    """The filterstring() func returns a list of words from S that
    have a length greater than N. The func accepts two args"""
    parse_string(S)

    words_list = S.split()
    condition = is_greater(N)

    return list(ft_filter(condition, words_list))


def main():
    from sys import argv

    try:
        assert len(argv) == 3, "the arguments are bad"
        assert argv[1].isascii(), "the arguments are bad"
        assert argv[2].isdigit(), "the arguments are bad"

        filtered_list = filterstring(argv[1], int(argv[2]))
        print(filtered_list)

    except AssertionError as msg:
        print(f"AssertionError: {msg}")
        exit(1)


if __name__ == "__main__":
    main()
