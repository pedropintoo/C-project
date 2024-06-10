## Dependências

Para correr o projeto é necessário ter instalado:
 - `antlr4` (com gramática AGL)
 - `python3`
 - `tkinter`
 - `numpy`
 - `antlr4-python3-runtime`

Instalar as dependências do projeto:

```bash
pip install -r requirements.txt  
```

## Teste Simples da Gramática
Entre dentro do diretório root `agl-gg04/`. 

Em primeiro lugar, compile o projeto **antlr4** usando o script `build.sh` que vai dar o *build* necessário, tanto aos ficheiros para a gramática principal $AG_L$, como aos da secundária $xAG_L$:
```
./build
```
Opcionalmente, pode testar a árvore sintática com qualquer exemplo:
```
antlr4-test AGL program -gui ../doc/examples/ex01.agl        
antlr4-test AGL program -gui ../doc/examples/ex02.agl        
antlr4-test AGL program -gui ../doc/examples/ex03.agl        
antlr4-test AGL program -gui ../doc/examples/ex04.agl        
antlr4-test AGL program -gui ../doc/examples/ex05.agl        
antlr4-test AGL program -gui ../doc/examples/ex06.agl        
```

## Experimentar programas em $AG_L$
Após o **antlr4-build**, ainda dentro de `src`, pode experimentar qualquer programa em $AG_L$ usando o script `run.sh`:
```
./run /doc/examples/ex01.agl                                
./run /doc/examples/ex02.agl                                
./run /doc/examples/ex03.agl                                
./run /doc/examples/ex04.agl                                
./run /doc/examples/ex05.agl                                
./run /doc/examples/ex06.agl

### Também há ficheiros extra de exemplo como 
./run /doc/examples/extra/curve_figures_rotate.agl
./run /doc/examples/extra/ifStatement.agl  
./run /doc/examples/extra/model_with_deps.agl
###...
```

## Limpar o Ambiente
