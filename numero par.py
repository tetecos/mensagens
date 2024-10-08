nome = input("digite seu nome: ")
termo = int(input(f"\nola senhor {nome} como voce gostaria de ser chamado? \n(1)masculo \n(2)rei \n(3)soberano \n(4)pica \n"))

if termo == 1:
    print(f"ola {nome} o masculo")
elif termo == 2:
    print(f"ola {nome} o rei")
elif termo == 3:
    print(f"ola {nome} o soberano")
elif termo == 4:
    print(f"ola {nome} o pica")
else:
    print("opcao invalida")


      