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

4. **Propriedades dos Modelos Gráficos**:
   - Verificação da validade das propriedades dos diferentes modelos gráficos.
   - As propriedades devem ser definidas corretamente e estar de acordo com os modelos gráficos correspondentes.

4. **Instanciação de Vistas**:
   - Verificação das ações suportadas pelas vistas, como `move`, `refresh`, `wait` e `close`.

## Como Executar

Para executar o analisador semântico e verificar os testes, siga os passos abaixo:

1. Navegue até o diretório `src`:
   ```sh
   cd src
   ```

2. Execute o script de testes:
   ```sh
   ./tests/run-tests.sh
   ```

O script irá executar todos os testes presentes nos diretórios `ValidTests` e `InvalidTests`, verificando se o comportamento esperado é obtido.

## Exemplos de Teste

### Testes Válidos

Exemplo de um ficheiro .agl válido (`ValidTests/example1.agl`):
```agl
// Comentário de linha
view v1 {
    move(10, 20);
}
dot d1 {
    move(15, 25);
}
```

### Testes Inválidos

Exemplo de um ficheiro .agl inválido (`InvalidTests/example1.agl`):
```agl
dot d1 {
    move(10, 20);
}
move(15, 25); // Erro: move sem instância
```

## Notas

- Certifique-se de que tem o ANTLR4 instalado e configurado corretamente no seu sistema.
- Os testes são projetados para garantir que o analisador semântico detecte corretamente os erros e valide os programas AGL.

## Conclusão

Este projeto implementa um analisador semântico robusto para a linguagem AGL, proporcionando uma camada adicional de verificação que garante a corretude dos programas antes da sua execução.

---

Sente-se à vontade para adicionar ou modificar qualquer seção conforme necessário. Se desejares incluir exemplos específicos ou o código do analisador semântico, podes fornecê-los que eu posso integrar ao README.