import os

def exibir_nome_programa():
    print('𝕊𝔸𝔹𝕆ℝ 𝔼𝕏ℙℝ𝔼𝕊𝕊\n')

def opcoes():
    print('1. Cadastrar Restaurante')
    print('2. Listar Restaurante')
    print('3. Ativar Restaurante')
    print('4. Sair\n')

def finalizar_app():
        os.system('cls')
        print('Finalizando app!\n')

def opcao_invalida():
    print('Opção inválida!\n')
    input('Digite uma tecla para voltar ao menu principal:')
    main()

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        if opcao_escolhida == 1:
            print('Cadastrar Restaurante')
        elif opcao_escolhida == 2:
            print('Listar Restaurante')
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