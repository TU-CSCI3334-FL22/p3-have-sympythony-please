from tokenize import Token
from Scanner import *

class Grammar:
    productions = []
    nonterminals = []
    terminals = []

    def __str__(self):
        # tostring for a Grammar
        return str(self.productions)

def printTups(tups):
    print(list(map(lambda x: (x[0].name, x[1]),tups)))

def parse(tokens):
    """
    Write functions for each non-terminal in our modified grammar def
    Define non-terminals and terminals as we go
    
    """
    g = Grammar()
    lines,symbols = tokens

    # if we've not found a colon we must be looking at a non_terminal
    # and the beginning of a new production
    # if we see an "alsoderives" we add a new production with same LHS and new RHS
    derivation = False
    production_name = "default"
    cur_production = []
    for tup in lines:
        cat,s = tup

        match cat:
            case TokenCat.SYMBOL:
                # if we see a symbol its either before or after a colon
                if derivation:
                    # derivation of a production
                    g.terminals.append(s)
                    cur_production.append(s)
                else:
                    # new non-terminal & derivation
                    g.nonterminals.append(s)
                    production_name = s
            case TokenCat.DERIVES:
                derivation = True
            case TokenCat.ALSODERIVES:
                g.productions.append((production_name, cur_production))
                cur_production = []
            case TokenCat.SEMICOLON:
                derivation = False
                g.productions.append((production_name, cur_production))
                cur_production = []
                production_name = "default"

    s = set(g.nonterminals)
    g.terminals = [x for x in g.terminals if x not in s]

    print(g)
    return g
    