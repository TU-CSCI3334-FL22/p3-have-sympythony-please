import string
from Scanner import scanner
from argparse import ArgumentParser, FileType

# read arguments from commandline
# rn only takes one argument, filename
parser = ArgumentParser(description="scans tokens from a grammar")
parser.add_argument('filename', type=str, metavar='FILENAME',
                    help="name of file to be scanned")
args = parser.parse_args()

def main():
    # extract filename from args
    filename = args.filename

    # pass into scanner and pattern-match output
    tokens,lookup_tbl = scanner(filename)
    for line in tokens:
        # enums in python have a builtin .name that returns string
        print(list(map(lambda x: x.name, line)))
    
    print(lookup_tbl)
    
    return 0

if __name__ == "__main__":
    main()
