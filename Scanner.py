
def scanner(filename):
    file = open(filename, "r")
    # loop through the file
    # collect all the symbols into a list first
    
    
    symbols = []
    non_terminals = []

    for line in file:
        parts = line.split()
        for part in parts:
            term = part.lower()
            if term == "|":
                
            elif term == ";":
            elif term == ":":
            elif term == "epsilon":
            else:

