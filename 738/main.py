import argparse
import pathlib
import sys

# TODO make function

def main():
    """ """

    parser = argparse.ArgumentParser()
    parser.add_argument("data_path", help="path to a txt file containing data")
    parser.add_argument("max_length", type=int, help="max length of each line")
    args = parser.parse_args()

    if not pathlib.Path(args.data_path).is_file():
        raise RuntimeError(f"Provided file does not exist: {args.data_path}")

    # assume data is one a single line
    with open(args.data_path, "rt") as F:
        data = F.readline()

    tokens = data.split(" ")
    output = []
    line = []
    line_length = 0
    for token in tokens:
        print(f"token='{token}', len(token)={len(token)}, line={line}, line_length={line_length}")
        TOKEN_LENGTH = len(token)

        # determine what new line length would be if we added the current token
        # add 1 for space between previous word and current
        new_length = line_length + TOKEN_LENGTH
        if line_length != 0:
            new_length += 1
    
        if new_length > args.max_length:
            if line_length == 0: # case where we can't fit one word on line
                print("None")
                sys.exit(0)
            output.append(line)
            line = [token]
            line_length = TOKEN_LENGTH
        else:
            line.append(token)
            line_length = new_length
    
    if len(line) > 0:
        output.append(line)

    print(output)

    # extra testing:
    lengths = [len(" ".join(line)) for line in output]
    print(lengths)
        

if __name__ == "__main__":
    main()
