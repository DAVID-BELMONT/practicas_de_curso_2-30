



from interfaces.icatalog import ICatalog
from model.esquema_usuario import validar_datos
from utilidades.paginador import paginar_lista

class GestorUsuarios(ICatalog):
    def __init__(self):
        # Carga usuarios desde archivo .json y los guarda en memoria
        self.usuarios = [ ]

    def crear_usuario(self, usuario, nombre, password, estatus=True):
        """
        Crea un usuario validando longitud de campos y evitando duplicados.
        Devuelve errores o el usuario creado (sin contraseña).
        """
        errores = validar_datos(usuario, nombre)

        # Verifica si ya existe el nombre de usuario
        if any(u["usuario"] == usuario for u in self.usuarios):
            errores.append("El usuario ya existe.")

        if errores:
            return {"error": errores}

        # Diccionario con los datos del usuario
        nuevo = {
            "usuario": usuario,
            "nombre": nombre,
            "password": password,
            "estatus": estatus
        }

        self.usuarios.append(nuevo)

        # Retornamos el usuario, excluyendo la contraseña
        return {k: v for k, v in nuevo.items() if k != 'password'}

    def actualizar_usuario(self, usuario, nuevo_nombre):
        """
        Busca el usuario por nombre y modifica su campo 'nombre' si es válido.
        """
        for u in self.usuarios:
            if u["usuario"] == usuario:
                if len(nuevo_nombre) > 20:
                    return {"error": "El nombre excede los 20 caracteres."}
                u["nombre"] = nuevo_nombre
                return {k: v for k, v in u.items() if k != 'password'}
        return {"error": "Usuario no encontrado."}

    def eliminar_usuario(self, usuario):
        """
        Elimina un usuario por su identificador único.
        """
        for i, u in enumerate(self.usuarios):
            if u["usuario"] == usuario:
                del self.usuarios[i]
                return {"mensaje": "Usuario eliminado"}
        return {"error": "Usuario no encontrado"}

    def paginator(self, page: int, rows: int) -> list[dict]:
        """
        Retorna una página de usuarios sin incluir la contraseña.
        """
        datos = paginar_lista(self.usuarios, page, rows)
        return [{k: v for k, v in u.items() if k != 'password'} for u in datos]

    def counter(self) -> int:
        """
        Devuelve el total de usuarios en el sistema.
        """
        return len(self.usuarios)