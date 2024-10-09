import csv

def guardar_inconsistencias(inconsistencias, archivo_salida):
    """
    Guarda las inconsistencias en un archivo CSV.

    Parámetros:
    inconsistencias (list): Lista de registros con inconsistencias.
    archivo_salida (str): Ruta del archivo donde se guardarán las inconsistencias.
    """
    with open(archivo_salida, 'w', encoding='utf-8', newline='') as f:
        escritor = csv.writer(f)
        escritor.writerow(["sexo", "grupo_etario", "jurisdiccion_residencia", 
                           "jurisdiccion_residencia_id", "depto_residencia", 
                           "depto_residencia_id", "jurisdiccion_aplicacion", 
                           "jurisdiccion_aplicacion_id", "depto_aplicacion", 
                           "depto_aplicacion_id", "fecha_aplicacion", 
                           "vacuna", "cod_dosis_generica", "nombre_dosis_generica", 
                           "condicion_aplicacion", "orden_dosis", "lote_vacuna", 
                           "id_persona_dw", "OBSERVACIÓN"])
        
        for linea in inconsistencias:
            escritor.writerow(linea)  # Usa writerow para manejar automáticamente las comas

def guardar_estadisticas_en_csv(estadisticas, nombre_archivo):
    """
    Guarda las estadísticas en un archivo CSV.

    Parámetros:
    estadisticas (dict): Diccionario con las estadísticas a guardar.
    nombre_archivo (str): Ruta del archivo donde se guardarán las estadísticas.
    """
    with open(nombre_archivo, mode='w', newline='', encoding='utf-8') as archivo_csv:
        escritor = csv.writer(archivo_csv)
        escritor.writerow(['Categoria', 'Descripcion', 'Cantidad'])
        
        # Distribución por Género
        for genero, cantidad in estadisticas['Distribucion por Genero'].items():
            escritor.writerow(['Distribucion por Genero', genero, cantidad])
            
        # Vacunas Aplicadas por Tipo
        for vacuna, cantidad in estadisticas['Vacunas Aplicadas por Tipo'].items():
            porcentaje = f"{cantidad:.2f}%"  # Formatear como cadena solo para el CSV
            escritor.writerow(['Vacunas Aplicadas por Tipo', vacuna, porcentaje])
            
        # Dosis por Jurisdicción de Residencia
        for jurisdiccion, cantidad in estadisticas['Dosis por Jurisdiccion de Residencia'].items():
            escritor.writerow(['Dosis por Jurisdiccion de Residencia', jurisdiccion, f"{cantidad} dosis"])
            
        # Segunda Dosis por Jurisdicción
        for jurisdiccion, cantidad in estadisticas['Segunda Dosis por Jurisdiccion'].items():
            escritor.writerow(['Segunda Dosis por Jurisdiccion', jurisdiccion, f"{cantidad} dosis"])
            
        # Dosis de Refuerzo para Mayores de 60
        escritor.writerow(['Dosis de Refuerzo para Mayores de 60', '', estadisticas['Dosis de Refuerzo para Mayores de 60']])
        
        # Dosis por Grupo Etario
        for grupo_etario, cantidad in estadisticas['Dosis por Grupo Etario'].items():
            escritor.writerow(['Dosis por Grupo Etario', grupo_etario, f"{cantidad} dosis"])

        # Dosis por Condición de Aplicación
        for condicion, cantidad in estadisticas['Dosis por Condición de Aplicación'].items():
            escritor.writerow(['Dosis por Condición de Aplicación', condicion, f"{cantidad} dosis"])

        # Vacunas Administradas por Fecha
        for fecha, cantidad in estadisticas['Vacunas Administradas por Fecha'].items():
            escritor.writerow(['Vacunas Administradas por Fecha', fecha, f"{cantidad} dosis"])
