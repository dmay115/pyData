def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    swap = ""
    if to_swap.upper() == to_swap:
        for letter in phrase:
            if letter == to_swap:
                swap += letter.lower()
            elif letter.upper() == to_swap:
                swap += letter.upper()
            else:
                swap += letter
        return swap
    else:
        for letter in phrase:
            if letter == to_swap:
                swap += letter.upper()
            elif letter.lower() == to_swap:
                swap += letter.lower()
            else:
                swap += letter
        return swap

