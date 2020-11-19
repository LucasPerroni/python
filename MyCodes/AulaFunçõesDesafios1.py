from random import randint
from time import sleep


def titulo(escrita, tamanho):
    print(f'-' * tamanho)
    print(f'{escrita:^{tamanho}}')
    print(f'-' * tamanho)


def area(a, b):
    S = a * b
    print(f'A área de um terreno {a:.2f}x{b:.2f} é {S:.2f} m².')


def escreva(esc):
    print('~'*(len(esc) + 2))
    print(f'{esc:^{len(esc) + 2}}')
    print('~'*(len(esc) + 2))


def contagem(a, b, c):
    print('-'*50)
    if c == 0:
        c = 1
    if c < 0:
        c *= -1
    if b > a:
        print(f'Contagem de {a} até {b} com passo {c}', flush=True)
        sleep(0.5)
        while b >= a:
            print(a, end=' ')
            a += c
            sleep(0.2)
        print('')
    elif a > b:
        print(f'Contagem de {a} até {b} com passo {c}', flush=True)
        sleep(0.5)
        while a >= b:
            print(a, end=' ')
            a -= c
            sleep(0.3)
        print('')


def maior(*n):
    print('Analisando os valores...')
    pos = 0
    if not n:
        print('Não foram informados valores')
        print('')
    else:
        while pos < len(n):
            print(n[pos], end=' ')
            pos += 1
        print('')
        print(f'Foram informados {len(n)} valores ao todo')
        print(f'O maior valor é {max(n)}')
        print('')


def sortear(lst, rng):
    print(f'Sorteando {rng} valores da lista: ', end='')
    for c in range(0, rng):
        x = randint(1, 10)
        lst.append(x)
        print(f'{x}', end=' ')
    print('')


def somaPar(lst):
    lst1 = []
    for c in lst:
        if c % 2 == 0:
            lst1.append(c)
    print(f'A soma dos valores pares de {lst} é {sum(lst1)}')


titulo('Exercício 96', 50)
print('Controle de terrenos')
l = float(input('Largura (m): '))
c = float(input('Comprimento (m): '))
area(l, c)

titulo('Exercício 97', 50)
escreva('Olá')
escreva('Como vai?')
escreva('Curso Python, aula de funções!')

titulo('Exercício 98', 50)
contagem(1, 10, 1)
contagem(10, 0, 2)
print('-'*50)
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contagem(i, f, p)

titulo('Exercício 99', 50)
maior(1, 2, 43, 1, 2, 32)
maior(2, 3, -1, 5)
maior(-5, -32, -45, -2)
maior()

titulo('Exercício 100', 50)
lista = []
sortear(lista, 10)
somaPar(lista)
