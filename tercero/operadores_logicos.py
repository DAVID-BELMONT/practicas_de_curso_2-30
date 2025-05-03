


'''# OPERADORES ARITMÉTICOS'''

a = 4
b = 6

print(a + b) # suma
print(a - b) # resta
print(a * b) # multiplicación
print(a / b) # división
print(a // b) # división entera
print(a % b) # Môdulo, devuelve el resto de la división
print(a ** b) # Elevado a...
print(-a) # Negación, cambiar el valor positivo o negativo 

# ==================================================================

'''OPERADORES LÓGICOS'''
# Utlizados para combinar o invertir expresiones condicionales (booleanos)

a = True
b = False
x = 10

#AND (Y lógico)
print(a and b) # imprime False

#Ejemplo
print(x > 5 and x < 20) # True
print(x < 11 and x != 10) # False

#=================================
#OR (O lógico)
print( a or b) # Imprime True
print(x < 5 or x > 8) # True

#=================================
#NOT (Negación lógica)
print(not a) # False
print(not(x > 5)) # False

#===============================================

'''OPERADORES DE COMPARACIÓN'''

# IGUAL A...
a = 5
b = 12
print(a == b) # False

# DISTINTO DE...
print(a != b) # True

# MAYOR QUE...
print( a > b) # False

# MENOR QUE...
print(a < b) # True

# MAYOR O IGUAL QUE...
print(a >= b) # False

# MENOR O IGUAL QUE...
print(a <= b) # True

#=====================================
'''OPERADORES DE ASIGNACIÓN'''

# Asignaciôn simple
x = 20

# Suma y asigna
x += 1
print(x) # 4

# Resta y asigna
x -= 2
print(x)

# Multiplica y asigna
x *= 5
print(x)

# Divide y asigna
x /= 2
print(x)

#División entera y asigna
x //= 2
print(x)

# Módulo y asigna
x %= 5
print(x)

# Potencia y asigna
x **= 4
print(x)

