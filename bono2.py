# Sum of two squares of elements

def suma_cuadrada(entrada):
    i = 1
    while (i * i <= entrada):
        j = 1
        while(j * j <= entrada):
            if(i*i + j * j == entrada):
                return True
            j = j + 1
        i = i + 1
    return False
entrada=(int(input("Digite un numero: ")))
if (suma_cuadrada(entrada)):
    print("Siii")
else:
    print("Nope")

