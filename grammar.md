### Table 1: MBNF Grammar

| | | | |
| --------|-------|---| ---|
| 1 | Grammar | $\rightarrow$ | ProductionList |
|    2 | ProductionList | $\rightarrow$ |  ProductionSet SEMICOLON ProductionList|
|    3 |                | $\mid$ | $\epsilon$ |
|    4 | ProductionSet | $\rightarrow$ |  SYMBOL  DERIVES  RightHandSide ProductionSet'|
|    5 | ProductionSet'| $\rightarrow$ | ALSODERIVES RightHandSide ProductionSet'|
|    6 |               | $\mid$ | $\epsilon$ |
|    7 | RightHandSide | $\rightarrow$ |  SymbolList|
|    8 |               | $\mid$ | EPSILON|
|    9 | SymbolList | $\rightarrow$ |  SYMBOL |
|    10| | $\mid$ | SymbolList SYMBOL |
