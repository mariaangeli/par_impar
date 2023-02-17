# programa para verificar si un numero es par o impar

# input
x = int(input("Digite el valor de x: "))

# processing
r = x%2
if r==0:
    msj="PAR"
else:
    msj="IMPAR"

# output
print(" El numero " + str(x) + " es " + msj)