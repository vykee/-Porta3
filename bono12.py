# Prime or not prime

n = 0
n=int(input("Digite un numero: "))
if n >= 1:
    for x in range(2,n//2):
        if n % x == 0:
            print("Yes")
            break
    else:
        print("No")
else:
    print("No")

