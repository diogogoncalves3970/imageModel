# Explicação do Debug do Código

Este documento detalha os erros encontrados no arquivo `debug.py`, suas causas e as correções aplicadas.

## Erros Identificados e Correções

### 1. Erro de Sintaxe na Entrada do Item 1
**Linha 6:** `item1 = float(input(Preço do item 1? ))`

**Causa:** Falta de aspas ao redor da string passada para `input()`. Em Python, argumentos de função devem ser strings válidas, e sem aspas, o interpretador trata "Preço" como uma variável indefinida, causando um `NameError`.

**Correção:** Adicionar aspas duplas: `item1 = float(input("Preço do item 1? "))`

### 2. Tipo Incorreto para desconto_cupom
**Linha 18:** `desconto_cupom = (input("Você tem um cupom de desconto? (Digite o percentual ou 0): "))`

**Causa:** `input()` retorna uma string, mas o código tenta usar `desconto_cupom` em operações matemáticas (divisão e comparação). Isso resulta em `TypeError` ao tentar dividir uma string por um número ou comparar string com int.

**Correção:** Converter para `float`: `desconto_cupom = float(input("Você tem um cupom de desconto? (Digite o percentual ou 0): "))`

### 3. F-String Incompleta no Print do Item 2
**Linha 27:** `print(" Item 2:        R$ {total_item2:.2f}")`

**Causa:** Falta o prefixo `f` para indicar uma f-string. Sem ele, `{total_item2:.2f}` é tratado como texto literal, não interpolado, resultando em saída incorreta.

**Correção:** Adicionar `f`: `print(f" Item 2:        R$ {total_item2:.2f}")`

### 4. Erro de Indentação no Bloco if
**Linha 34:** `print(f" Desconto ({desconto_cupom:.0f}%): -R$ {desconto:.2f}")`

**Causa:** O código dentro do bloco `if` não está indentado. Em Python, blocos de código (como dentro de `if`) devem ser indentados consistentemente (geralmente 4 espaços), caso contrário, ocorre `IndentationError`.

**Correção:** Indentar a linha: adicionar 4 espaços antes do `print`.

### 5. Comparação Inválida no if (Relacionado ao Tipo de desconto_cupom)
**Linha 33:** `if desconto_cupom > 0:`

**Causa:** Após a correção do tipo, isso funcionará, mas originalmente, ao comparar string com int, Python 3 lança `TypeError`. Mesmo após conversão, garantir que seja numérica evita problemas.

**Correção:** Já resolvido com a conversão para `float` acima.

## Código Corrigido

```python
#                                      CÓDIGO CORRIGIDO
# ENTRADA DE DADOS
cliente = input("Qual é seu nome? ")

qtd1 = int(input("Quantidade do item 1: "))
item1 = float(input("Preço do item 1? "))

qtd2 = int(input("Quantidade do item 2: "))
item2 = float(input("Preço do item 2? "))

qtd3 = int(input("Quantidade do item 3: "))
item3 = float(input("Preço do item 3? "))

# CÁLCULOS DOS ITENS
total_item1 = qtd1 * item1
total_item2 = qtd2 * item2
total_item3 = qtd3 * item3

subtotal = total_item1 + total_item2 + total_item3
imposto = subtotal * 0.10

# DESCONTO
desconto_cupom = float(input("Você tem um cupom de desconto? (Digite o percentual ou 0): "))
desconto = subtotal * (desconto_cupom / 100)

# TOTAL FINAL
total = subtotal + imposto - desconto

# EXIBIÇÃO
linha = "=" * 31
separador = "-" * 31

print(linha)
print(f" Cliente: {cliente}")
print(linha)
print(f" Item 1:        R$ {total_item1:.2f}")
print(f" Item 2:        R$ {total_item2:.2f}")
print(f" Item 3:        R$ {total_item3:.2f}")
print(separador)
print(f" Subtotal:      R$ {subtotal:.2f}")
print(f" Imposto (10%): R$ {imposto:.2f}")

if desconto_cupom > 0:
    print(f" Desconto ({desconto_cupom:.0f}%): -R$ {desconto:.2f}")

print(linha)
print(f" TOTAL:         R$ {total:.2f}")
print(linha)
```

## Validação
Após as correções, o código executa sem erros. Teste com entradas como:
- Nome: João
- Quantidades: 2, 1, 3
- Preços: 10.50, 5.00, 7.25
- Cupom: 10

Saída esperada inclui cálculos corretos e desconto aplicado se cupom > 0.