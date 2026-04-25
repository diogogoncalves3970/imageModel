# Explicação da Refatoração

Este documento explica as mudanças aplicadas no arquivo `refatoracao.py` para melhorar a legibilidade, manutenibilidade e aderência às boas práticas de programação em Python.

## Código Original

```python
def c(l):
    t=0
    for i in range(len(l)):
        t=t+l[i]
    m=t/len(l)
    mx=l[0]
    mn=l[0]
    for i in range(len(l)):
        if l[i]>mx:
            mx=l[i]
        if l[i]<mn:
            mn=l[i]
    return t,m,mx,mn

x=[23,7,45,2,67,12,89,34,56,11]
a,b,c2,d=c(x)
print("total:",a)
print("media:",b)
print("maior:",c2)
print("menor:",d)
```

## Código Refatorado

```python
def calcular_estatisticas_lista(numeros):
    total = sum(numeros)
    media = total / len(numeros)
    maior = max(numeros)
    menor = min(numeros)
    return total, media, maior, menor

numeros = [23, 7, 45, 2, 67, 12, 89, 34, 56, 11]
total, media, maior, menor = calcular_estatisticas_lista(numeros)
print("Total:", total)
print("Média:", media)
print("Maior:", maior)
print("Menor:", menor)
```

## Mudanças Principais

### 1. Nomenclatura Descritiva
- **Função**: Renomeada de `c` (não descritivo) para `calcular_estatisticas_lista`, que claramente indica o propósito da função.
- **Variáveis**: 
  - `l` → `numeros` (lista de entrada)
  - `t` → `total`
  - `m` → `media`
  - `mx` → `maior`
  - `mn` → `menor`
  - `x` → `numeros`
  - `a, b, c2, d` → `total, media, maior, menor` (evitando confusão com o nome da função original `c`)

### 2. Uso de Funções Built-in
- Substituídos loops manuais por funções nativas do Python:
  - `sum(numeros)` para calcular o total
  - `max(numeros)` para o maior valor
  - `min(numeros)` para o menor valor
- Isso torna o código mais eficiente, conciso e menos propenso a erros.

### 3. Legibilidade e Estilo
- Adicionada indentação consistente e espaços ao redor de operadores (ex.: `t=t+l[i]` → `total = sum(numeros)`).
- Removidos loops redundantes, tornando o código mais "Pythonic".
- As mensagens de impressão foram padronizadas com maiúsculas e sem dois-pontos inconsistentes.

### 4. Manutenibilidade
- O código refatorado é mais fácil de entender, modificar e estender.
- Segue convenções do PEP 8 (guia de estilo do Python), como nomes descritivos e uso de funções built-in.

## Validação
O código refatorado foi executado e produz a mesma saída correta:
- Total: 346
- Média: 34.6
- Maior: 89
- Menor: 2

Essas mudanças garantem que o código seja mais profissional e sustentável para futuras alterações.