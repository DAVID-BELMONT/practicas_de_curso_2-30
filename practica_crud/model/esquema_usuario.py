

import re  # importamos el módulo de expresiones regulares


def validar_datos(usuario: str, nombre: str) -> list[str]:
    """
    Verifica que el usuario no exceda 10 caracteres y el nombre 20.
    Retorna una lista de errores en caso de que se incumplan las reglas.
    """
    errores = []




    if len(usuario) > 10:
        errores.append("El campo 'usuario' no debe tener más de 10 caracteres.")
    if len(nombre) > 20:
        errores.append("El campo 'nombre' no debe tener más de 20 caracteres.")



       # Verifica que solo use letras, números y guión bajo
    if not re.fullmatch(r'^[a-zA-Z0-9_.]+$', usuario):
        errores.append("El 'usuario' solo puede contener letras, números, guiones bajos y puntos (sin espacios ni otros símbolos).")


    return errores

