idade = int(input("Digite sua idade: "))
habilitacao = input("Você tem habilitação?: ")
if idade >= 18 and habilitacao == "sim":
    print("Pode dirigir")
else:
    print("Não pode dirigir")
