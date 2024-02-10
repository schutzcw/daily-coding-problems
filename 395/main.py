def get_sets(input_: list[str]):
    """ """
    map_ = {}
    for string in input_:
        sorted_ = "".join(sorted(string))
        if sorted_ not in map_:
            map_[sorted_] = []
        map_[sorted_] += [string]
    output = []
    for key in map_:
        output.append([v for v in map_[key]])
    return output

def main():
    """ """
    input_ = ['eat', 'ate', 'apt', 'pat', 'tea', 'now']
    sets = get_sets(input_)
    print(sets)


if __name__ == "__main__":
    main()

# [['eat', 'ate', 'tea'],
#  ['apt', 'pat'],
#  ['now']]
        
