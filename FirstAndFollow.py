
class Tables:
    # symbol -> [terminals / non-terminals that follow]
    firstTable = {}
    followTable = {}
    nextTable = {}

_epsilon = 'ε'
# _epsilon = 'apple'
def computeFirsts(g):
    # g -> list of productions -> list of terminals -> list of non-terminals
    t = Tables()
    for terminal in g.terminals:
        if terminal.lower() == 'epsilon':
            continue
        else:
            t.firstTable[terminal] = set()
            t.firstTable[terminal].add(terminal)
    
    t.firstTable[_epsilon] = set(_epsilon)
    t.firstTable[""] = set("")

    for nt in g.nonterminals:
        t.firstTable[nt] = set()

    # keep some boolean flag and whenever we update it we set to True
    same = False
    while not same:
        for prod_name,prods in reversed(g.productions):
            prods = list(map(lambda x: x[1], prods))
            # print(prods)
            if not prods:
                t.firstTable[prod_name].add(_epsilon)
                continue
            
            # do we have to handle prod_lst \ {e}
            # rep epsilon using "ε"
            # rep eof using ""

            rhs = t.firstTable[prods[0]]
            rhs.discard(_epsilon)

            k = len(prods)
            i = 1
            while i < k and _epsilon in t.firstTable[prods[i]]:
                for x in t.firstTable[prods[i]]:
                    if x != _epsilon:
                        rhs.add(x)
                i += 1
                
            if i == k and _epsilon in t.firstTable[prods[k-1]]:
                rhs.add(_epsilon)

            for x in rhs:
                t.firstTable[prod_name].add(x)

            same = True

    for k,v in t.firstTable.items():
        print(k + ": ", end="")
        print(v)

    return t.firstTable

def computeFollows(grammar):
    return