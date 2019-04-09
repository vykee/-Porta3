# Este programa  de microeconomia permite de calcular la demanda potencial de un producto
# dado la cantidad de la poblacion de un localidad, el precio promedio del producto en el mercado,
# la cantidad promedio de consumo per capita en el mercado, la tasa de fidelidad es decir
# la tasa de los clientes fieles a este producto.

q = 5
c = 0
p = 2
Q = 0
t = 0

c = int(input("Introduce la poblacion:  "))
t = int(input("Introduce la tasa de los clientes: en % "))
n = c*t/100
Q = q*p*n
print("$",Q)

