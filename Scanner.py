from enum import Enum
from lib2to3.pgen2 import token
from mailbox import linesep

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

    # 2D list of tokens for entire file
    lines = []
    for line in file:
        
        # output for current line
        tokens = []

        # each token in the line split on whitespace
        parts = line.split()
        for part in parts:
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
        
    # return type: (list[list[Token]], dict(string,int))
    return (lines,lookup_tbl)