# Tema **AGL**, grupo **agl-gg04**

## <span style="color:red">[TO DO]</span>

 - __agl__ nos modelos!
 - Default values for agl vars.                         
 - Join all versions of interpreter / semantic analysis and compiler in one branch.
 - deepcopy for all objects. (ST is fixed to Pacman(). Must create a createObject for each and copyAttributesTo)

## Documentação extra

 - Análise semântica - [doc/semantic_check.md](doc/semantic_check.md)  <span style="color:red">[POR COMPLETAR!!!]</span>
 - Exemplos AGL e xAGL - [doc/examples](doc/examples/) <span style="color:red">[POR COMPLETAR!!!]</span>
 - Tutorial de execução - [doc/running.md](doc/running.md) <span style="color:red">[POR COMPLETAR!!!]</span>

## Estrutura do repositório
O repositório está organizado da seguinte forma:

- `doc/` contém a documentação do projeto.
- `doc/examples/` contém exemplos de código AGL e xAGL.
- `doc/examples/demo/` contém videos de demonstração da linguagem AGL.
- `src/` contém o código fonte do projeto.
- `src/tests/` contém os testes do projeto (nomeadamente análise semântica).


## Relatório


### Introdução
Este documento apresenta o relatório do projeto final do grupo AGL-gg04 para a disciplina de Compiladores do ano letivo 2023/2024, focado na criação da linguagem de programação **$AG_L$ (*animated graphics language*)**. 

- O objetivo geral deste trabalho foi o desenvolvimento de um ambiente de programação, constituído pela linguagem de programação $AG_L$ (*animated graphics language*) e correspondentes ferramentas de compilação, que permite a criação de programas na linguagem de programação genérica *Python3*, usando a biblioteca *tkinter*, que, quando executados, permitem a visualização, com possível animação e interação, de *gráficos 2D*.

- A linguagem assume (implicitamente) a existência de uma área de desenho, *canvas*, com dimensões ilimitadas, sobre a qual se podem instanciar (desenhar) figuras gráficas 2D. Podem também ser instanciadas vistas (*View*), que permitem capturar o estado do *canvas* numa dada região, com um determinado zoom e num determinado instante no tempo. Há um conjunto base de modelos gráficos pré-definidos, mas a linguagem possui mecanismos construtivos que permitem definir outros. As instâncias dos modelos gráficos podem, ao longo do tempo, mudar a sua posição e as suas propriedades, mas, apenas quando uma vista é *refrescada* é que as alterações são capturadas por essa vista.

- Para além disso, a linguagem principal permite a importação de elementos auxiliares através de *descrições* numa linguagem secundária, cujos elementos, em *runtime*, possam ser carregados pelo programa final. Em concreto, foi definida uma linguagem secundária, aqui designada por $xAG_L$, associada a ficheiros com a extensão *xagl*, que permite auxilar a linguagem principal $AG_L$ de alguma maneira (por exemplo, definindo modelos). O resultado desta tarefa é a gramática da linguagem $xAG_L$, a construção gramatical na linguagem $AG_L$ que permite fazer a importação de descrições em $xAG_L$, o interpretador que permite fazer o parsing de descrições $xAG_L$, e exemplos ilustrando a sua utilização. Este interpretador foi desenvolvido na linguagem destino (neste caso *Python3*) e não na linguagem de trabalho (neste caso *Java*), uma vez que a interpretação é feita em *runtime*.

**Torres de Hanoi**: demonstra a facilidade na criação de programas complexos em $AG_L$. Utilizando multiplas vistas e modelos que facilitam a criação de animações complexas. 
![Intro.gif](doc/examples/demo/Intro.gif)

### Requesitos do projeto

Foram definidos 4 níveis para a realização deste projeto:

