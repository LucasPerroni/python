i = int(input('Número de linhas e colunas da matriz quadrada: '))
j = i
a = 1
b = 0
lista = {}
for i in range(1, i + 1):
    for j in range(1, j + 1):
        x = float(input(f'Valor de [{i}][{j}]: '))
        lista[f'x{i}{j}'] = x
print('\033[31m-\033[30m' * 50)
print('Matriz = ', end='')
while True:
    if b < j:
        b += 1
        print(f"[{lista[f'x{a}{b}']:^5.2f}]", end=' ')
    else:
        b = 1
        a += 1
        print('')
        print(f"         [{lista[f'x{a}{b}']:^5.2f}]", end=' ')
    if a == i and b == j:
        break
print('')
if i == 2 or i == 3:
    while True:
        print('\033[31m-\033[30m' * 50 + '''\033[34m
Soma = 1
Determinante = 2
Sair = 3\033[30m''')
        opcao = int(input('Opção: '))
        if opcao == 3:
            break
        elif opcao == 1:
            print(f'Soma = {sum(lista.values()):.2f}')
        elif opcao == 2 and i == 2:
            raiz2 = lista['x11'] * lista['x22'] - (lista['x12'] * lista['x21'])
            print(f'Determinante = {raiz2:.2f}')
        elif opcao == 2 and i == 3:
            raiz3 = ((lista['x11'] * lista['x22'] * lista['x33'] +
                      lista['x12'] * lista['x23'] * lista['x31'] +
                      lista['x13'] * lista['x21'] * lista['x32']) -
                     (lista['x13'] * lista['x22'] * lista['x31'] +
                      lista['x12'] * lista['x21'] * lista['x33'] +
                      lista['x11'] * lista['x23'] * lista['x32']))
            print(f'Determinante = {raiz3:.2f}')
