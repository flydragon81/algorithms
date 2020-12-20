'''Functions'''


def find_smallest(data):
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


def find_biggest(data):
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


def average_number(data):
    """

    :param data: list
    :return: number
    """
    total = 0
    for num in data:
        total += num
    avg = total / len(data)
    return avg



def bubble_sort(data, ascending=True):
    """

    :param data: list
    :return: list
    """
    length_data = len(data)
    j = 0
    for i in range(1, length_data):
        temp = data[i]
        for j in range(i - 1, -1, -1):
            if ascending:
                if temp < data[j]:
                    data[j + 1] = data[j]
                    data[j] = temp
                else:
                    break
            else:
                if temp > data[j]:
                    data[j + 1] = data[j]
                    data[j] = temp
                else:
                    break

    return data


def insertion_sort(data, ascending=True):
    """

    :param data: list
    :param ascending: ture
    :return: list
    """
    for i in range(1, len(data)):

        key = data[i]

        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i - 1
        if ascending:
            while j >= 0 and key < data[j]:
                data[j + 1] = data[j]
                j -= 1
            data[j + 1] = key
        else:
            while j >= 0 and key > data[j]:
                data[j + 1] = data[j]
                j -= 1
            data[j + 1] = key

    return data
