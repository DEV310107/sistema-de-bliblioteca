# main.py

import os
from funcoes import main, cadastrar_cliente, login, cliente_opcoes, bibliotecario_opcoes

sair = False

while not sair:
    escolha = main()

    os.system("cls" if os.name == "nt" else "clear")

    if escolha == 1:
        cadastrar_cliente()

    elif escolha == 2:
        usuario, tipo = login()
        
        if usuario and tipo == "cliente":
            while True:
                cliente_opcoes(usuario)
                print("Deseja voltar ao menu principal?")
                print("1 - Sim")
                print("2 - Não")
                var = int(input("---> "))
                if var == 1:
                    break
                elif var == 2:
                    print("Continuando no menu de opções do cliente...")
                else:
                    print("Opção inválida. Por favor, escolha 1 ou 2.")
        
        elif usuario and tipo == "bibliotecario":
            bibliotecario_opcoes(usuario)

    elif escolha == 0:
        sair = True

    else:
        print("Opção inválida.")
        os.system("pause")
        os.system("cls" if os.name == "nt" else "clear")
