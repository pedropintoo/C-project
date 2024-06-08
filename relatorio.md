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

Por exemplo, no ficheiro presente em src/tests/InvalidTests/VariableDeclaration_1.agl temos um exemplo onde foi definida uma variável como Number e posteriormente foi tentado atribuir-lhe um valor do tipo String. O analisador semântico deteta este erro.

2. **Atribuições e Operações**:
   - Verificação da validade das atribuições e operações entre variáveis.
   - Garantia de que os tipos de dados são compatíveis nas operações.

3. **Propriedades dos Modelos Gráficos**:
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