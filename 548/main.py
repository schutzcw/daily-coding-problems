import argparse
import random

MIN_HAND_DEG_PER_MIN = 6.0
HR_HAND_DEG_PER_HR = 30.0
HR_HAND_DEG_PER_MIN = 0.50

def calculate_angle(time: str) -> float:
    """ """
    tokens = time.split(":")
    hrs = int(tokens[0])
    if hrs == 12:
        hrs = 0
    HOURS = hrs
    MINUTES = int(tokens[1])

    MIN_DEG = MIN_HAND_DEG_PER_MIN * MINUTES
    hr_deg = HR_HAND_DEG_PER_HR * HOURS
    # account for minutes into hour
    hr_deg += HR_HAND_DEG_PER_MIN * MINUTES 
    return abs(MIN_DEG - hr_deg)

def rand_time():
    hour = random.randint(0,12)
    minute = random.randint(0,59)

    return f"{hour}:{minute}"

def main():
    """ """

    parser = argparse.ArgumentParser()
    parser.add_argument("--time", help="The time in hh:mm format")
    args = parser.parse_args()

    time = args.time
    if time is None:
        time = rand_time()

    angle = calculate_angle(time)
    print(f"{time} -> {angle} degrees")


if __name__ == "__main__":
    main()