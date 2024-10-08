import csv

def guardar_inconsistencias(inconsistencias, archivo_salida):
    with open(archivo_salida, 'w', encoding='utf-8') as f:
        f.write("sexo,grupo_etario,jurisdiccion_residencia,jurisdiccion_residencia_id,depto_residencia,depto_residencia_id,jurisdiccion_aplicacion,jurisdiccion_aplicacion_id,depto_aplicacion,depto_aplicacion_id,fecha_aplicacion,vacuna,cod_dosis_generica,nombre_dosis_generica,condicion_aplicacion,orden_dosis,lote_vacuna,id_persona_dw,OBSERVACIÓN\n")
        for linea in inconsistencias:
            f.write(",".join(linea) + "\n")

def guardar_estadisticas_en_csv(estadisticas, nombre_archivo):
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