def titulo(escrita, tamanho, cor):
    print(f'\033[{cor}m-' * tamanho)
    print(f'{escrita:^{tamanho}}')
    print(f'\033[{cor}m-\033[m' * tamanho)


def soma(*n):
    print(f'Soma = {sum(n)}   Quantidade de números: {len(n)}')


def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1
    print(lst)


titulo('Oloko meu', 40, 34)
titulo('aaa', 30, 0)
titulo('sla bixo', cor=31, tamanho=20)

soma(1, 2, 3, 1, 3, 10)
soma(17, 13)

lista = [1, 3, 4, 2, 15]
dobra(lista)
