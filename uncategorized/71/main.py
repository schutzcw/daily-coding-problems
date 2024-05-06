import math
import random

def rand7():
    # random.random() -> [0,1)
    return 1 + math.floor(random.random() * 7)

def rand5():
    val = rand7()
    while val > 5:
        val = rand7()
    return val
    

if __name__ == "__main__":
    val_map = {i+1:0 for i in range(5)}
    for i in range(50_000):
        val = rand5()
        val_map[val] += 1
    print(val_map)
