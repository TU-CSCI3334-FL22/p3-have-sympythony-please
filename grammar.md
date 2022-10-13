### Table 1: MBNF Grammar

| | | | |
| --------|-------|---| ---|
| 1 | Grammar | $\rightarrow$ | ProductionList |
|    2 | ProductionList | $\rightarrow$ |  ProductionSet SEMICOLON|
|    3 |                | $\mid$ | ProductionList ProductionSet  SEMICOLON|
|    4 | ProductionSet | $\rightarrow$ |  SYMBOL  DERIVES  RightHandSide ProductionSet'|
|    5 | ProductionSet'| $\rightarrow$ | ALSODERIVES RightHandSide ProductionSet'|
|    5 |               | $\mid$ | EPSILON|
|    6 | RightHandSide | $\rightarrow$ |  SymbolList|
|    7 |               | $\mid$ | EPSILON|
|    8 | SymbolList | $\rightarrow$ |  SYMBOL |
|    9 | | $\mid$ | SymbolList SYMBOL |
