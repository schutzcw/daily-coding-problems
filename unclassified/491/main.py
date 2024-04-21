#TODO: What's the max size integer you can have before you start running into issues?

def is_palidrome(number: int) -> bool:
    """Check to see if the number is a palindrome without converting it to a string.

    Args:
        number (int): The integer to check.

    Returns:
        bool: True if the number is a palindrome. Otherwise False.
    """

    vals = []
    n = 1
    div = number
    while div >= 1:
        print(f"div: {div}")
        val = int(div) % 10
        print(f"val: {val}")
        vals.append(val)
        n = n * 10
        div = number / n

    for i in range(len(vals)):
        print(f"{vals[i]}, {vals[-i-1]}")
        if vals[i] != vals[-i-1]:
            return False
    return True



def main():
    """ """
    import sys
    print(sys.maxsize)
    #        9223372036854775807
    number = 1223334445444333221
    print(f"Number: {number}")
    result = is_palidrome(number)
    print(result)

if __name__ == "__main__":
    main()