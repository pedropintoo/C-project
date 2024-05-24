# C-project

## Simple test in Grammar
In the directory `src`. Firstly, compile the antlr4 project:
```
antlr4-build
```
Secondly, generate the syntax tree: 
```
antlr4-test AGL program -gui ../doc/ex01.agl        [DONE]
antlr4-test AGL program -gui ../doc/ex02.agl        [DONE]
antlr4-test AGL program -gui ../doc/ex03.agl        [DONE]
```

## Fast test: 
Inside the `src` directory:
```
cat ../doc/ex00.agl | antlr4-run > ../doc/t1.py
```

## Test in Python
Inside the `src` directory:
```
./run ../doc/ex01.agl                                [DONE]
./run ../doc/ex02.agl                                [DONE]
./run ../doc/ex03.agl                                [DONE]
./run ../doc/ex04.agl                                [DONE]
```