n = int(input('Digite um número e receba a soma até ele: '))
lista = []
while n > 0:
    lista.append(n)
    n = n - 1
else:
    print('A soma de todos os números é: ', sum(lista))

