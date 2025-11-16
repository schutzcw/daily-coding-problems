import argparse
import os
import pathlib
import sys

def main() -> None:
    """ 
    description
    
    :param name:
    :return
    """
    
    parser = argparse.ArgumentParser()
    parser.add_argument("param", help="description")
    args = parser.parse_args()
    # args.param

    # fill in here

if __name__ == "__main__":
    main()
