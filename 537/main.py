import argparse
import random
from typing import List


def generate_collatz_sequence(value: int) -> List[int]:
    """ """
    seq = [value]
    while value > 1:
        if value % 2 == 0:
            value = int(value / 2)
        else:
            value = 3 * value + 1
        seq.append(value)
    return seq

def main():
    """ """
    parser = argparse.ArgumentParser()
    parser.add_argument("--value", type=int, default=0, help="Starting int in the sequence")
    parser.add_argument("--samples", type=int, help="The number of samples to test")
    parser.add_argument("--start-range", type=int, help="beginning of range")
    parser.add_argument("--end-range", type=int, help="end of range")
    args = parser.parse_args()

    if args.samples is not None:
        for _ in range(args.samples):
            val = int(random.random() * 1_000_000)
            seq = generate_collatz_sequence(val)
            print(seq)
            print(len(seq))
    elif args.start_range is not None:
        max_length = 0
        max_start_val = 0
        for start_val in range(args.start_range, args.end_range):
            print(start_val)
            seq = generate_collatz_sequence(start_val)
            if len(seq) > max_length:
                max_length = len(seq)
                max_start_val = start_val
        print(f"Max start val: {max_start_val}")
        print(f"Max length: {max_length}")
    else:
        val = args.value
        if val == 0:
            val = int(random.random()* 1_000)
        
        seq = generate_collatz_sequence(val)
        print(seq)
        print(len(seq))

if __name__ == "__main__":
    main()
