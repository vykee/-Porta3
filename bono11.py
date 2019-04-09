# Greatest Commom Divisor 2

num = 0
num1 =  0
num=int(input("Num: "))
num1=int(input("Num1: "))

if num <= 0:
    gcd = num
else:
    gcd = num1
while True:
    if num%gcd==0 and num1%gcd==0:
        print(gcd)
        break
    else:
        gcd -= 1
