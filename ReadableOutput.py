import json

def printDict(d):
    for k,v in d.items():
        print(f"  {k}: ", end="")
        print(v)
    print("    " + '-'*30)

def humanReadable(t):

    print("First Table: ")
    printDict(t.firstTable)

    print("Follow Table: ")
    printDict(t.followTable)

    print("Next Table: ")
    printDict(t.nextTable)

    return
