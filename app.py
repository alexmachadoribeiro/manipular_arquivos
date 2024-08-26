import os

def exibir_menu():
    print('1 - Ler arquivo.')
    print('2 - Gravar novos dados no arquivo.')
    print('3 - Sair do programa.')

def gravar_arquivo(dados, novo_nome, nova_idade, nova_profissao):
    dados += f'\n\n{'-'*30}\n\nNome: {novo_nome}.\nIdade: {nova_idade}.\nProfissão: {nova_profissao}.'
    with open('dados.txt', 'w', encoding='utf-8') as arquivo:
        arquivo.write(dados)

def ler_arquivo():
    with open("dados.txt", 'r', encoding="utf-8") as arquivo:
        dados = arquivo.read()
    return dados

if __name__ == "__main__":
    while True:
        exibir_menu()
        opcao = input('Opção desejada: ')
        os.system('cls')
        match opcao:
            case '1':
                dados = ler_arquivo()
                print(f'\n{dados}\n')
                continue
            case '2':
                print('NOVO CADASTRO:\n')
                novo_nome = input("Insira o nome do novo usuário: ")
                nova_idade = input("Insira a idade do novo usuário: ")
                nova_profissao = input("Insira a profissão do novo usuário: ")
                gravar_arquivo(dados, novo_nome, nova_idade, nova_profissao)
                continue
            case '3':
                print('Programa finalizado.')
                break
            case _:
                print('Opção inválida')
                continue