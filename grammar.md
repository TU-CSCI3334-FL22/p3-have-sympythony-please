### Table 1: MBNF Grammar

| | | | |
| --------|-------|---| ---|
| 1 | Grammar | $\rightarrow$ | ProductionList |
|    2 | ProductionList | $\rightarrow$ |  ProductionSet SEMICOLON|
|    3 |                | $\mid$ | ProductionList ProductionSet  SEMICOLON|
|    4 | ProductionSet | $\rightarrow$ |  SYMBOL  DERIVES  RightHandSide|
|    5 |               | $\mid$ | ProductionSet ALSODERIVES  RightHandSide|
|    6 | RightHandSide | $\rightarrow$ |  SymbolList|
|    7 |               | $\mid$ | EPSILON|
|    8 | SymbolList | $\rightarrow$ |  SymbolList SYMBOL|
|    9 | | $\mid$ | SYMBOL |
