from argparse import ArgumentParser

from src import parser

def parse_args():
    parser = ArgumentParser()

    parser.add_argument("file", help="Path to the SAM file.")

    return parser.parse_args()

if __name__ == "__main__":
    args = parse_args()

    reads = parser.read_sam(args.file)
    stats = parser.parse_reads(reads)

    print(stats)