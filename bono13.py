# Number of common Digit
num1 = 0
num2 = 0
n = 0
num1=int(input("Numeros1: "))
num2=int(input("Numeros2: "))
for i in range(1,min(num1,num2)+2):
    if num1%i==num2%i==0:
            n+=1
print(n)
