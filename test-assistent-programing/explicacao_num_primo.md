# Explicação do código `num_primo.py`

## Importação

```python
import math
```
- Importa o módulo `math` para usar `math.isqrt`, que calcula a raiz quadrada inteira de `n` de forma eficiente.

## Função `eh_primo(n)`

```python
def eh_primo(n):
```
- Declara a função `eh_primo` que recebe um número `n`.

```python
    """Retorna True se n for um número primo, caso contrário False."""
```
- Comentário de documentação (docstring) explicando o que a função faz.

```python
    if n < 2:
        return False
```
- Números menores que 2 não são primos, então retorna `False`.

```python
    if n <= 3:
        return True
```
- 2 e 3 são primos, então se `n` for 2 ou 3 retorna `True`.

```python
    if n % 2 == 0 or n % 3 == 0:
        return False
```
- Se `n` for divisível por 2 ou por 3, não é primo; retorna `False`.

```python
    limite = math.isqrt(n)
```
- Calcula a raiz quadrada inteira de `n` uma única vez para usar como limite do loop.

```python
    i = 5
```
- Inicia `i` em 5 para testar fatores potenciais maiores que 3.

```python
    while i <= limite:
```
- Continua enquanto `i` for menor ou igual ao limite. Isso permite testar apenas os divisores úteis.

```python
        if n % i == 0 or n % (i + 2) == 0:
            return False
```
- Verifica se `n` é divisível por `i` ou por `i + 2`. Isso testa pares de candidatos como 5 e 7, depois 11 e 13, etc.

```python
        i += 6
```
- Avança `i` em 6 porque todos os números primos maiores que 3 estão na forma `6k ± 1`.

```python
    return True
```
- Se nenhum divisor foi encontrado, `n` é primo; retorna `True`.

## Bloco principal

```python
if __name__ == "__main__":
```
- Verifica se o arquivo está sendo executado como programa principal, e não importado como módulo.

```python
    teste = 29
```
- Define a variável `teste` com o valor `29`.

```python
    print(f"{teste} é primo? {eh_primo(teste)}")
```
- Chama a função `eh_primo` para `29` e imprime o resultado.
