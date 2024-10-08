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
        if linea[0] not in ["M", "F"]:
            observacion.append("Género inválido")
        
        # Ejemplo de validación para grupo etario
        if len(linea) > 1 and (linea[1] == '' or not linea[1].isdigit()):
            observacion.append("Grupo etario no válido")
        
        # Ejemplo de validación para jurisdicción
        if len(linea) > 2 and linea[2] == '':
            observacion.append("Falta jurisdicción de residencia")
        
        # Ejemplo de validación para vacuna
        if len(linea) > 3 and linea[3] == '':
            observacion.append("Falta tipo de vacuna")
        
        # Guardar datos o inconsistencias
        if observacion:
            inconsistencias.append(linea + [', '.join(observacion)])  # Combina todas las observaciones
        else:
            datos_limpios.append(linea)
    
    return datos_limpios, inconsistencias