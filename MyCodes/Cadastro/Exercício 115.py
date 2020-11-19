from MyCodes.personal import *

lista = []
while True:
    menu(['Ver pessoas cadastradas', 'Cadastrar mais uma pessoa', 'Sair'], 'MENU PRINCIPAL')
    op = inputInt('\033[32mSua opção:\033[m ')
    if op == 1:
        title('PESSOAS CADASTRADAS', 50)
        readArch('cadastrados.txt')
    elif op == 2:
        title('NOVO CADASTRO', 50)
        nome = inputName('Nome: ')
        idade = inputInt('Idade: ')
        lista.append(nome)
        lista.append(str(idade))
        try:
            f1 = open('cadastrados.txt', 'x')
            for items in lista:
                if items == lista[0]:
                    f1.write(f'{items:.<40}')
                else:
                    f1.write(f'{items:>2} anos')
            lista.clear()
            f1.close()
        except FileExistsError:
            f2 = open('cadastrados.txt', 'a')
            for items in lista:
                if items == lista[0]:
                    f2.write(f'\n{items:.<40}')
                else:
                    f2.write(f'{items:>2} anos')
            lista.clear()
            f2.close()
        print(f'Novo registro de {nome} adicionado.')
    elif op == 3:
        title('Saindo do sistema... Até logo!', 50)
        break
    else:
        print('\033[31m[ERRO]\033[m')
