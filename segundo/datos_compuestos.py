

"""
los datos compuestos son estructuras que pueden contener múltiples valores, 
a diferencia de los tipos simples como int,
float o bool. Estos son útiles para organizar y 
manipular conjuntos de datos relacionados. Los principales tipos de datos compuestos 

"""

# 1. Listas [list]  CORCHETES

lista = ["David" , "soy Belmont" , False , 1.85]
print(lista [1]) # DAVID


# 2. Tuplas (tuple)   PARENTECIS

mi_tupla = (1, 2, 3)
print(mi_tupla[0])  # 1


# 3. Conjuntos  {set}  LLAVES

mi_conjunto = {1, 2, 3, 3}
print(mi_conjunto)  # {1, 2, 3}


# 4. Diccionarios (dict)    clave : valor  __ se busca por clave 
mi_diccionario = {"nombre": "Camillo", "edad": 30}
print(mi_diccionario["nombre"])  # "Camillo"
