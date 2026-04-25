import math


def eh_primo(n):
    """Retorna True se n for um número primo, caso contrário False."""
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
