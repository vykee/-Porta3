# Este programa es un menu que permite a una empresa de hacer
#el inventario de los productos que le restan y le que vendio.
import pandas as pd
df = pd.read_excel(r'C:\Users\Usuario\Documents\Producto.xlsx')
# Aqui, python pide al usuario de hacer un choice in el menu que le presenta
choice = 0
while choice !=5:
   choice=int(input("1.Ver producto\n2.Ver la cantidad que compro\n3.cantidad in stock\n4.Cantidad que vendio\n5-Salir\n6-R: " ))
   if choice==1:
     c = df.iloc[1:7,0:2]
     print(c)
     print("     ************")
   elif choice==2:
     c1 = df.iloc[1:7,1:5]
     print(c1)
     print("     ************")
   elif  choice==3:
     c2 = df.iloc[1:7,9:12]
     print(c2)
     print("     ************")
   elif choice==4:
     c3 = df.iloc[1:7,5:8]
     print(c3)
     print("     ************")

if choice == 5:
    pass
