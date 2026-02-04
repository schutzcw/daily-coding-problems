import argparse
import os
import pathlib
import sys

results = []

def hint_good(current_vals, hints):
    n_vals = len(current_vals)
    if n_vals == 0:
        return True

    # only need to check the lasted hint. previous ones have been proven valid
    hint_idx = n_vals-1
    hint = hints[hint_idx]
    cur_val = current_vals[hint_idx]
    prev_val = current_vals[hint_idx-1]
    if (hint == "+") and (cur_val <= prev_val):
        return False
    elif (hint == "-") and (cur_val >= prev_val):
        return False
    return True

def reconstruct(current_vals: list[int],
                remaining_vals: list[int],
                hints: list[(str|None)]) -> None:

    if len(remaining_vals) == 0:
        results.append(current_vals)
        return

    for val_idx, val in enumerate(remaining_vals):
        potential_vals = current_vals + [val]
        if hint_good(potential_vals, hints):
            reconstruct(potential_vals,
                        remaining_vals[:val_idx] + remaining_vals[val_idx+1:],
                        hints)


def main() -> None:

    N = 4
    sequence = [i for i in range(0,N+1)]
    hints = [None, "+", "+", "-", "+"]
    reconstruct([], sequence, hints)
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
