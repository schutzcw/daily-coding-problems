import sys

def get_first_repeated_char(string: str) -> str:
    """_summary_

    Args:
        string (str): _description_

    Returns:
        str: _description_
    """

    seen = set()
    for char in string:
        if char in seen:
            return char
        seen.add(char)
    return "null"

def print_repeated(string):
    first_repeated_char = get_first_repeated_char(string)
    print(first_repeated_char)

if __name__ == "__main__":
    # STRING = sys.argv[1]

    print_repeated("acbbac")
    print_repeated("abcdef")    
    print_repeated("abckldnwuckdbqycotnuvqwpodef")
   