def validar_genero(genero):
    """Valida si el género es 'M' o 'F'."""
    return genero in ["M", "F"]

def validar_grupo_etario(grupo_etario):
    """Valida si el grupo etario es un número entero válido."""
    return grupo_etario.isdigit() and 0 <= int(grupo_etario) <= 120

def validar_jurisdiccion(jurisdiccion):
    """Valida si la jurisdicción no está vacía."""
    return bool(jurisdiccion)

def validar_vacuna(vacuna):
    """Valida si el tipo de vacuna no está vacío."""
    return bool(vacuna)

def detectar_inconsistencias(datos):
    """
    Detecta inconsistencias en los datos y separa los registros válidos de los no válidos.

    Parámetros:
    datos (lista): Lista de registros (cada registro es una lista).

    Retorna:
    tupla: Una tupla que contiene dos listas:
        - datos_limpios: Registros válidos.
        - inconsistencias: Registros inválidos con observaciones.
    """
    datos_limpios = []
    inconsistencias = []
    
    for linea in datos:
        observacion = []
        
        # Validaciones
        if not validar_genero(linea[0]):
            observacion.append("Género inválido")
        
        if len(linea) > 1 and not validar_grupo_etario(linea[1]):
            observacion.append("Grupo etario no válido")
        
        if len(linea) > 2 and not validar_jurisdiccion(linea[2]):
            observacion.append("Falta jurisdicción de residencia")
        
        if len(linea) > 3 and not validar_vacuna(linea[3]):
            observacion.append("Falta tipo de vacuna")
        
        # Guardar datos o inconsistencias
        if observacion:
            inconsistencias.append(linea + [', '.join(observacion)])  # Combina todas las observaciones
        else:
            datos_limpios.append(linea)
    
    return datos_limpios, inconsistencias