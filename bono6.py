#Sum of two numbers

n = 0
list = []
sum = 0
n=(input("Digite dos numeros: "))
list=n.split(',')
for i in list:
    sum = int(sum) + int(i)
    print(sum)

