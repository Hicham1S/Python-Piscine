import typing as t


def ft_filter(func: t.Callable[[t.T], t.Any], iterable: t.Iterable[t.T]):
    """ Custom implementation of filter() function """

    return [word for word in iterable if func(word)]
