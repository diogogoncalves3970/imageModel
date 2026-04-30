import math


def eh_primo(n):
    """Verifica se um número é primo.

    Utiliza um algoritmo otimizado que testa divisibilidade por 2, 3 e depois
    por números da forma 6k ± 1 até a raiz quadrada de n.

    Args:
        n: Número inteiro a ser verificado.

    Returns:
        bool: True se n for um número primo, False caso contrário.

    Examples:
        >>> eh_primo(29)
        True
        >>> eh_primo(10)
        False
    """
    if n < 2:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    limite = math.isqrt(n)
    i = 5
    while i <= limite:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6

    return True


if __name__ == "__main__":
    teste = 29
    print(f"{teste} é primo? {eh_primo(teste)}")
