#crie um programa que leia o nome de uma cidade e diga se ela começa com o nome 'SANTO'.
from time import sleep #import do sleep
print('\033[31m---------------------------------------------------\033[m') #titúlo
cid = str(input('Nome da cidade: ')).strip() #input do nome da cidade na variavel cid
print(f'A cidade de \033[31m{cid}\033[m começa com a palavra Santo?') #print formatado
print('\033[31mANALISANDO...\033[m') #simulacao loading
sleep(1) #sleep
print(f'Resultado: {cid[:5].upper() == "SANTO"}') #procura santo no input
print('\033[31m---------------------------------------------------\033[m')
