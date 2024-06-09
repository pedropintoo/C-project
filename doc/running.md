## Dependências

Para correr o projeto é necessário ter instalado:
 - `antlr4` (com gramática AGL)
 - `python3`
 - `tkinter`
 - `numpy`

Instalar as dependências do projeto:
<span style="color:red">[POR COMPLETAR!!!]</span>
```bash
pip install -r requirements.txt  
```

## Simple test in Grammar
In the directory `src`. Firstly, compile the antlr4 project:
```
antlr4-build
```
Secondly, generate the syntax tree: 
```
antlr4-test AGL program -gui ../doc/examples/ex01.agl        
antlr4-test AGL program -gui ../doc/examples/ex02.agl        
antlr4-test AGL program -gui ../doc/examples/ex03.agl        
antlr4-test AGL program -gui ../doc/examples/ex04.agl        
antlr4-test AGL program -gui ../doc/examples/ex05.agl        
antlr4-test AGL program -gui ../doc/examples/ex06.agl        
```

## Compile and Run the project
Inside the `src` directory:
```
./run ../doc/examples/ex01.agl                                
./run ../doc/examples/ex02.agl                                
./run ../doc/examples/ex03.agl                                
./run ../doc/examples/ex04.agl                                
./run ../doc/examples/ex05.agl                                
./run ../doc/examples/ex06.agl                                
```
