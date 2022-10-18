class Grammar:
    productions = []
    nonterminals = []
    terminals = []

def parse(tokens):
    lines,symbols = tokens
    # first figure out terminals and non terminals
    terminals = []
    non_terminals = []
    

    