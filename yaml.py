from os import terminal_size
import yaml 

_epsilon = 'ε'
def makeNextTable(tbl,g):
    print("here ")
    i = 0
    terminal_map = {}
    for t in g.terminals + [_epsilon, ""]:
        terminal_map[t] = i
        i += 1
    
    
    next_tbl = {}
    for nt in g.nonterminals:
        next_tbl[nt] = [-1 for _ in range(len(g.terminals)+2)]

    print(tbl.nextTable)
    for idx,terminals in tbl.nextTable.items():
        nt = g.productions[idx][1]
        for terminal in terminals:
            next_tbl[nt][terminal_map[terminal]] = idx
        print(f"{idx} {nt}")
    



    print(g.terminals + [_epsilon, ""])
    for k,v in next_tbl.items():
        print(k + ": ", end="")
        print(v)
    return

def yaml_print(tables):
    print("got here")

    return