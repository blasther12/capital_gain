## Ganho de Capital
Este projeto contém um programa de linha de comando (CLI) que calcula o imposto a
ser pago sobre lucros ou prejuízos de operações no mercado financeiro de ações.

### Principais Decisões Arquiteturais
#### Modularização
Cada cálculo (custo, lucro, imposto) foi encapsulado em funções independentes, promovendo a reutilização do código e facilitando a manutenção e extensibilidade.

#### Cálculo do Preço Médio
O cálculo contínuo do preço médio é feito com base nas compras, garantindo que o custo das vendas seja calculado corretamente a cada operação.

#### Impostos
A tributação é aplicada de forma condicional. Perdas acumuladas são compensadas com lucros futuros, seguindo regras fiscais comuns para ganhos de capital, com um imposto de 20% sobre o lucro ajustado.

#### Estruturas de Dados
O uso de modelos Operation e OperationTax organiza os dados relacionados às operações e aos impostos, facilitando a manipulação dos dados e a extensão do código conforme novas operações ou regras fiscais são adicionadas.

### Dependências
Este projeto utiliza o Poetry para gerenciamento de dependências e ambientes virtuais. Para instalar e configurar o ambiente, siga as instruções abaixo:

**Instalação**

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

**Ativar o ambiente virtual:** Para ativar o ambiente virtual gerenciado pelo Poetry, use o comando:

```bash
poetry shell
```
**Instalar as dependências do projeto:** No diretório do projeto, execute o comando:

```bash
poetry install
```

### 🚀 Executando o projeto

```bash
make run
```

### Executando casos do documento de instrução

```bash
make run-cases
```

### ⚙️ Executando os testes

```bash
make test
```