#faça um programa que leia um número qualquer e mostre seu fatorial
print('\033[33m-=-=-=-=-=-=-=-=-=-=-=FATORIAL=-=-=-=-=-=-=-=-=-=-=-\033[m') #titulo
num = int(input('Digite um número para calcular seu fatorial: ')) #input do número desejado
c = num #define o contador como o num inserido no input
f = 1 #fatorial é definido como 1
print(f'Calculando {num}! = ', end='') #formato do fatorial
while c > 0: #enquanto o contador for maior que 0
    print(f'{c}', end='') #mostre o contador
    print(' x ' if c > 1 else ' = ', end='') #se o c for maior que 1 coloque x, senão coloque =
    f = f * c #fatorial é definido como f * c
    c -= 1 #contador é contador - 1
print(f'\033[33m{f}\033[m') #resultado do fatorial
print('\033[33m-\033[m' * 52)
