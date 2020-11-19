try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except (ValueError, TypeError):
    print('Tivemos um problema com o tipo de dado que você digitou.')
except ZeroDivisionError:
    print('Não é possível dividir por zero.')
except KeyboardInterrupt:
    print('\nO usuário preferiu não informar todos os dados.')
else:
    print(f'O resultado é {r:.1f}')
finally:
    print('Volte sempre!')
