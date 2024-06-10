# AGLSemanticCheck

## Descrição

Implementação de um analisador semântico para a linguagem de programação AGL (Animated Graphics Language). O analisador semântico é responsável por verificar a correção semântica dos programas escritos em AGL, garantindo que não existam erros que passem despercebidos pela análise sintática.

## Estrutura do Projeto

- `src/`: Diretório contendo o código fonte.
  - `AGLSemanticCheck.java`: Implementação do analisador semântico.
  - `tests/`: Diretório contendo os testes.
    - `ValidTests/`: Contém exemplos de programas AGL válidos.
    - `InvalidTests/`: Contém exemplos de programas AGL com erros semânticos.
    - `run-tests.sh`: Script shell para executar todos os testes.

## Verificações Semânticas Realizadas

O analisador semântico verifica os seguintes aspectos:

1. **Declaração de Variáveis**:
   - As variáveis devem ser declaradas antes de serem utilizadas.
   - Não pode haver repetições nas declarações de variáveis.

Por exemplo, no ficheiro presente em src/tests/InvalidTests/VariableDeclaration_1.agl, temos um exemplo onde foi definida uma variável como Number e posteriormente foi tentado atribuir-lhe um valor do tipo String. O analisador semântico deteta este erro. Por outro lado, o analisador também deteta se o utilizador tentar definir uma variável que já se encontra declarada, reportando o erro, como no ficheiro InvalidTests/VariableDeclaration_2.agl.

2. **Atribuições e Operações**:
   - Verificação da validade das atribuições e operações entre variáveis.
   - Garantia de que os tipos de dados são compatíveis nas operações.

Por exemplo, o ficheiro `ValidTests/OperationsValid.agl` contém exemplos de operações válidas, como a soma de um ponto com um vetor, a multiplicação de um ponto por um inteiro, e a comparação entre um float e um inteiro com o mesmo valor.

Por outro lado, o ficheiro `InvalidTests/OperationsInvalid.agl` contém exemplos de operações inválidas, como a tentativa de somar um ponto com um inteiro, a soma de dois pontos, ou a divisão de dois vetores. Nestes casos, o analisador semântico deteta e sinaliza os erros, garantindo que apenas operações válidas sejam permitidas no código AGL.

3. **Propriedades dos Arrays**:
    - Consistência de Tipos de Arrays: verificação para garantir que o tipo de array a atribuir coincide com o tipo declarado

Por exemplo, os ficheiros `InvalidTests/TestArray{1,2,3,4}.agl` contêm vários exemplos que ilustram estas verificações. No ficheiro InvalidTests/TestArray1.agl, tentou-se definir a variável "c" como um Array de Strings, mas como esta variável era um Array de um Array de Pontos, o analisador semântico detetou o erro. Outro exemplo, no ficheiro InvalidTests/TestArray2.agl, mostra uma tentativa de atribuir um valor do tipo String a um elemento de um Array de Pontos, que também foi corretamente identificado como erro pelo analisador.

No ficheiro `InvalidTests/TestArray4.agl`, foram realizados diversos testes para verificar a consistência dos tipos de arrays atribuídos. Testou-se a atribuição correta e incorreta de valores a arrays de arrays de pontos, verificando-se que o analisador semântico deteta e sinaliza os erros adequadamente.

No ficheiro `ValidTests/TestArray1.agl`, encontram-se atribuições válidas como, por exemplo: atribuição de um array de inteiros; atribuição de um array de arrays de pontos, etc ...

4. **Propriedades dos objetos**:
   - Verificação de Propriedades Válidas: O analisador semântico verifica se as propriedades atribuídas aos objetos gráficos existem e são válidas.
   - Verificação de Valores Válidos: o analisador garante que os valores atribuídos a estas propriedades sejam válidos e compatíveis com o esperado.

Por exemplo, os ficheiros `InvalidTests/TestAttributes{1,2,3}.agl` contêm exemplos que ilustram estas verificações. 
No ficheiro InvalidTests/TestAttributes1.agl, tentou-se definir uma propriedade fill2 para um retângulo, mas esta propriedade não existe, e o analisador semântico detetou o erro. 
Outro exemplo, no ficheiro InvalidTests/TestAttributes2.agl, mostra uma tentativa de atribuir um valor inválido à propriedade fill, que não é uma cor reconhecida pelo Tkinter, o que também foi identificado como erro pelo analisador. 
Já no ficheiro InvalidTests/TestAttributes3.agl, tentou-se definir a propriedade 'state' para um retângulo como "super", mas esta propriedade não é válida, e o erro foi corretamente detetado pelo analisador.

