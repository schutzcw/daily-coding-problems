###
# Description:
#	Daily coding problem 321: minimum steps.
###
import argparse
from functools import reduce
from math import sqrt

def factors(n):
	step = 2 if n%2 else 1
	return sorted(list(set(reduce(list.__add__, ([i, n//i] for i in range(1, int(sqrt(n))+1, step) if n % i == 0)))))

def main() -> None:
    """ 
    description
    
    :param name:
    :return
    """
    
    parser = argparse.ArgumentParser()
    parser.add_argument("n", type=int, help="starting number for steps")
    args = parser.parse_args()

    n = args.n
    steps = [n]
    while n != 1:
        _factors = factors(n)
        n = min(_factors[len(_factors)//2], n - 1)
        steps += [n]

    print(steps)

if __name__ == "__main__":
    main()
