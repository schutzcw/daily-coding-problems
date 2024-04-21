import argparse

enable_debugging = False

def log(string: str) -> None:
    """ """
    if enable_debugging:
        print(string)

def find_longest_substring(string: str, k: int) -> tuple[str,int]:
    """ """
    if len(string) == 0:
        return string

    max_idx = 0
    max_length = 0
    char_count = dict()
    start = 0
    for idx in range(len(string)):
        log(f"idx: {idx}")
        if (idx - start) > max_length:
            max_length = idx - start
            max_idx = start
            log(f"New max length: {max_length}: {string[start:(start+idx+1)]}")
        
        char = string[idx]
        if char not in char_count:
            char_count[char] = 0
        char_count[char] += 1
        keys = char_count.keys()
        log(f"char_set: {keys}")
        while len(keys) > k:
            char = string[start]
            log(f"len(keys) > {k}. Decrementing {char}")
            char_count[char] -= 1
            if char_count[char] == 0:
                del char_count[char]
            start += 1
    return string[max_idx:(max_idx + max_length)], max_idx
            

def main():
    """ """
    parser = argparse.ArgumentParser()
    parser.add_argument("--debug", action="store_true", help="enable debuggin")
    args = parser.parse_args()
    global enable_debugging
    enable_debugging = args.debug

    # string = "abcba"
    string = "abbbbbacbadbbbabbabbbabbdbcbbcbbbdbcbbccccaaaabdbabc"
    k = 2
    print(find_longest_substring(string,k))

if __name__ == "__main__":
    main()