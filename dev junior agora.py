import os

mensagens = []

nome = input("Nome: ")

while True:


    os.system('cls') #comando para limpar o terminal

    if len(mensagens) > 0:
        for m in mensagens:
            print(m['nome'], "-", m['texto'])

    print("_______________")

    #obter o texto
    texto = input("mensagem: ")
    if texto == "fim":
        break

    #adicionando mensagem na lista
    mensagens.append({
        "nome":nome,
        "texto":texto
    })