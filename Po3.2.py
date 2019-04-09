# este programa permite saber si el costo  y la disponibilidad de un producto de acuerdo a un inventario hecho
# Installamos y importamos la libreria pandas para poder importar el documento excel
import pandas as pd
#Abrimos y imprimos  el documento excel usando pandas
df = pd.read_excel(r'C:\Users\Usuario\Documents\Producto.xlsx')
choice=int(input("1.Ver producto\n2.Salir\nR: " ))
# Aqui, si el usuario eligo 1 el 1, entonces, debe imprimirle la columna
# de producto, de costo unitaria, y la cantidad que esta in stock
# sino, el programa debe acabar de ejecutar.
if choice==1:
    c = df.iloc[1:7,0:2]
    print(c)
else:
    pass
