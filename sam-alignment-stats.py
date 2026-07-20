from argparse import ArgumentParser

from src import parser

def parse_args():
    parser = ArgumentParser()

    parser.add_argument("file", help="Path to the SAM file.")

    return parser.parse_args()

if __name__ == "__main__":
    args = parse_args()

    sequence = parser.read_sam(args.file)

    print(sequence)