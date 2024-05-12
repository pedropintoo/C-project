# C-project

## Simple test in Grammar
In the directory `src`. Firstly, compile the antlr4 project:
```
antlr4-build
```
Secondly, generate the syntax tree: 
```
antlr4-test -gui ../doc/ex01.agl        [DONE]
antlr4-test -gui ../doc/ex02.agl        [X]
antlr4-test -gui ../doc/ex03.agl        [X]
```