#### Nível mínimo  [<span style="color:green">DONE</span>]

  - Suporte para comentários, de linha e de bloco, tal como ilustrado no exemplos.
  - Instanciação de uma vista (*View*) sobre a área de desenho (*canvas*). As vistas devem portam as ações de *move*, *refresh*, *wait* e *close*. Neste nível, considerámos que existe apenas uma vista.
  - Instanciação dos modelos gráficos base *Dot*, *Line*, *Circle*, *Rectangle*, *Ellipse*, *Text*, *Arc*, *ArcChord* e *PieSlice*. Todos estes modelos têm implicitamente um ponto de referência, cuja localização no canvas será indicada aquando da sua instanciação. Todos os objetos gráficos devem suportar a ação de *move*. Todos os objetos gráficos possuem um conjunto de propriedades, que podem ser alteradas em tempo de execução.
  - Suporte dos tipos de dados *Integer*, *Number*, *Point*, *Vector*, *String*, e *Time* e da instanciação de objetos destes tipos. Suporte de expressões envolvendo estes tipos de dados.
  - Suporte da construção *with*.
  - Uma construção gramatical repetitiva *for*, para iterar sobre uma sequência de valores.
  - Verificação semântica no uso de variáveis e de expressões e na manipulação de propriedades.
  - Definição e implementação de uma linguagem secundária, aqui designada por $xAG_L$, associada a ficheiros com a extensão *xagl*.


#### Nível desejável  [<span style="color:green">DONE</span>]

  - Instanciação dos modelos gráficos base *Polyline*, *Spline*, *Polygon* e *Blob*. Todos estes modelos têm implicitamente um ponto de referência, cuja localização no *canvas* será indicada aquando da sua instanciação. Todos os objetos gráficos devem suportar a ação de *move*. Todos os objetos gráficos possuem um conjunto de propriedades, que podem ser alteradas em tempo de execução.
  - O tipo de dados *Boolean* e a manipulação de expressões booleanas.
  - Uma construção gramatical condicional. Neste nível, considerámos apenas a construção *if-else* com suporte para expressões booleanas, incluindo *and*, *or*, *not*, *==*, *!=*, *<*, *<=*, *>* e *>=*. Com as respetivas prioridades.
  - Uma construção gramatical repetitiva baseada em predicado (condição de término ou de continuação). Neste nível, considerámos as construções *while*, *repeat-until*.
  - Suporte para a especificação de vetores (*Vector*) em coordenadas polares.
  - A possibilidade de definição de novos modelos (associada à palavra-chave *Model*), que permita agregar instâncias de outros modelos, base ou definidos anteriomente, numa nova entidade. Todas as propriedades destes novos modelos serão definidas aquando da sua conceção. Deve ser possı́vel fazer depender as propriedades dos modelos incorporados de propriedades do modelo principal. O novo modelo poderá ser depois instanciado.
  - Suporte para estrutura de dados iterável (array, lista, ...) e de mecanismos de instanciação, acesso e manipulação dos seus elementos. Neste nível, considerámos apenas a construção de *array* (apenas aceita elementos do mesmo tipo).
  - Possibilidade de aplicar as ações move, refresh e close diretamente a uma lista de objetos.


#### Nível adicional  [<span style="color:green">DONE</span>]

  - Suporte para a rotação de objetos gráficos. Neste nível, houve a necessidade de redefinir internamente a forma como os objetos gráficos são representados (para permitir rotação de TODOS os objetos). Considerámos também a rotação de modelos que contêm outros modelos através do seu ponto de referência.
  - Suporte para várias vistas.
  - Suporte para a operação *deepcopy*, que permite a *cópia profunda* de objetos gráficos. Facilitação na duplicação de objetos gráficos complicados.
  - Definição de palavras reservadas para a linguagem principal $AG_L$. As palavras reservadas da linguagem destino (neste caso *Python3*) não são um subconjunto das palavras reservadas da linguagem principal $AG_L$. (Por exemplo, a palavra *return* é uma palavra reservada da linguagem destino, mas não da linguagem principal $AG_L$).
  - O tipo de dados *Enum* e a manipulação de variáveis enumeradas.

#### Desafios  [<span style="color:green">DONE</span>]

  - Criação de uma animação interativa que permita a um utilizador resolver as torres de Hanoi.

<hr>

### Nível mínimo

> Neste nível, o nosso grupo focou-se na implementação dos requisitos mínimos, tendo em conta a instânciação de uma vista, a instânciação dos modelos gráficos base, a manipulação de tipos de dados, a construção *with*, a construção *for*, a verificação semântica e a definição e implementação de uma linguagem secundária.

#### __Instanciação e Definição | Tipos de Dados__
---
- Para instanciar um tipo de dados/objetos usa-se o operador **(:)**
- Para fazer a atribuição de algum valor usa-se o operador **(=)**
  
