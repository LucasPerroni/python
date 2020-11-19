from MyCodes.personal import title
from MyCodes.AulaMódulos.utilidades import dados, moeda

title('Exercícios 107, 108, 109, 110, 111 e 112', 50, 34)
p = dados.leiaDinheiro('Preço: R$')
moeda.resumo(p, 50, 65)
