def brackets_valid(string: str) -> bool:
    """ """
    print("*"*25)
    print(f"Testing input string: {string}")
    MAP = {
           "}": "{",
           "]": "[",
           ")": "(",
           }
    OPEN_BRACKETS = [MAP[key] for key in MAP]
    stack: list[str] = []
    for idx, char in enumerate(string):
        if char in OPEN_BRACKETS:
            stack.append(char)
        elif char in MAP:
            if (len(stack) == 0) or (stack[-1] != MAP[char]):
                print(f"No match at idx: {idx}")
                return False
            stack.pop()               
        else:
            print(f"Invalid character: {char}")
            return False
    
    if len(stack) == 0:
        return True
    else:
        print("Non-empty stack")
        return False


def main():
    input_string = "([])[]({})"
    print(brackets_valid(input_string))
    input_string = "([)]"
    print(brackets_valid(input_string))
    input_string =  "((()"
    print(brackets_valid(input_string))

if __name__ == "__main__":
    main()