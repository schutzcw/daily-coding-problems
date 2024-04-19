
from typing import List

import random

def generate_random(nums: List[int], probs: List[float]) -> int:
    """ """
    cprobs: List[float] = []
    csum = 0
    for _, val in enumerate(probs):
        csum += val
        cprobs.append(csum)

    rand_val = random.uniform(0,1)
    for (num, cprob) in zip(nums, cprobs):
        if rand_val <= cprob:
            return num
    raise RuntimeError("")
    

def main():
    NUMS = [1, 2, 3, 4]
    PROBS = [0.1, 0.5, 0.2, 0.2]
    
    mc = {i : 0 for i in NUMS}
    N = 100_000
    for _ in range(N):
        mc[generate_random(NUMS, PROBS)] += 1

    for (k,v) in mc.items():
        print(f"{k}: {v/N}")
    

if __name__ == "__main__":
    main()