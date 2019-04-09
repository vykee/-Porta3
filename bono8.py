# Compare two numbers

valors = 0
lista = []

valors=(input("Digite dos valores: "))
lista=valors.split(',')
for i in lista:
    if lista[0] == lista[1]:
        print(lista[0],"es igual a",lista[1])
    elif lista[0] >= lista[1]:
        print(lista[0],"es mayor que",lista[1])
    elif lista[0] <= lista[1]:
        print(lista[0], "es menor que",lista[1])
