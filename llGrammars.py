from Scanner import *
from Parser import *

class Token:
    type = ""

class Tables:
    firstTable = {}
    followTable = {}
    nextTable = {}

def grammar_scan(contents):
    print("Scan contents into a list of tokens return it")
    lines,symbols = scanner(contents)
    # lines is => [(TokenCat, string)]
    print(list(map(lambda x: (x[0].name, x[1]),lines)))
    # print(list(map(lambda x,y: x.name, lines)))

    return (lines,symbols)

def grammar_parse(tokens):
    print("Read tokens into a grammar")
    return parse(tokens)

def fixLL(ir):
    return ir

def make_tables(ir, worklist):
    if(worklist):
        sys.exit("Worklists not supported yet!")
    else:
        print("Make and return the appropriate tables")
        return(Tables())

        
def print_tables(tables):
   print("Print tables in human-readable format")

def print_yaml(tables):
    print("Print tables in yaml format, or error if the involution of the next table fails")
   
def usage():
    print("error and help message here")
