#Multiplication of the given number:

entrada=input("Digite los numeros: ")
lista=entrada.split(',')
mult = 1
for i in lista:
    mult = mult * int(i)
print(mult)
