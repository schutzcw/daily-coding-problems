input_list = [2, 1, 2, 3, 3, 1, 3, 5]


def length_from_index(input_list, start_idx):
    """
    return: idx, length, stop_idx (non-inclusive)
    """
    _list = input_list[start_idx:]
    if len(_list) < 2:
        return len(_list)

    _set = set()
    for idx, val in enumerate(_list):
        _set.add(val)
        if len(_set) == 3:
            return idx
    return len(_list)


def main() -> None:
    """ 
    description
    
    :param name:
    :return list of elements involved, length of longest sublist
    """
    print(input_list)

    max_len = 0
    max_idx = 0
    for idx in range(len(input_list)):
        tmp_len = length_from_index(input_list, idx)
        if tmp_len > max_len:
            max_len = tmp_len
            max_idx = idx
    print(f"max_len: {max_len}, max_idx = {max_idx}")


if __name__ == "__main__":
    main()
