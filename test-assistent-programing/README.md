# Test Assistant Programming

Este projeto é uma coleção de exemplos e exercícios práticos em Python, desenvolvidos para auxiliar no aprendizado de conceitos fundamentais de programação, incluindo algoritmos, refatoração de código, depuração e boas práticas de desenvolvimento.

## Estrutura do Projeto

```
test-assistent-programing/
├── debug.py                           # Sistema de cálculo de compras com depuração
├── explicacao-debug.md                # Explicação detalhada dos erros e correções em debug.py
├── num_primo.py                       # Função para verificar se um número é primo
├── explicacao_num_primo.md            # Explicação linha por linha do algoritmo de verificação de primos
├── refatoracao.py                     # Função para calcular estatísticas de uma lista
└── explicacao_refatoracao.md          # Documentação da refatoração de código ruim para bom
```

## Exemplos Incluídos

### 1. Verificação de Números Primos (`num_primo.py`)

Implementa um algoritmo otimizado para verificar se um número é primo, utilizando testes de divisibilidade eficientes.

**Como executar:**
```bash
python num_primo.py
```

**Saída esperada:**
```
29 é primo? True
```

**Características:**
- Algoritmo O(√n) otimizado
- Testa apenas divisores necessários (forma 6k ± 1)
- Inclui docstring completa no padrão Google

### 2. Sistema de Cálculo de Compras (`debug.py`)

Programa interativo que calcula o total de uma compra com três itens, aplicando imposto de 10% e desconto opcional via cupom.

**Como executar:**
```bash
python debug.py
```

**Exemplo de uso:**
- Nome do cliente: João
- Item 1: Quantidade 2, Preço 10.00
- Item 2: Quantidade 1, Preço 25.50
- Item 3: Quantidade 3, Preço 5.00
- Cupom de desconto: 5

**Características:**
- Entrada interativa de dados
- Cálculo de subtotal, imposto e desconto
- Exibição formatada de recibo
- Comentários inline explicando lógica de decisões

### 3. Cálculo de Estatísticas (`refatoracao.py`)

Demonstração de refatoração: calcula total, média, maior e menor valor de uma lista de números.

**Como executar:**
```bash
python refatoracao.py
```

**Saída esperada:**
```
Total: 346
Média: 34.6
Maior: 89
Menor: 2
```

**Características:**
- Uso de funções built-in do Python (sum, max, min)
- Código limpo e legível após refatoração
- Exemplo prático de melhoria de código

## Pré-requisitos

- Python 3.6 ou superior
- Nenhum módulo externo necessário (apenas biblioteca padrão)

## Como Usar

1. Clone ou baixe este repositório
2. Navegue até a pasta `test-assistent-programing`
3. Execute qualquer arquivo Python diretamente:
   ```bash
   python nome_do_arquivo.py
   ```

## Documentação Adicional

Cada exemplo inclui um arquivo de explicação detalhada:

- `explicacao_num_primo.md`: Análise linha por linha do algoritmo de primos
- `explicacao_refatoracao.md`: Processo de refatoração e melhores práticas
- `explicacao-debug.md`: Identificação e correção de erros comuns

## Objetivos de Aprendizado

Este projeto visa demonstrar:

- Implementação de algoritmos matemáticos eficientes
- Importância da refatoração para código sustentável
- Técnicas de depuração e correção de erros
- Boas práticas de documentação (docstrings, comentários)
- Uso adequado de funções built-in do Python
- Formatação e apresentação de dados

## Contribuição

Sinta-se à vontade para:

- Adicionar novos exemplos
- Melhorar algoritmos existentes
- Corrigir bugs ou melhorar documentação
- Sugerir exercícios adicionais

## Licença

Este projeto é para fins educacionais e pode ser usado livremente para aprendizado.