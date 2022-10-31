from enum import Enum

class TokenCat(Enum):
    SEMICOLON = 1
    DERIVES = 2
    ALSODERIVES = 3
    EPSILON = 4
    SYMBOL = 5

# [(TokenCat, "name")]

token_map = {
    ':': TokenCat.DERIVES,
    ';': TokenCat.SEMICOLON,
    '|': TokenCat.ALSODERIVES,
    # 'epsilon': TokenCat.EPSILON,
}

valid_chars = {";","|",":"}
def custom_split(line):
    output = []
    part = ""
    for c in line:
        if not c.isalnum():
            if part:
                output.append(part)
            if c in valid_chars:
                output.append(c)
            part = ""
        else:
            part += c
    if part:
        output.append(part)
    return output


def scanner(file):
    """Main Scanner Function

    Args:
        file: file we are scanning

    Returns:
        tuple(list[list[Token]], list[string]): 
        (list of tokens, list of symbols)
    """
    
    symbols = set()
    # 2D list of tokens for entire file
    lines = []
    for line in file:

        # if the line is a comment ignore it
        if line and line[0] == '/':
            continue

        # each token in the line split on whitespace
        parts = custom_split(line)
        # _parts = line.split()
        # print(_parts)
        # print(parts)

        for part in parts:
            # converting to lower to simplify checks
            # basically just for handling diff caps for epsilon
            token = part.lower()

            if token not in token_map:
                symbols.add(part)

            # append the token to the list of tokens
            lines.append((token_map.get(token, TokenCat.SYMBOL), part))
            
        # if the list isnt empty append it
        
    # return type: (list[list[Token]], list[string])
    return (lines,list(symbols))