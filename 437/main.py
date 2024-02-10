from typing import Set

def get_smallest_substring(string: str, chars: Set[str]) -> (str | None):
    """
    """
    print(f"String: {string}")
    print(f"Chars: {chars}")

    idx = 0
    shortest_idx = -1
    shortest_str = string
    while idx < len(string):
        print(f"idx: {idx}, char: {string[idx]}")
        if string[idx] in chars:
            print(f"start: {idx}")
            remaining = chars.copy()
            remaining.remove(string[idx])

            idx2 = idx + 1
            while idx2 < len(string):
                print(f"\tidx2: {idx2}, char: {string[idx2]}")
                if string[idx2] in remaining:
                    print("\t\tremoved")
                    remaining.remove(string[idx2])    

                if len(remaining) == 0:
                    print("\tlen(remaining) == 0")
                    str_length = idx2 - idx + 1
                    if str_length < len(shortest_str):
                        shortest_str = string[idx:idx2+1]
                        shortest_idx = idx
                        print(f"\t\tshortest_str: {shortest_str}")
                        break
                idx2 += 1
    
        idx += 1

    return None if shortest_str == string else shortest_str


def main():
    """ """
    chars = set(["a", "e", "i"])
    string = "figehaeci"

    shortest = get_smallest_substring(string, chars)
    print()
    print(f"Shortest String: {shortest}")

if __name__ == "__main__":
    main()