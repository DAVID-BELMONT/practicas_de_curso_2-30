""""
las variables es cualquier dato qu se almacenan 
en la memoria de nustro programa 


"""


a = 5
b = 8
c = a + b
print(c)



# concatenar unir cadenas de string

nombre = "david"
bienbenida = "hola " + nombre + " ¿como estas?"

# los espacios son un caracter 

print(bienbenida)


# los f string van de la mano con los corchetes {} para concatenar  texto y numero si que cuando la variable sea un mero marque error
# los f string convierte las variables en TEXTO por eso hace que no marue un error la consola

nom = 2
saludo = f"Hola  {nom}  ¿como estas?"
print(saludo)


#operadores de pertenecia (in / no in)

print("david" in bienbenida) #true -- verdas ---  david esta en la variable bienvenida 
print("david" not in saludo) # true ---- david no esta en la variable saludo 
