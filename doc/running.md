## Dependências

Para correr o projeto é necessário ter instalado:
 - `antlr4`
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

Em primeiro lugar, compile o projeto **antlr4** usando o script `build` que vai dar o *build* necessário, tanto aos ficheiros para a gramática principal $AG_L$, como aos da secundária $xAG_L$:
```bash
./build
```

## Experimentar programas em $AG_L$
Após o **antlr4-build**, ainda dentro de `agl-gg04/`, pode experimentar qualquer programa em $AG_L$ usando o script `run`:
```bash
./run doc/examples/ex00.agl  # default values
./run doc/examples/ex01.agl                                
./run doc/examples/ex02.agl                                
./run doc/examples/ex03.agl                                
./run doc/examples/ex04.agl                                
./run doc/examples/ex05.agl                                
./run doc/examples/ex06.agl
./run doc/examples/hanoi.agl # desafio
```

Para além de exemplos base, no diretório `doc/examples/extra` existem extensões de exemplos base, outros exemplos diferenciados, entre outras coisas. Como por exemplo: 
```bash
./run doc/examples/extra/ex02_diff.agl
./run doc/examples/extra/ex04_extra.agl
./run doc/examples/extra/rotate_models.agl
./run doc/examples/extra/model_with_rotation.agl
./run doc/examples/extra/curve_figures_rotate.agl
./run doc/examples/extra/rotate_deepcopy.agl

```

## Testar a gramática
Opcionalmente, dentro do diretório `src` pode testar a árvore sintática com qualquer exemplo:
```bash
antlr4-test AGL program -gui ../doc/examples/ex01.agl        
antlr4-test AGL program -gui ../doc/examples/ex02.agl        
antlr4-test AGL program -gui ../doc/examples/ex03.agl        
antlr4-test AGL program -gui ../doc/examples/ex04.agl        
antlr4-test AGL program -gui ../doc/examples/ex05.agl        
antlr4-test AGL program -gui ../doc/examples/ex06.agl
antlr4-test AGL program -gui ../doc/examples/hanoi.agl        
```

## Testar a Análise Semântica
De modo a testar a **Análise Semântica** do **Compilador**, foram desenvolvidos alguns testes que avaliam, tanto se a análise semântica **validou** corretamente um programa, como também se **invalidou** corretamente um programa:

Entre no diretório `src/`:
```bash
cd src 
```
Experimente os testes:

```bash
./tests/run-tests.sh
```
#### Resultados
Os resultados dos testes devem ser apresentados no terminal. A confirmação de que os testes correram da maneira desejada é dada pela sua cor devido ás verificações de **validação** ou **invalidação** referidos anteriormente. Assim, os testes de **validação** estão corretos se aparecer [**<span style="color:green">OK</span>**] **(a verde)**, e os testes de **invalidação** estão corretos se aparecer [**<span style="color:green">FAIL</span>**] **(a verde)**.

Qualquer outro *output* como, **<span style="color:red">OK</span>** ou **<span style="color:red">FAIL</span>** a **vermelho**, significa que a análise semântica falhou pois, ou validou algo que não devia ser validado ou falhou um teste que devia ter sido validado, respetivamente.


## Limpar os Ficheiros de Compilação
Para limpar os ficheiros gerados quando se fez o **build**, pode usar o script `clean` caso não queira fazer mais testes:

Certifique-se de que está no diretório root `agl-gg04/`
```bash
./clean
```
