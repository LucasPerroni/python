def titulo(escrita, tamanho, cor=0):
    """
    --> Cria um título no programa.
    :param escrita: Parte escrita do título
    :param tamanho: Tamanho do título
    :param cor: Cor do título (30 = Branco; 31 = Vermelho; 32 = Verde;
                               33 = Amarelo; 34 = Azul; 35 = Roxo;
                               36 = Ciano; 37 = Cinza; 0 = Nenhuma)
    :return: Sem retorno
    """
    print(f'\033[{cor}m-' * tamanho)
    print(f'{escrita:^{tamanho}}')
    print(f'\033[{cor}m-\033[m' * tamanho)


def teste(b):
    a = 8
    b += 4
    c = 2
    print(f'''A dentro vale {a}
B dentro vale {b}
C dentro vale {c}''', end='\n'*2)


def teste2():
    global a
    a = 10


def somar(a=0, b=0, c=0):
    s = a + b + c
    return s


def fatorial(n):
    f = 1
    while n > 0:
        f *= n
        n -= 1
    return f


help(titulo)
# help(titulo) = print(titulo.__doc__)
titulo('Olá', 5)

a = 5
teste(a)
print(f'A fora vale {a}', end='\n'*2)
# print(f'B fora vale {b})   [ERRO]
# print(f'C fora vale {c})   [ERRO]
teste2()
print(f'A fora vale {a}', end='\n'*2)

v1 = somar()
v2 = somar(2, 7, 1)
v3 = somar(2, 4)
print(f'As somas valem {v1}, {v2} e {v3}.', end='\n'*2)

print(fatorial(9))
