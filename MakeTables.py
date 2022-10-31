
class Tables:
    # symbol -> [terminals / non-terminals that follow]
    firstTable = {}
    followTable = {}
    nextTable = {}
    next_tbl = {}


def cleanGrammar(g):
    line_num = 0
    # rn prods -> [(prod_name, prods)]
    new_prods = []
    for prod_name, prods in g.productions:
        prods = list(map(lambda x: x[1], prods))
        new_prods.append((line_num, prod_name, prods))
        line_num += 1
    g.productions = new_prods


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
        same = True
        for idx,prod_name,prods in reversed(g.productions):
            # print(prods)
            if not prods:
                t.firstTable[prod_name].add(_epsilon)
                continue

            # do we have to handle prod_lst \ {e}
            # rep epsilon using "ε"
            # rep eof using ""

            rhs = t.firstTable[prods[0]].copy()
            rhs.discard(_epsilon)

            k = len(prods)
            i = 0
            while i < k and _epsilon in t.firstTable[prods[i]]:
                for x in t.firstTable[prods[i]]:
                    if x != _epsilon:
                        rhs.add(x)
                i += 1

            if i == k and _epsilon in t.firstTable[prods[k-1]]:
                rhs.add(_epsilon)

            for x in rhs:
                if x not in t.firstTable[prod_name]:
                    same = False
                t.firstTable[prod_name].add(x)

    # print("FIRST TABLE ----------------------------------------")
    # for k,v in t.firstTable.items():
    #     print(k + ": ", end="")
    #     print(v)
    # print("--------------------------------------------")

    return t

def computeFollows(g, t):

    for nt in g.nonterminals:
        t.followTable[nt] = set()

    # assuming first NT is start state
    t.followTable[g.nonterminals[0]].add("")
    same = False
    nt_set = set(g.nonterminals)

    while not same:
        same = True
        for idx,prod_name,prods in g.productions:

            trailer = t.followTable[prod_name].copy()

            k = len(prods)
            for i in range(k-1,-1,-1):
                if prods[i] in nt_set:
                    for x in trailer:
                        if x not in t.followTable[prods[i]]:
                            same = False
                        t.followTable[prods[i]].add(x)

                    if _epsilon in t.firstTable[prods[i]]:
                        for x in t.firstTable[prods[i]]:
                            trailer.add(x)
                        trailer.discard(_epsilon)
                    else:
                        trailer = t.firstTable[prods[i]]
                else:
                    trailer = t.firstTable[prods[i]]
    # print("FOLLOW TABLE ------------------------------")
    # for k,v in t.followTable.items():
    #     print(k + ": ", end="")
    #     print(v)
    # print("-----------------------------------")
    return t



def computeNext(g,t):
    for i in range(len(g.productions)):
        t.nextTable[i] = set()

    for idx,prod_name,prods in g.productions:

        if not prods:
            t.nextTable[idx].add(_epsilon)
            t.nextTable[idx].update(t.followTable[prod_name])
            continue

        rhs = t.nextTable[idx]

        k = len(prods)
        i = 0
        while i < k:
            if _epsilon not in t.firstTable[prods[i]]:
                for x in t.firstTable[prods[i]]:
                    if x != _epsilon:
                        rhs.add(x)
                    i = k
            i += 1

        k = len(prods)
        i = 0
        while i < k and _epsilon in t.firstTable[prods[i]]:
            for x in t.firstTable[prods[i]]:
                if x != _epsilon:
                    rhs.add(x)
            i += 1

        if i == k and _epsilon in t.firstTable[prods[k-1]]:
            rhs.add(_epsilon) #AND the follow of prod_name
            rhs.update(t.followTable[prod_name].copy())


        t.nextTable[idx].update(rhs)



    # print("NEXT TABLE -----------------------------------------------")
    # for k,v in t.nextTable.items():
    #     print(f"{k} | {g.productions[k][1:]} => ", end="")
    #     print(v)
    # print("---------------------------------------------")

    return t
