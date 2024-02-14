
def get_palindrome(idx: int, string: str) -> str:
    """ """
    palindrome = string[idx]
    prev_idx = idx - 1
    next_idx = idx + 1
    while (prev_idx >= 0) and (next_idx < len(string)):
        if string[prev_idx] == string[next_idx]:
            palindrome = string[prev_idx] + palindrome + string[next_idx]
        prev_idx -= 1
        next_idx += 1
    return palindrome

def get_longest_sub_palindrome(string: str) -> str:
    """ """
    max_palindrome = ""
    for idx in range(len(string)):
        palindrome = get_palindrome(idx, string)
        print(f"idx: {idx}, palindrome: {palindrome}, len(palindrome): {len(palindrome)}")
        if len(palindrome) > len(max_palindrome):
            max_palindrome = palindrome
            print(f"NEW: {palindrome}")
    return max_palindrome

def main():
    lsp1 = get_longest_sub_palindrome("aabcdcb")
    lsp2 = get_longest_sub_palindrome("bananas")
    print(lsp1)
    print(lsp2)

if __name__ == "__main__":
    main()