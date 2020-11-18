def aumentar(x, y, z=False):
    a = x + (y/100)*x
    return a if not z else moeda(a)


def diminuir(x, y, z=False):
    a = x - (y/100)*x
    return a if not z else moeda(a)


def metade(x, y=False):
    a = x / 2
    return a if not y else moeda(a)


def dobro(x, y=False):
    a = x * 2
    return a if not y else moeda(a)


def moeda(x):
    a = f'R${x:.2f}'.replace('.', ',')
    return a


def resumo(x, y=0, z=0):
    print('-'*(21 + len(dobro(x, True))))
    print(f'{"RESUMO DO VALOR":^{(21 + len(dobro(x, True)))}}')
    print('-'*(21 + len(dobro(x, True))))
    print(f'Preço analisado: \t{moeda(x)}')
    print(f'Dobro do preço: \t{dobro(x, True)}')
    print(f'Medade do preço: \t{metade(x, True)}')
    print(f'Aumento de {y:>2}%: \t{aumentar(x, y, True)}')
    print(f'Redução de {z:>2}%: \t{diminuir(x, z, True)}')
    print('-'*(21 + len(dobro(x, True))))
