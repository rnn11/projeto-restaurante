import os
restaurantes = [
    {'Nome': 'Cantina toscana', "Categoria": "Italiana", "Ativo": True},
    {'Nome': "Suchi da Praça", "Categoria": "Japonesa", "Ativo": False},
    {"Nome": "Churrascaria Gaúcha", "Categoria": "Brasileira", "Ativo": True},
    {"Nome": "Padaria Michele", "Categoria": "Padaria", "Ativo": True}
]

def exibir_nome_do_programa():
    print("""
    █▀▀ ▄▀█ █▀ ▄▀█ █▀ ▀█▀ █▀█ █▀█ █▀   █▀▄ █▀▀   █▀█ █▀▀ █▀ ▀█▀ ▄▀█ █░█ █▀█ ▄▀█ █▄░█ ▀█▀ █▀▀ █▀   █▀█ █▄░█ █░░ █ █▄░█ █▀▀
    █▄▄ █▀█ █▄▀ █▀█ ▄█ ░█░ █▀▄ █▄█ ▄█   █▄▀ ██▄   █▀▄ ██▄ ▄█ ░█░ █▀█ █▄█ █▀▄ █▀█ █░▀█ ░█░ ██▄ ▄█   █▄█ █░▀█ █▄▄ █ █░▀█ ██▄""")
    print("")

def menu():
    print('\n1. Cadastrar Restaurante')
    print('2. Listar Restaurantes')
    print('3. Ativar Restaurante')
    print('4. Sair')

def finalizar_app():
    os.system('cls')
    print("\nFinalizando...")

def opcao_invalida():
    print("\nDesculpe! Não temos essa opção em nosso sistema.\n")
    input("Digite ENTER para voltar ao menu principal")
    main()

def cadastrar_restaurante():
    print("Cadastre-se: ")
    nome_proprietario = input("Quem é o proprietário?: ")
    nome_restaurante = input("Qual o nome do seu restaurante?: ")
    categoria_restaurante = input("Qual a categoria do seu restaurante?: ")
    endereco_restaurante = input("Qual o endereço do seu restaurante?: ")
    restaurante_ativo = input("Seu restaurante está ativo? (Ativo/Inativo): ").lower() in ['Ativo']
    restaurantes.append({'Nome': nome_restaurante, 'Categoria': categoria_restaurante, 'Ativo': restaurante_ativo})
    print(f"O '{nome_restaurante}' de {nome_proprietario} foi cadastrado com sucesso!")
    print(f'Endereço: {endereco_restaurante}')
    print(f"Ativo" if restaurante_ativo else "Inativo")
    input('Aperte ENTER para voltar para o inicio')
    main()

def lista_restaurantes():
    print("Listando os restaurantes:")
    for restaurante in restaurantes:
        nome_restaurante = restaurante['Nome']
        categoria_restaurante = restaurante['Categoria']
        restaurante_ativo = "Ativo" if restaurante['Ativo'] else "Inativo"
        print(f'- {categoria_restaurante}: {nome_restaurante}: {restaurante_ativo}')
    input('Aperte ENTER para voltar para o inicio')
    main()
def escolher_opção():
    try:
        opcao = int(input("\nEscolha uma opção: "))
        if opcao == 1:
            cadastrar_restaurante()
        elif opcao == 2:
            lista_restaurantes()
        elif opcao == 3:
            print("Ativar restaurante")
        elif opcao == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    exibir_nome_do_programa()
    while True:
        menu()
        escolher_opção()

if __name__ == '__main__':
    main()