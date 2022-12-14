from Scanner import *

class Grammar:
    productions = []
    nonterminals = []
    terminals = []

    def __str__(self):
        # tostring for a Grammar
        return str(self.productions)

def printTups(tups):
    print(list(map(lambda x: (x[1]),tups)))

def parse(tokens):
    """
    Write functions for each non-terminal in our modified grammar def
    Define non-terminals and terminals as we go
    
    """
    g = Grammar()
    lines,symbols = tokens
    
    def productionList(tups):
        # list of productions to return
        prod_list = []
        # first item expected is production set
        while tups:
            prod_set = productionSet(tups)
            for sub_lst in prod_set:
                prod_list.append(sub_lst)
            if tups[0][0] != TokenCat.SEMICOLON:
                quit()
            tups.pop(0)

        return prod_list    

    def productionSet(tups):
        derivations = []

        # expect non-terminal symbol first
        if tups[0][0] != TokenCat.SYMBOL:
            print("didnt find symbol")
            quit()
        non_terminal = tups[0][1]
        g.nonterminals.append(non_terminal)
        tups.pop(0)

        # expects derives next
        if tups[0][0] != TokenCat.DERIVES:
            print("didnt find derives")
            quit()
        tups.pop(0)

        right_hand_side = rhs(tups)
        derivations.append((non_terminal, right_hand_side))
        while tups[0][0] == TokenCat.ALSODERIVES:
            derivations.append((non_terminal, productionSetPrime(tups)))

        return derivations

    def productionSetPrime(tups):
        cat,s = tups[0]
        # I dont know how to handle nothing correctly
        if cat == TokenCat.SEMICOLON:
            return
        if cat != TokenCat.ALSODERIVES:
            # pSetPrime expects alsoderives here
            print("didnt find alsoder")
            quit()
        tups.pop(0)
        return rhs(tups)

    def rhs(tups):
        if tups[0][0] == TokenCat.SEMICOLON:
            # checking if goes to nothing
            return []
        else:
            return symbolList(tups)

    def symbolList(tups):
        sym_lst = []
        while(tups[0][0] == TokenCat.SYMBOL):
            # build symbol list
            if tups[0][1].lower() != 'epsilon': 
                sym_lst.append(tups[0])
                g.terminals.append(tups[0][1])
            tups.pop(0)
        cat,_ = tups[0]
        if cat != TokenCat.SEMICOLON and cat != TokenCat.ALSODERIVES:
            quit()
        return sym_lst

    def quit():
        print("exiting")
        exit(0)

    g.productions = productionList(lines)
    s = set(g.nonterminals)
    g.terminals = list(set([x for x in g.terminals if x not in s]))
    
    return g