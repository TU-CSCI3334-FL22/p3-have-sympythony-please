from Scanner import *

class Grammar:
    productions = []
    nonterminals = []
    terminals = []

def printTups(tups):
    print(list(map(lambda x: (x[0].name, x[1]),tups)))

def parse(tokens):
    """
    Write functions for each non-terminal in our modified grammar def
    Define non-terminals and terminals as we go
    
    """
    g = Grammar()

    lines,symbols = tokens
    # first figure out terminals and non terminals
    terminals = []
    non_terminals = []

    colon = False
    for tup in lines:
        cat,s = tup
        if cat == TokenCat.SYMBOL:
            terminals.append(tup)
        if cat == TokenCat.DERIVES:
            colon = True
        if cat == TokenCat.SEMICOLON:
            colon = False
        if not colon and cat == TokenCat.SYMBOL:
            non_terminals.append(tup)
    tmp = []
    for x in terminals:
        if x not in non_terminals:
            tmp.append(x)

    terminals = tmp

    # print("terminals:")
    # printTups(terminals)
    # print("nonterminals:")
    # printTups(non_terminals)

    g.terminals = terminals
    g.nonterminals = non_terminals

    return g
    