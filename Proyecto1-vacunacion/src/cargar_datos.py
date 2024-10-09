import csv

class CargarDatos:
    def cargar_datos(self, archivo1: str) -> list:
        """
        Carga los datos desde un archivo CSV y los devuelve como una lista de diccionarios.

        Parámetros:
        archivo1 (str): Ruta del archivo CSV a cargar.

        Retorna:
        list: Lista de diccionarios donde cada diccionario representa una fila del CSV.
        """
        datos = []
        
        # Cargar datos del archivo
        with open(archivo1, 'r', encoding='utf-8') as f:
            # Leer encabezados
            encabezados = f.readline().strip().split(',')
            for linea in f:
                campos = linea.strip().split(',')
                # Crear un diccionario para cada fila
                fila = dict(zip(encabezados, campos))
                datos.append(fila)
        return datos

    def verificar_registro(self, registro):
        observacion = ""
        
        # Verificación de consistencia
        if registro['sexo'] not in ['Masculino', 'Femenino']:
            observacion = "Género no válido."
        elif registro['grupo_etario'] == '' or not registro['grupo_etario'].isdigit():
            observacion = "Grupo etario no válido."
        elif registro['jurisdiccion_residencia'] == '':
            observacion = "Falta jurisdicción de residencia."
        elif registro['vacuna'] == '':
            observacion = "Falta tipo de vacuna."
        
        return observacion

    def guardar_registros_erroneos(self, registros):
        try:
            with open('registros_erroneos.csv', mode='w', newline='', encoding='utf-8') as f:
                fieldnames = registros[0].keys() if registros else []
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(registros)
        except Exception as e:
            print(f"Se produjo un error al guardar registros erróneos: {e}")