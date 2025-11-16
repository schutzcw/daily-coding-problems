import random

def rand5() -> int:
    return random.randint(1,5)

def rand7() -> None:
    """ """
    sum = 0
    for _ in range(5):
        sum += rand5()
    return sum % 7 + 1

if __name__ == "__main__":
    map = {i : 0 for i in range(1,8)}
    iters = 10_00_000
    for _ in range(iters):
        map[rand7()] += 1

    print(f"target: {1/7*100}%")
    for (k,v) in map.items():
        print(f"{k} : {v / iters * 100}%")
