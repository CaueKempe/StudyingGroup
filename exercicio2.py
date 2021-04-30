num = int(input("Escolha um número: "))
lista = []
while num > 0:
    print(num)
    lista.append(num)
    num = num - 1
else:
    print("Soma de todos os antecessores deste número que são maiores que 0 é:{}".format(sum(lista)))
