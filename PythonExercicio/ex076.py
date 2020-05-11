#crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
#no final, mostre uma listagem de preços organizado os dados em forma tabular.
print('=' * 40)
print('{:^40}'.format('LISTAGEM DE PREÇOS'))
print('=' * 40)
listagem = ('Lápis', 1.75,
            'Borracha', 2,
            'Caderno', 15.90,
            'Estojo', 25,
            'Tranferidor', 4.20,
            'Compasso', 9.99,
            'Mochila', 120.32,
            'Canetas', 22.30,
            'Livro', 34.90)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    elif pos % 2 == 1:
        print(f'R${listagem[pos]:>7.2f}')
print('=' * 40)
