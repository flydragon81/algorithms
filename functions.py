'''Functions'''


def find_smallest_number(data):
    """

    :param data: list
    :return: int
    """
    idx = 0
    found = data[idx]
    i = 0
    while i < len(data):
        if data[i] < found:
            found = data[i]
            idx = i
        i = i + 1

    return idx


def find_biggest_number(data):
    """

    :param data: list
    :return: int
    """
    idx = 0
    found = data[idx]
    i = 0
    while i < len(data):
        if data[i] > found:
            found = data[i]
            idx = i
        i += 1

    return idx
