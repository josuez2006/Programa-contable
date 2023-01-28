def for_each_item_do(list: list, fn) -> list:
    new_list = []
    for item in list:
        new_list.append(fn(item))

    return new_list


def disarray(arr: list) -> list:
    new_arr = []
    for inner_arr in arr:
        for element in inner_arr:
            new_arr.append(element)

    return new_arr