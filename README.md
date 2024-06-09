# Tema **AGL**, grupo **agl-gg04**


## Documentação extra

 - Análise semântica - [doc/analise_semantica.md](doc/analise_semantica.md) 
 - Exemplos AGL e xAGL - [doc/examples](doc/examples.md)


## Estrutura do repositório
O repositório está organizado da seguinte forma:
- `doc/` contém a documentação do projeto.
- `doc/examples/` contém exemplos de código AGL e xAGL.
- `src/` contém o código fonte do projeto.
- `src/tests/` contém os testes do projeto (nomeadamente análise semântica).

## Dependências

Para correr o projeto é necessário ter instalado:
 - `antlr4` (com gramática AGL)
 - `python3`
 - `tkinter`
 - `numpy`


Instalar as dependências do projeto:
```bash
pip install -r requirements.txt [POR COMPLETAR!!!]
```

## Relatório

- Use esta secção para fazer um relatório sucinto mas explicativo dos objetivos concretizados.

## Contribuições

- Use esta secção para expôr as contribuições individuais dos vários elementos do grupo e que
  justificam as participações individuais globais apresentadas no início.

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

## To do

```
All agl vars must start with `__agl__`               [X]
to avoid conflicts with python vars.
```


## Constituição dos grupos e participação individual global

| NMec | Nome | Participação |
|:---:|:---|:---:|
| 115637 | GIOVANNI PEREIRA SANTOS | 0.0% |
| 113893 | GUILHERME FERREIRA SANTOS | 0.0% |
| 104384 | JOÃO PEDRO AZEVEDO PINTO | 0.0% |
| 114547 | JOÃO PEDRO FERREIRA MONTEIRO | 0.0% |
| 113278 | JORGE GUILHERME CONCEIÇÃO DOMINGUES | 0.0% |
| 115304 | PEDRO MIGUEL AZEVEDO PINTO | 0.0% |
