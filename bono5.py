# The Greatest Common Divisor

v1 = 0
v2 = 0
v3 = 0

v1=int(input("Valor1: "))
v2=int(input("Valor2: "))
v3=int(input("Valor3: "))

if v1 <= v2 and v1 <= v3:
    gcd = v1
elif v2 <= v1 and v2 <= v3:
    gcd = v2
else:
    gcd = v3
while True:
    if v1%gcd == 0 and v2%gcd == 0 and v3%gcd == 0:
        print(gcd)
        break
    else:
        gcd -= 1





