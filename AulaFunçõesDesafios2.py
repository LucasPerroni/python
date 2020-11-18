def titulo(escrita, tamanho, cor=0):
    """
    --> Cria um título no programa.
    :param escrita: Parte escrita do título.
    :param tamanho: Tamanho do título.
    :param cor: Cor do título (30 = Branco; 31 = Vermelho; 32 = Verde;
                               33 = Amarelo; 34 = Azul; 35 = Roxo;
                               36 = Ciano; 37 = Cinza; 0 = Nenhuma)
    :return: Sem retorno.
    """
    print(f'\033[{cor}m-' * tamanho)
    print(f'{escrita:^{tamanho}}')
    print(f'\033[{cor}m-\033[m' * tamanho)


def voto(y):
    from datetime import date
    idade = date.today().year - y
    a = ''
    if idade < 16:
        a = f'Com {idade} anos, não pode votar.'
    elif 16 <= idade < 18 or idade >= 65:
        a = f'Com {idade} anos, voto opcional.'
    elif 18 <= idade < 65:
        a = f'Com {idade} anos, voto obrigatório.'
    return a


def fatorial(n, show=False):
    """
    --> Mostra o fatorial de um número.
    :param n: O fatorial a ser calculado.
    :param show: Mostrar ou não o cálculo.
    :return: O valor do fatorial.
    """
    f = 1
    if show:
        print(f'{n}! = ', end='')
    while n >= 1:
        if show and n != 1:
            print(n, end=' x ')
        if show and n == 1:
            print(n, end=' = ')
        f *= n
        n -= 1
    return f


def ficha(n='<desconhecido>', g='0'):
    if n.strip() == '':
        n = '<desconhecido>'
    if g.isnumeric():
        g = int(g)
    else:
        g = 0
    print(f'O jogador {n} fez {g} gols.')


def inputInt(n='Digite um número inteiro: '):
    """
    Função para ler um número inteiro.
    :param n: Parte escrita.
    :return: O número inteiro.
    """
    a = input(n)
    while not a.isnumeric():
        a = input('\033[31m[ERRO]\033[m Digite um número inteiro: ')
    a = int(a)
    return a


def notas(*n, sit=False):
    """
    --> Função para analisar as notas de uma classe.
    :param n: As notas.
    :param sit: Opcional, para saber qual é a situação da classe.
    :return: Dicionário com os resultados.
    """
    med = sum(n) / len(n)
    lista = {'Total': len(n), 'Maior': max(n), 'Menor': min(n), 'Média': f'{med:.2f}'}
    if sit:
        if med >= 7:
            s = 'Boa'
        elif 6 <= med < 7:
            s = 'Razoável'
        else:
            s = 'Ruim'
        lista['Situação'] = s
    return lista


def ajuda():
    from time import sleep
    while True:
        print('\033[m\033[30;43m~'*27)
        print('  SISTEMA DE AJUDA PYTHON')
        print('~'*27)
        a = input('\033[mFunção ou biblioteca> ')
        if a.lower().strip() == 'quit':
            print('\033[30;41m~'*12)
            print('  ATÉ LOGO')
            print('~'*12)
            break
        print('\033[30;44m~'*(35 + len(a)))
        print(f'  ACESSANDO O MANUAL DO COMANDO: {a}')
        print('~'*(35 + len(a)))
        sleep(0.4)
        print('\033[m\033[30;7m')
        help(a)
        sleep(0.4)


titulo('Exercício 101', 50, 34)
ano = int(input('Ano de nascimento: '))
print(voto(ano))

titulo('Exercício 102', 50, 34)
print(fatorial(6, True))
print(f'7! = {fatorial(7)}')
print(f'6! + 5! = {fatorial(6) + fatorial(5)}\n')
help(fatorial)

titulo('Exercício 103', 50, 34)
nome = input('Nome do jogador: ')
gols = input('Quantidade de gols: ')
ficha(nome, gols)

titulo('Exercício 104', 50, 34)
n = inputInt('Digite um número: ')
print(f'Você digitou o número {n}')

titulo('Exercício 105', 50, 34)
print(notas(4.5, 5.2, 9.75, 1.5, 5.8, sit=True))

titulo('Exercício 106', 50, 34)
ajuda()
