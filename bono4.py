# The last digtit

listas = []
num = 0
c = 0
l = 0

num=(input("Digite dos numeros: "))
listas = num.split(',')
for x in listas:
        c = int(listas[0]) ** int(listas[1])
        l = c%10
print(l)










