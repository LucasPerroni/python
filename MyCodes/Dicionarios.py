from datetime import datetime

x = -1
lista = {}
lista1 = []
continuar = 's'

while continuar == 's':
    while True:
        lista['Nome'] = input('\033[30mNome: ').strip().title()
        i = int(input('Ano de nascimento: '))
        lista['Idade'] = datetime.today().year - i
        lista['Carteira'] = int(input('Carteira de trabalho (0 não tem): '))
        if lista['Carteira'] == 0:
            lista1.append(lista.copy())
            lista.clear()
            break
        else:
            lista['Contratacao'] = int(input('Ano de contratação: '))
            lista['Salario'] = float(input('Salário: R$'))
            lista['Aposentadoria'] = lista['Contratacao'] + 35 - i
            lista1.append(lista.copy())
            lista.clear()
            break
    continuar = input('Continuar (S/N)? ').strip().lower()[0]
    while continuar not in 'sn':
        continuar = input('\033[31m[ERRO]\033[37m Continuar (S/N)? ').strip().lower()[0]
    print('\033[31m-\033[30m'*70)

print('Código  Nome')
for c in lista1:
    x += 1
    print(f'{x:^6}  ' + c['Nome'])
while True:
    print('\033[34m-\033[30m'*50)
    valor = int(input('Código (99 para parar): '))
    if valor == 99:
        break
    elif valor > x or valor < 0:
        print('\033[31m[ERRO]\033[30m')
        continue
    print(f'''Nome: {lista1[valor]["Nome"]}
Idade: {lista1[valor]["Idade"]}
Carteira de trabalho: {lista1[valor]["Carteira"]}''')
    if lista1[valor]['Carteira'] > 0:
        print(f'''Ano de contratação: {lista1[valor]["Contratacao"]}
Salário: R${lista1[valor]["Salario"]:.2f}
Idade de aposentatoria: {lista1[valor]["Aposentadoria"]}''')
