import os

restaurantes = ['Pizza', 'Sushi', 'Churrascaria', 'Lanchonete']
    

def exibir_nome_programa():
    print('𝕊𝔸𝔹𝕆ℝ 𝔼𝕏ℙℝ𝔼𝕊𝕊\n')

def opcoes():
    print('1. Cadastrar Restaurante')
    print('2. Listar Restaurante')
    print('3. Ativar Restaurante')
    print('4. Sair\n')

def finalizar_app():
        exibir_subtitulo('Finalizando o App')
        print('Obrigado por usar o Sabor Express!\n')
def voltar_ao_menu_principal():
    input('Digite uma tecla para voltar ao menu principal: ')
    main()
def opcao_invalida():
    print('Opção inválida!\n')
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    os.system('cls')
    print(texto)
    print()

def cadastrar_novo_restaurante():
    exibir_subtitulo('Cadastrar Novo Restaurante')
    nome_restaurante = input('Digite o nome do restaurante: ')
    restaurantes.append(nome_restaurante)
    print(f'O Restaurante {nome_restaurante} foi cadastrado com sucesso!\n')
    voltar_ao_menu_principal()

def listar_restaurantes():
    exibir_subtitulo('Listar Restaurantes')
    for restaurante in restaurantes:
        print(f'- {restaurante}')
    voltar_ao_menu_principal()

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
           listar_restaurantes()
        elif opcao_escolhida == 3:
            print('Ativar Restaurante')
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()
        

def main():
    os.system('cls')
    exibir_nome_programa()
    opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()