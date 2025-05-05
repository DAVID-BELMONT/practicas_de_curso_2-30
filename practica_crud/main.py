

from controladores.gestor_usuarios import GestorUsuarios

def mostrar_menu():
    print("\n========= MENÚ CRUD =========")
    print("1. Crear usuario")
    print("2. Mostrar usuarios (paginados)")
    print("3. Actualizar nombre de usuario")
    print("4. Eliminar usuario")
    print("5. Ver total de usuarios")
    print("6. Salir")
    print("=============================")

def main():
    gestor = GestorUsuarios()
    
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            usuario = input("introduce tu nombre de Usuario (máx 10 caracteres): ejemplo: ")
            nombre = input("el Nombre del usuario no deve exeder un (máx 20 caracteres): ")
            password = input("introduce tu Contraseña: ")
            resultado = gestor.crear_usuario(usuario, nombre, password)
            print("\nResultado:")
            print(resultado)

        elif opcion == "2":
            try:
                pagina = int(input("Página: "))
                por_pagina = int(input("Usuarios por página: "))
                usuarios = gestor.paginator(pagina, por_pagina)
                for u in usuarios:
                    print(u)
            except ValueError:
                print("Error: debes ingresar números válidos.")

        elif opcion == "3":
            usuario = input("Nombre de usuario a actualizar: ")
            nuevo_nombre = input("Nuevo nombre (máx 20 caracteres): ")
            resultado = gestor.actualizar_usuario(usuario, nuevo_nombre)
            print(resultado)

        elif opcion == "4":
            usuario = input("Usuario a eliminar: ")
            resultado = gestor.eliminar_usuario(usuario)
            print(resultado)

        elif opcion == "5":
            print(f"Total de usuarios: {gestor.counter()}")

        elif opcion == "6":
            print("Saliendo del programa..........")
            break

        else:
            print("Opción inválida. introduce un numero del 1 al 6.")

if __name__ == "__main__":
    main()
