# Logic values

value = 0
list = []
c = 0

value=(input("Introdue dos valores logicas: "))
list=value.split(',')
for x in list:
    c = int(list[0]) ^ int(list[1])
print(c)