Neste nível, foram implementados 6 tipos principais de dados:
- **Integer**: Representa um número inteiro; 
- **Number**: Representa um número inteiro ou número real;
```
#Instanciação e Operações

a : Integer = 3
b : Number = 2.0*a;
c : Integer = 2*3;
d : Number = 2.0*3.0;

e : Number = a + b;
f : Number = c - b;
g : Number = d / 2.0;
```  

- **String**: Sequência de caractéres;
```
nome : String = "Nome";
```
antlr4-test AGL program -gui ../doc/ex01.agl        [DONE]
antlr4-test AGL program -gui ../doc/ex02.agl        [DONE]
antlr4-test AGL program -gui ../doc/ex03.agl        [DONE]
```

#### __Definição de uma View__
---
  Para se definir uma *View* é necessário ter em conta diversas propriedades, cada uma com um tipo e valor *default*:
  - Ox: Number = 0.0 , Oy: Number = 0.0 | O ponto do canvas do centro da janela da *View*
  - width: Integer = 201 | Número de pixéis numa linha
  - height: Integer = 201 | Número de pixéis numa coluna
  - title: String = "No title" | O título da janela
  - background: String = "black" | A cor do fundo da *View*
  
  (O operador **with** possibilita a atribuição de valores para quaisquer propriedades de um objeto na sua instanciação)

Exemplo:
```
view : View with {
  width = 601;
  height = 601;
  title = "Title for View";
  background = "blue";
}
```
A *View* suporta ações como **move** *(explicado mais á frente)*, **refresh**, **wait** e **close**

| Instrução | Definição | 
| :---: | :---: |
| ```refresh view after 100 ms``` | Atualiza a **View** após 100 milissegundos, ou seja, quaisquer alterações em objetos são mostradas após o tempo definido em milissegundos |
| ```refresh view after 10 s``` | Faz **refresh** da **View** após 10 segundos | 
| ```p : Point = wait mouse click``` | Espera um click pelo utilizador na **View** e atribui as coordenadas a ao ponto **p** | 
| ```close view``` | Fecha a janela da **View** | 


#### __Definição de Objetos do Canvas__
---
Neste nível, foram desenvolvidos alguns tipos de objeto principais como:
  - **Line** : Representa uma linha reta que conecta o seu ponto de referência com outro ponto dado por um vetor *length*

(Para definir o ponto de referência de um objeto usa-se o operador **at**)
```
linha : Line at (10, 20) with {
  length = (30, 40);
  fill = "red";
}
```
- **Rectangle** : Representa um retângulo referenciado pelo seu ponto do centro e um vetor *length* a apontar para o canto superior direito a partir desse ponto
```
retangulo : Rectangle at (10, 20) with {
  length = (30, 40);
  fill = "blue";
}
```
- **Ellipse** : Representa uma elipse que é referenciada pelo seu ponto central e um vetor *length* a apontar para o canto superior direito do retangulo em que a elipse se insere
```
elipse : Ellipse at (10, 20) with {
  length = (30, 40);
  fill = "green";
}
```
- **Arc**, **ArcChord** e **PieSlice** são derivadas da **Ellipse** mas, para além da sua referência e *length*, estes tipos de objeto são definidos por um ângulo de **start** (ângulo inicial a partir do qual se vai desenhar a parte da elipse correspondente) e um **extent** (ângulo que a figura vai tomar a contar a partir do **start**)
- **Arc**: Representa o arco de uma elipse, não fechado, e pode ter como atributo a cor da sua **outline**
```
arco : Arc at (10, 20) with {
  length = (30, 40);
  start = 0;
  extent = 90;
  outline = "tomato";
}
```
- **ArcChord**: Representa o arco de uma elipse, no entanto, as suas extremidades conectam-se diretamente formando uma reta
```
arccord : ArcChord at (10, 20) with {
  length = (30, 40);
  start = 0;
  extent = 90;
  fill = "cyan";
}
```
- **PieSlice**: Representa o arco de uma elipse, no entanto, as suas extremidades conectam-se ao seu **centro** 
```
pieslice : PieSlice at (10, 20) with {
  length = (30, 40);
  start = 0;
  extent = 90;
  fill = "purple";
}
```
- **Text**: Representa um texto que pode ser colocado em qualquer lugar do canvas
```
texto : Text at (10, 20) with {
  text = "Texto";
  fill = "red";
}
```
- **Dot**: Representa um ponto no canvas
```
ponto : Dot at (10, 20) with {
  fill = "black";
}
```
#### Todos estes objetos e Views suportam a operação **move** e **with**
---

Tendo como referência o objeto seguinte:
```
objeto : Rectange at (10, 20) with {
  length = (30, 40);
  fill = "blue";
}
```

| Instrução | Definição |
| :---:     | :---:     |
| ```move objeto to (0, 0)``` | Move diretamente o **objeto** para a posição **(0,0)**|
| ```move objeto by (5, 5)``` | Move o **objeto** segundo o vetor **(5,5)**, ou seja, iria ser deslocado para **(15,25)**|
| ```with objeto do { length = (15, 20); fill = "red"; }```| Altera as propriedades do **objeto** em runtime|

#### Construção repetitiva FOR
---
O **for** é capaz de repetir as instruções dentro dele através da iteração sobre uma sequência de valores:
- **Valor inicial**;
- **Valor final** - Exclusivo, ou seja, a variável fica com o valor de **Valor final** - 1;
- **Passo** - Opcional com valor de *default* =  1;
```
# Mostra na consola de 0 a 9 de 3 em 3
for i in 0..10..3 {
  print i
}
```
### Análise Semântica
---
```
[TODO]
```

### Linguagem Secundária $xAG_L$
---
```
[TODO]
```


### Nível desejável

> Neste nível, o nosso grupo focou-se na implementação dos requisitos desejáveis, tendo em conta a instânciação dos modelos gráficos base, a manipulação de tipos de dados, a construção *if-else*, a construção *while*, a construção *repeat-until*, a especificação de vetores (*Vector*), a definição de novos modelos, a estrutura de dados iterável e a aplicação das ações move, refresh e close diretamente a uma lista de objetos.

#### __Definição de Novos Tipos/Estruturas de Dados__
---
Neste nível, foram adicionados novos tipos de dados e o seu suporte como:
- **Boolean**: Representa uma expressão que pode resultar nos valores **True** ou **False**. Para além disso suporta operações como **and**, **or**, **not**, **==**, **!=**, **<**, **<=**, **>** e **>=**. Com as respetivas prioridades, cuja ordem é a seguinte: **not**, **and**, **or**, (**>** | **>=** | **<** | **<=**), (**==** | **!=**). Levámos em conta o mais comum em linguagens genéricas;

```
# Exemplos de expressão Boolean
var1 : Boolean = True;      #var1 = True
var2 : Boolean = 5+3 == 8;  #var2 = True
var3 : Boolean = 1 == 1 and (2 == 1+1 or 2!=2); #var3 = True
var4 : Boolean = not True; #var4 = False
var5 : Boolean = 4 <= 2 or 6 > 10; #var5 = False
```
- **Array**: Representa a estrutura de dados **lista** só de um único tipo;
```
# Exemplos de uso de Array
[TODO]
```
  - Atualização no **Vector**: Suporte para especificação opcional em coordenadas polares.
  
```
#Coordenadas polares (ângulo:tamanho) 
vetor : Vector = 50:10; 
```
#### __Suporte para Construção Condicional__
---
- **If-Else**: Permite a execução de um bloco de código se uma condição **Boolean** for verdade dentro do **if** e executa o bloco de código dentro do **else** caso contrário
```
# Exemplo de If-Else
var : Integer = 5;
if var < 10 do {
  print "O valor de var é menor que 10";
} else do {
  print "O valor de var é maior ou igual a 10";
}
# Ifs encadeados
if var < 5 do {
  print "O valor de var é menor que 5";
} else do {
  if var < 10 do {
    print "O valor de var é menor que 10";
  } else do {
    print "O valor de var é maior que 10";
  }
}
```
#### __Definição de Novas Estruturas de Repetição__
---
- **while**: Permite a repetição de um bloco de código enquanto uma condição for verdadeira;
```
a : Number = 2;
b : Number = 3;

