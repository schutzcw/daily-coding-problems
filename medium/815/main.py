import math
import random

# NOTE: to get to 3 decimal places we need to use a sufficiently large sampel size.
def main():
    """
    Overview: Sample only in the first quadrant. Area of circle in first quadrant is A = pi * r^2 / 4.
    Therefore, pi = 4 * A / r^2. We've set r = 1, so pi = 4 * A, where A ~= fraction of samples that fall within x^2 + y^2 = 1 
    """
    n_samples = 5_000
    for _ in range(17):
        count = 0
        for _ in range(n_samples):
            x = random.random()
            y = random.random()
            r2 = math.pow(x, 2) + math.pow(y,2)
            if r2 <= 1:
                count += 1
        pi = 4 * count / n_samples
        print(f"(N={n_samples}, PI ~= {pi:.5f}, diff = {3.14158 - pi}")
        n_samples *= 2

    

if __name__ == "__main__":
    main()