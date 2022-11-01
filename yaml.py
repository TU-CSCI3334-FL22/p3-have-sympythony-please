from os import terminal_size
import yaml 

_epsilon = 'ε'
def makeNextTable(tbl,g):
    invalid = False
    # print("here ")
    i = 0
    terminal_map = {}
    for t in g.terminals + [""]:
        terminal_map[t] = i
        i += 1
    
    
    g.next_tbl = {}
    for nt in g.nonterminals:
        g.next_tbl[nt] = [-1 for _ in range(len(g.terminals)+1)]

    # print(tbl.nextTable)
    for idx,terminals in tbl.nextTable.items():
        nt = g.productions[idx][1]
        for terminal in terminals:
            if terminal == _epsilon:
                continue
            # print(f"storing {terminal} at rule {idx} in nt {nt}")
            if g.next_tbl[nt][terminal_map[terminal]] != -1 and terminal != "":
                invalid = True
                #print("index " ,idx ,"nt ", nt, "terminal ", terminal)
            g.next_tbl[nt][terminal_map[terminal]] = idx
        # print(f"{idx} {nt}")

    # print(g.terminals + [""])
    # for k,v in g.next_tbl.items():
    #     print(k + ": ", end="")
    #     print(v)
    if invalid:
        print(" is invalid")
    return

def yaml_print(tables, g):

    print("terminals: ", end="")
    print("[", end="")
    k=1
    for terminal in g.terminals:
        print(terminal, end="")
        if k < len(g.terminals):
            print(", ", end="")
        k+=1
    print("]")

    print("non-terminals: ", end="")
    print("[", end="")
    k=1
    for nonterminal in g.nonterminals:
        print(nonterminal, end="")
        if k < len(g.nonterminals):
            print(", ", end="")
        k+=1
    print("]")

    print("eof-marker: \"\"")
    print("error-marker: --")

    print("start-symbol: ", end="")
    print(g.nonterminals[0])

    print("productions: ")
    for idx,prod_name,prods in g.productions:
        print(" ",idx , ": {", end="")
        print(prod_name, ": [", end="")
        k = 1
        for p in prods: 
            print(p, end="")
            if k < len(prods):
                print(", ", end="")
            k+=1

        print("]}")

    print("table: ")
    i = 0
    terminal_map = {}
    for t in g.terminals + [""]:
        terminal_map[t] = i
        i += 1
    for k,v in g.next_tbl.items():
        print(" " , k + ": {", end="")
        n = 1
        for t in g.terminals + [""]:
            num = v[terminal_map[t]]
            if(t == ""):
                print("\"\"", end="")
            else:
                print(t, end = "")
            print(": ", end = "")
            if(num == -1):
                print("--", end="")
            else:
                print(num, end = "")
            if(n < len(v)):
                print(", ", end = "")
            n+=1
        print("}")






        #for idx,terminals in tables.nextTable.items():
        #    nt = g.productions[idx][1]
        #    for terminal in terminals:
        #        if terminal == _epsilon:
        #            continue
        #        print(terminal, ": ", idx, end="")
        #        if(k < len(g.terminals)):
        #            print(", ", end="")
        #        #print(f"storing {terminal} at rule {idx} in nt {nt}")
        #        k+=1
        #print("}")


    return