while not (a + b >= 10) do {
    a = a + 1;
    print a;
}
```
- **repeat-until**: Repete um bloco de código até que uma condição se verifique
```
a :Number = 2;
b : Number = 3;
repeat {
    a = a + 1;
    print a;
} until not (a + b >= 10);
```

#### __Definição de Novos Tipos de Objeto__
---
Também foi adicionado o suporte de novos tipos de figura onde todos respeitam as mesmas regras dos objetos anteriores e as mesmas ações.

- **Polyline**: Representa uma linha que conecta uma lista de pontos
```
polyline : Polyline at (10, 20) with {
  points = [(30, 40), (50, 60), (40, 70)];
  fill = "black";
}
```
- **Spline**: Representa uma linha que conecta uma lista de pontos, no entanto, esta conexão tem um aspeto curvo e *smooth*
```
spline : Spline at (10, 20) with {
  points = [(30, 40), (50, 60), (40, 70)];
  fill = "black";
}
```
- **Polygon**: Representa um polígono definido por vários pontos. De forma mais simples, é uma **Polyline** mas que conecta-se sempre de volta no seu ponto de referência
```
polygon : Polygon at (10, 20) with {
  points = [(30, 40), (50, 60), (40, 70)];
  fill = "black";
  outline = "blue";
}
```
- **Blob**: Apresenta a mesma lógica que o **Polygon**, no entanto, com o aspeto da **Spline**
```
blob : Blob at (10, 20) with {
  points = [(30, 40), (50, 60), (40, 70)];
  fill = "black";
  outline = "blue";
}
```
- **Model**: Possibilita a definição de novos "tipos" de objeto complexos, ou seja, constituídos por um conjunto de outros objetos como propriedades. Também possibilita a ação **action** em qualquer propriedade e que executa algum conjunto de operações caso essa propriedade sofra alteração
```
Pacman :: Model {
    face : PieSlice at (0,0) with {
        length = (50,50);
        fill = "pink";
        start = 30;
        extent = 300;
    }

    # the eye, without a reference
    Ellipse at (20,35) with {
        fill = "black";
        length = (5,5);
    }

    open : Boolean = False;
    action on open {
        if open do {
          with face do {
            start = 30;
            extent = 300;
          }
        } else do {
          with face do {
            start = 1;
            extent = 359;
          }
        }
    }
}
pacman1 : Pacman;  #pacman1 é do tipo Pacman
```


### Nível adicional

> Neste nível, o nosso grupo focou-se na implementação dos requisitos adicionais, tendo em conta a rotação de objetos gráficos e a suporte para várias vistas.

#### __Adicionada a Suporte para várias vistas__
---
Também foi adicionada a possibilidade de se usarem várias views o que fez com que o método **wait mouse click** se aplique agora a todas as **Views**;
```
view1: View with {
    width = 500;
    height = 500;
    title = "View 1";
    background = "wheat";
}

