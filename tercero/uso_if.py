

# CONDICIONALES IF, ELIF, ELSE

num = 10

if num % 2 == 0:
    print(f"{num} es un número par.")
elif num > 10:
    print(f"{num} es mayor que 10.")
else:
    print(f"{num} es impar o menor que 10.")

# ESTRUCTURAS ITERATIVAS

# FOR
for i in range(1,6):
    print(f"El cuadrado de {i} es {i **2}")

# WHILE

n = 0
limite = 5

while n <= limite:
    print(f"n = {n}")
    n += 1