from MyCodes.personal import title, inputInt, inputFloat
from urllib.request import urlopen

title('Exercício 113', 50, 34)
a = inputInt('Digite um valor inteiro: ')
b = inputFloat('Digite um valor real: ')
print(f'O valor inteiro é {a} e o valor real é {b:.1f}.')

title('Exercício 114', 50, 34)
try:
    pag = urlopen('http://www.pudim.com.br/')
except:
    print('\033[31mO site não está acessível!\033[m')
else:
    print('\033[32mO site está acessível!\033[m')
