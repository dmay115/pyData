def repeat(phrase, num):
    """Return phrase, repeated num times.

        >>> repeat('*', 3)
        '***'

        >>> repeat('abc', 2)
        'abcabc'

        >>> repeat('abc', 0)
        ''

    Ignore illegal values of num and return None:

        >>> repeat('abc', -1) is None
        True

        >>> repeat('abc', 'nope') is None
        True
    """
    rep_phrase = ""
    try:
        if num >= 0:
            while num > 0:
                rep_phrase += phrase
                num -= 1
            return rep_phrase
        else:
            return None
    except:
        return None