5. **Operação de refresh/close**:
   - Tipo de ID em Refresh/Close: Todas as IDs usadas nas operações de refresh e close devem ser do tipo View.
   - Expressão de Tempo em Refresh: No caso da operação refresh, a expressão após after deve ser do tipo Integer, Number ou uma variável do tipo Time garantindo que o valor temporal fornecido seja válido.

Por exemplo, os ficheiros `InvalidTests/TestRefresh1.agl` e `InvalidTests/TestClose1.agl` contêm exemplos que ilustram estas verificações. No ficheiro `InvalidTests/TestRefresh1.agl`, a operação refresh é aplicada corretamente a uma variável do tipo View, mas falha ao ser aplicada a uma variável do tipo Integer, sendo este erro corretamente detetado pelo analisador semântico. De maneira similar, no ficheiro `InvalidTests/TestClose1.agl`, a operação close é corretamente aplicada a uma View, mas um erro é detetado quando se tenta aplicar close a uma variável do tipo Integer.
Relativamente à expressão de tempo em Refresh, o ficheiro `ValidTests/TestRefreshTimeExpression.agl` contém um exemplo que ilustra esta verificação. Neste ficheiro, temos duas operações refresh, uma com uma expressão de tempo do tipo Integer e outra com uma expressão de tempo do tipo Time, ambas corretamente verificadas pelo analisador semântico.
Por outro lado, no ficheiro `InvalidTests/TestRefreshTimeExpressionInvalid.agl`, a expressão de tempo após after é do tipo String, o que é inválido, e o erro é corretamente detetado pelo analisador semântico. O analisador também não permite que seja feita a operação refresh com um valor negativo, como é possível verificar no ficheiro `InvalidTests/TestRefreshTimeExpressionInvalid2.agl`.


6. **Operação de move**:
   - Tipos de ID em Move: Os IDs usados na operação de move podem ser objetos, do tipo model ou do tipo view.
   - Uso de "by" e "to": Quando a operação move utiliza by, deve ser seguida por um Point ou um Vector, permitindo movimentos relativos. Quando a operação move utiliza to, deve ser seguida por um elemento do tipo Point, especificando uma posição absoluta para o movimento.

Por exemplo, o ficheiro `InvalidTests/TestMoveInvalid1.agl` contém um exemplo que ilustra esta verificação. Neste ficheiro, a operação move é aplicada a um Point, mas isso é inválido, pois Point não é considerado um objeto. Este erro é corretamente detetado pelo analisador semântico.

Por exemplo, no ficheiro `InvalidTests/TestMoveInvalid2.agl` ....


7. **Verificação de estruturas de repetição**
   - Verificação de expressões condicionais: O analisador semântico assegura que as expressões condicionais utilizadas nas estruturas de repetição (`while`) sejam válidas e do tipo booleano.

Por exemplo, o ficheiro `ValidTests/TestWhile.agl` demonstra exemplos de verificações válidas para as estruturas de repetição. Neste ficheiro, as condições dentro das instruções `while` são corretamente verificadas pelo analisador semântico para garantir que sejam do tipo booleano.

Para além disso, foi criado um exemplo `InvalidTest/TestWhileFail.agl`, que contém exemplos de estruturas `while` com expressões inválidas, como a expressão 'abc', que não é do tipo booleano. Este teste ilustra como o analisador semântico identifica erros relativos a este tipo de estruturas.


8. **Verificação das estruturas de ação**
   - Verificação de elementos: É assegurado que dentro de uma action apenas podem ser englobadas ações com atributos previamente definidos dentro do Model (ver este texto).
   - Verificação de Instantiation: É também assegurado que não pode ser feita uma instanciação dentro de uma action.


9. **Verificação dos atributos dos ObjectType**:
   - Verificação dos atributos: Para cada ObjectType (por exemplo "Blob", "Arc", ...) foi feita uma verificação dos possíveis atributos nessas estruturas.
   - Verificação das atribuições de variáveis: Para cada atribuição feita dentro de um ObjectType (por exemplo "outline", "fill", ...) foi feita uma verificação do tipo de variável possível para essa verificação. Para a atribuição de "points" o tipo de variável terá de ser um array de pontos.

Por exemplo, o ficheiro `InvalidTests/TestAttributes5.agl` demontra que numa View não pode haver a definição de uma "origin".

Por exemplo, o ficheiro `InvalidTests/TestAttributes4.agl` demontra que à variável "height" não pode ser atribuido um ponto (uma vez que tem de ser um inteiro).


10. **Olá**

## Como Executar

Para executar o analisador semântico e verificar os testes, siga os passos abaixo:

Dentro do diretório `src`: 

1. Execute o script de testes:
   ```sh
   ./tests/run-tests.sh
   ```

O script irá executar todos os testes presentes nos diretórios `ValidTests` e `InvalidTests`, verificando se o comportamento esperado é obtido.

