def leiaDinheiro(x):
    a = input(x)
    while True:
        a = a.replace(',', '.')
        try:
            float(a)
        except ValueError:
            print(f'\033[31m[ERRO] "{a}" é um preço inválido.\033[m')
            a = input(x)
        else:
            break
    a = float(a)
    return a
