import sys

if __name__ == "__main__":
    target = int(sys.argv[1])
    
    arr = [10, 15, 3, 7]
    will_match = set()
    for val in arr:
        if val in will_match:
            print(f"Success! {target - val} + {val}")
            sys.exit(0)
        diff = target - val
        will_match.add(diff)
    
    print(f"No matches")
    