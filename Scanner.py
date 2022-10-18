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
        tuple(list[list[Token]], list[string]): 
        (list of tokens, list of symbols)
    """
    # read in the file
    file = open(filename, "r")
    
    # dict to represent the lookup table for symbols
    # lookup_tbl = {}

    # set of terminals, not sure if needed
    symbols = set()
    # 2D list of tokens for entire file
    lines = []
    for line in file:

        # if the line is a comment ignore it
        if line and line[0] == '/':
            continue
        
        # output for current line
        tokens = []

        # each token in the line split on whitespace
        parts = line.split()

        for part in parts:
            # converting to lower to simplify checks
            # basically just for handling diff caps for epsilon
            token = part.lower()

            if token not in token_map:
                symbols.add(part)

            # append the token to the list of tokens
            tokens.append(token_map.get(token, Token.SYMBOL))
            
        # if the list isnt empty append it
        if tokens:
            lines.append(tokens)
        
    # return type: (list[list[Token]], list[string])
    return (lines,list(symbols))