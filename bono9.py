# fuct_for_prime

prime = []
num1 = int(input("Digite un primer valor: "))
num2 = int(input("Digite un valor mayor que num1: "))
for valor in range(num1,num2 + 1):
    num = 0
    if valor > 1:
        for i in range(2,valor):
            if (valor % i) == 0:
                num=1
                break
        if(num==0):
            print(valor,end=",")



