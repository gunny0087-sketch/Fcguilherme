soma = 0
numeropositivo = 0
while True:
    numero = int(input("Digite um número: "))
    if numero < 0:
        break
    soma += numero
    if numeropositivo == 0:
        maior = numero
    else:
        if numero > maior:
            maior = numero
    numeropositivo += 1
if numeropositivo > 0:
    media = soma / numeropositivo
    print(f"A soma de todos os números é {soma}")
    print(f"A média aritmética dos números é {media}")
    print(f"O maior número é {maior}")
else:
    print("Nenhum número positivo foi digitado.")
