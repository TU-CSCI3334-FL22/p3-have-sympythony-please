from enum import Enum

class Token(Enum):
    SEMICOLON = 1
    DERIVES = 2
    ALSODERIVES = 3
    EPSILON = 4
    SYMBOL = 5

token_map = {
    ':': Token.DERIVES,
    ';': Token.SEMICOLON,
    '|': Token.ALSODERIVES,
    'epsilon': Token.EPSILON,
}

def scanner(filename):
    """Main Scanner Function

    Args:
        filename (string): name of file we are scanning

    Returns:
        tuple(list[list[Token]], dict[string,int]): 
        (list of tokens, lookup table for symbols)
    """
    # read in the file
    file = open(filename, "r")
    
    # dict to represent the lookup table for symbols
    lookup_tbl = {}

    # set of terminals, not sure if neede
    terminals = set()

    # 2D list of tokens for entire file
    lines = []
    for line in file:
        
        # output for current line
        tokens = []

        # each token in the line split on whitespace
        parts = line.split()
        
        # if the line is a comment ignore it
        if parts and parts[0] == '//':
            continue

        for part in parts:
            # check if the part is a terminal (all caps)
            if part.isupper():
                terminals.add(part)

            # converting to lower to simplify checks
            # basically just for handling diff caps for epsilon
            token = part.lower()

            # if we encounter a token that isnt accounted for in lookup table, add it
            if token not in token_map and part not in lookup_tbl:
                # using len to assign idx instead of storing a local idx var
                lookup_tbl[part] = len(lookup_tbl)

            # append the token to the list of tokens
            tokens.append(token_map.get(token, Token.SYMBOL))
            
        # if the list isnt empty append it
        if tokens:
            lines.append(tokens)

    print(list(terminals))
        
    # return type: (list[list[Token]], dict(string,int))
    return (lines,lookup_tbl)