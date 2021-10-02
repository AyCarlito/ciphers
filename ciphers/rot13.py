import caesar
import argparse

def get_arguments():
    parser = argparse.ArgumentParser(description="ROT13")
    parser.add_argument("m", type=str, help="Message")
    args = parser.parse_args()
    return args

def main():
    args = get_arguments()
    caesar.decode(caesar.encode(args.m, 13), 13)
    
if __name__ == "__main__":
    main()
