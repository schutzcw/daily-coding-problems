#!/usr/bin/env python3
###
# Learned ord() and chr() functions. Find out number of digits and work backwards
###

import argparse
import sys
import math
from typing import Dict

INT_MAP: Dict[int, str] = {i : chr(64 + i) for i in range(1,27)}
print(INT_MAP)


def print_in_excel_format(num: int):
    digits: str = ''
    n_digits: int = math.floor(math.log(num, 26))
    while n_digits >= 0:
        TMP = int(math.pow(26, n_digits))
        DIGIT = math.floor(num / TMP)
        digits += INT_MAP[DIGIT]
        n_digits -= 1
        num -= TMP * DIGIT
    print(digits)


def main() -> None:
	""" 
	description
	
	:param name:
	:return
	"""
	
	parser = argparse.ArgumentParser()
	parser.add_argument("number", type=int, help="number to convert")
	args = parser.parse_args()
	
	if args.number < 1:
		print("number must be greater than 0")
		sys.exit(1)
	print_in_excel_format(args.number)


if __name__ == "__main__":
	main()