view2: View with {
    Ox = 500;
    width = 500;
    height = 500;
    title = "View 2";
    background = "wheat";
}

view3: View with {
    Ox = 1000;
    width = 500;
    height = 500;
    title = "View 3";
    background = "wheat";
}
refresh view1, view2, view3;  #Atualiza todas as views
p : Point = wait mouse click; #Espera por um clique do utilizador em qualquer View
close view1, view2, view3;    #Fecha todas as views

```

#### __Adicionada a Rotação de objetos__
---
Neste nível foi adicionado a possibilidade de dar **rotate** a qualquer objeto.
Para este efeito teve de se remodular a maneira como alguns objetos eram criados de modo a possibilitar esta rotação, nomeadamente, a **Ellipse** e os seus derivados **Arc**, **ArcChord**, **PieSlice** que, em vez de serem criados com os métodos usuais, **create_oval** e **create_arc** do tkinter, são agora criados através do cálculo dos pontos a partir das condições iniciais e aplicando esses pontos de maneira semelhante á **Polyline**.

A rotação também se aplica a **Model** o que vai rodar todos os seus objetos pelas mesmas regras de rotação.
Segue um exemplo com o auxilio do **deepcopy** para criar uma cópia exata de um objeto, que irá ser explicado mais á frente:
```
Ex1 :: Model {

    cellSize : Number = 200;

    rec: Rectangle at (0,cellSize) with {
        length = (50,50);
        fill = "orange";
    }

    ell: Ellipse at (cellSize,cellSize) with {
        length = (60,40);
        fill = "blue";
    }
}

