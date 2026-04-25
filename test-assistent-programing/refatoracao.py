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