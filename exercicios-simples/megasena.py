from random import randint
from time import sleep

print('         Jogo da Megasena        ')
print(37 * '-')
qtde = int(input('Quantos jogos que comprar? '))

total = 1
lista = []
jogos =[]

while total < qtde:
    cont = 0
    while True:
        numero = randint(1, 60)
        if numero not in lista:
            lista.append(numero)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total += 1

print('-=' * 3, f'SORTEANDO {total} JOGO(S)', '=-' * 3)
for i, val in enumerate(jogos):
    print(f'Jogo {i+1}: {val}')
    sleep(1)
print('-=' * 5, 'BOA SORTE', '=-' * 5)
