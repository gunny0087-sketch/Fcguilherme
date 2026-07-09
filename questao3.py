chances= 0
while chances< 3:
    usuario = input("Usuário: ")
    senha = input("Senha: ")
    if usuario == "aluno" and senha == "12345":
        print("Acesso liberado")
        break
    else:
        chances += 1

        if chances== 3:
            print("Você teve 3 tentativas")
        else:
            print("Tente novamente")
