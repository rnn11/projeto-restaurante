import os
import time
def gravar_cadastro(cadastro, endereco):
    with open('restaurantes.txt', 'a') as arquivo:
        arquivo.write(f"{cadastro};{endereco}\n")
def listar_restaurantes():
    with open('restaurantes.txt', 'r') as arquivo:
        restaurantes = arquivo.readlines()
    for restaurante in restaurantes:
        cadastro, endereco = restaurante.strip().split(';')
        print(f"- {cadastro}: {endereco}")
while True:
    print("Restaurantes Pirituba")
    print('\n1. Cadastrar Restaurante')
    print('2. Listar Restaurante')
    print('3. Ativar Restaurante')
    print('4. Sair')
    opcao = input("\nEscolha uma opção: ")
    if opcao == '1':
        os.system('cls')
        print("\nSeja bem-vindo à tela de cadastro de restaurantes de Pirituba")
        cadastro = input("Escolha o nome do seu restaurante: ")
        endereco = input("Qual o endereço do seu comércio?: ")
        print("\nRestaurante cadastrado com sucesso")
        print(f"\nO nome do seu restaurante é {cadastro}")
        print(f"E está localizado no endereço {endereco}")
        print("\nRESTAURANTE CADASTRADO!\n\nVocê será redirecionado ao menu3 do site.\n")
        gravar_cadastro(cadastro, endereco)
        continue
    elif opcao == '2':
        os.system('cls')
        print("\nOlá! Nós vamos listar os restaurantes registrados em Pirituba\nno dia de hoje:\n")
        listar_restaurantes()
        voltar = input("\n Aperte 'ENTER' para voltar à página inicial!\n")
        if voltar == '':
            os.system('cls')
            continue
    elif opcao == '3':
        os.system('cls')
        ativar = input("Qual o nome do restaurante que você deseja ativar?: ")
        with open('restaurantes.txt', 'r') as arquivo:
            restaurantes = arquivo.readlines()
            restaurantes2 = ['restaurantes.txt']
        if any(ativar in restaurante for restaurante in restaurantes):
            os.system('cls')
            print("\nNós achamos o seu restaurante em nosso sistema!\n O seu restaurante foi ativado\n")
            print(f"Muito obrigado, dono da '{ativar}'\n")
            print('Você será redirecionado ao menu do site')
            time.sleep(3)
            os.system('cls')
        else:
            os.system('')
            print("Desculpe, não encontramos o restaurante desejado.")
        continue
    elif opcao == '4':
        os.system('cls')
        print("Muito obrigado pela sua visita!\n\nAté a próxima\n")
        break
    else:
        os.system('cls')
        print('\n"Escolha apenas as opções dadas!\n')