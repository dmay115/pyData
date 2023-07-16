def remove_every_other(lst):
    """Return a new list of other item.

        >>> lst = [1, 2, 3, 4, 5]

        >>> remove_every_other(lst)
        [1, 3, 5]

    This should return a list, not mutate the original:

        >>> lst
        [1, 2, 3, 4, 5]
    """
    every_other = []
    switch = "every"
    for item in lst:
        if switch == "every":
            every_other.append(item)
            switch = "other"
        else:
            switch = "every"
    return every_other