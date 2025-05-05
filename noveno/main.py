
from clases.roles import Roles
from clases.usuarios import Usuarios

def mostrar_catalogo(catalogo, nombre: str, page: int = 1, rows: int = 10):
    print(f"\n=== Catálogo de {nombre} ===")
    print(f"Total de elementos: {catalogo.counter()}")
    print(f"Elementos página {page} (máx {rows} por página):")
    for item in catalogo.paginator(page, rows):
        print("-", item)

def main():
    # se debio tener un folder para crear estos y aqui solo se mandarian a llamar la informacion, parra no tener el codigo acoplado en el main.
    # es decir poder borrar el archivo sin tner que reescribir mucho codigo solo llamar metodos.
    roles = Roles()
    roles.lista_roles = [
        "Administrador", "Editor", "Lector", "Invitado", "Moderador", 
        "Supervisor", "Analista", "Auditor", "Tester", "Develops"
    ]
    
    usuarios = Usuarios()
    usuarios.roles = [
        "marco", "laura", "pedro", "sofía", "jorge", 
        "diana", "mateo", "andrea", "alejandro", "valentina"
    ]



    mostrar_catalogo(roles, "Roles")
    mostrar_catalogo(usuarios, "Usuarios")

if __name__ == "__main__":
    main()
