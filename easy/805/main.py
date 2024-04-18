import argparse

MAP = {idx : chr(val) for (idx, val) in enumerate(range(ord("A"), ord("A") + 26), start=1)}

enable_logging: bool = False

def log(string: str) -> None:
    if enable_logging:
        print(string)

def calc_column(val: int) -> str:
    """ """
    ret = ""
    itr = 1
    while val > 0:
        log("*"*25)
        log(f"itr = {itr}")
        log(f"val: {val}")
        modulo = val % 26
        if modulo == 0:
            modulo = 26
        log(f"modulo: {modulo}")
        ret = MAP[modulo] + ret
        log(f"ret: {ret}")
        val -= modulo
        val = int(val / 26)
    return ret
          

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("num", type=int, help="Number to calculate letter column for.")
    parser.add_argument("--debug", action="store_true", help="enabling logging")
    args = parser.parse_args()
    
    if args.debug:
        global enable_logging
        enable_logging = True
   
    print(calc_column(args.num))

if __name__ == "__main__":
    main()