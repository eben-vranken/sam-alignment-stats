def read_sam(file_path):
    sequence = ""

    try:
        with open(file_path) as fp:
            for line in fp:
                sequence += line.strip()
    except FileNotFoundError:
        print("File path does not point to an existing file!")
        exit(1)
        
    return sequence

def parse_sam():
    pass