ex1 : Ex1;
ellExtra : Ellipse = deepcopy ex1.ell to ex1.rec.origin; # exact copy
ellExtra.fill = "red";

refresh view;
p : Point = wait mouse click;
for i in 1..360 do {
    rotate ex1 by 1;
    move ellExtra to ex1.rec.origin;
    rotate ellExtra by -5;
    refresh view after 0.01 s;
}
refresh view;
```
![Rotate.gif](doc/examples/demo/Rotate.gif)

### Nível extra

> Neste nível, o nosso grupo focou-se na implementação dos requisitos extra, tendo em conta a criação de uma animação interativa que permita a um utilizador resolver as torres de Hanoi, a falicitação na criação de modelos predefinidos atribuindo valores default a propriedades e a facilitação na duplicação de objetos gráficos complicados com a funcionalidade *deepcopy*.

#### __Acrescentada a Funcionalidade DeepCopy__
---
Como funcionalidade extra, decidiu-se dar a possibilidade ao utilizador de fazer uma cópia exata de um objeto de modo a facilitar a contrução de elementos com as mesmas propriedades sem que resultasse na repetição de código, o que oferece ao programador a facilidade em criar estruturas complexas sem tornar o seu código extenso/complexo demais. No caso de um **Model**, o **deepcopy** vai copiar todos os objetos que o compõem e as suas propriedades.


Para facilitar ainda mais esta operação, quando se faz um **deepcopy** de algum objeto, consegue-se colocar diretamente esse objeto em qualquer lugar do canvas através da instrução **to**
```
object: Rectangle at (10,10) with {
    length = (50,50);
    fill = "orange";
}

object2 : Rectangle = deepcopy object to (20,20);
object3 : Rectangle = deepcopy object to (30,30);
object4 : Rectangle = deepcopy object to (40,40);
object5 : Rectangle = deepcopy object to (50,50);
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

<<<<<<< HEAD
=======
## Estrutura do repositório
O repositório está organizado da seguinte forma:
- `doc/` contém a documentação do projeto.
- `doc/examples/` contém exemplos de código AGL e xAGL.
- `src/` contém o código fonte do projeto.
- `src/tests/` contém os testes do projeto (nomeadamente analise semântica).

## Dependências

Para correr o projeto é necessário ter instalado:
 - `antlr4` (com gramática AGL)
 - `python3`
 - `tkinter`
 - `numpy`


Instalar as dependências do projeto:
```bash
pip install -r requirements.txt
```

## Relatório

- Use esta secção para fazer um relatório sucinto mas explicativo dos objetivos concretizados.

>>>>>>> fe68eb8 (start readme)
## Contribuições

Para este trabalho, o nosso grupo dividiu-o nos seguintes tópicos e distribui os mesmos pelos elementos do grupo da seguinte forma:

<span style="color:red">[POR COMPLETAR!!!]</span>

  - Construção da gramática AGL:
    - Pedro Pinto - 115304
    - João Pinto - 104384
    - João Monteiro - 114547
  - Compilador (AGL):
    - Pedro Pinto - 115304
    - Guilherme Santos - 113893
    - Giovanni Santos - 115637
  - Análise semântica (AGL):
    - João Pinto - 104384
    - João Monteiro - 114547
    - Jorge Domingues - 113278
  - Interpretador (xAGL):
    - Giovanni Santos - 115637  
  - Análise semântica (xAGL):
    - ...
  - Testes:
    - Pedro Pinto - 115304
    - João Pinto - 104384
    - João Monteiro - 114547
    - Guilherme Santos - 113893
  - Documentação:
    - Pedro Pinto - 115304
    - Guilherme Santos - 113893
    - ...
  
cat ../doc/ex00.agl | antlr4-run > ../doc/t1.py
```

## Run Semantic Check 
Inside the `src` directory:
```
antlr4-main AGLParser.g4 program -v AGLSemanticCheck.java
antlr4-build
cat tests/ValidTests/ex05.agl | antlr4-run
```

## Test Semantic Check
Inside the `src` directory:
```
./tests/run-tests.sh
```
