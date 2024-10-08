# Clase de estadísticas adaptada para streaming
class Estadisticas:
    def generar_estadisticas(self, datos_stream):
        estadisticas = {
            'Distribucion por Genero': {},
            'Vacunas Aplicadas por Tipo': {},
            'Dosis por Jurisdiccion de Residencia': {},
            'Segunda Dosis por Jurisdiccion': {},
            'Dosis de Refuerzo para Mayores de 60': 0,
            'Dosis por Grupo Etario': {},
            'Dosis por Condición de Aplicación': {},
            'Vacunas Administradas por Fecha': {},
        }

        for fila in datos_stream:
            # Procesar estadísticas usando el generador en lugar de listas completas
            sexo = fila['sexo']
            estadisticas['Distribucion por Genero'][sexo] = estadisticas['Distribucion por Genero'].get(sexo, 0) + 1
            
            vacuna = fila['vacuna']
            estadisticas['Vacunas Aplicadas por Tipo'][vacuna] = estadisticas['Vacunas Aplicadas por Tipo'].get(vacuna, 0) + 1
            
            jurisdiccion = fila['jurisdiccion_residencia']
            estadisticas['Dosis por Jurisdiccion de Residencia'][jurisdiccion] = estadisticas['Dosis por Jurisdiccion de Residencia'].get(jurisdiccion, 0) + 1
            
            if fila.get('orden_dosis') == '2':
                estadisticas['Segunda Dosis por Jurisdiccion'][jurisdiccion] = estadisticas['Segunda Dosis por Jurisdiccion'].get(jurisdiccion, 0) + 1
            
            try:
                edad = int(fila['grupo_etario'])
                if edad >= 60:
                    estadisticas['Dosis de Refuerzo para Mayores de 60'] += 1
                    
                # NUEVAS ESTADÍSTICAS
                grupo_etario = self.obtener_grupo_etario(edad)
                estadisticas['Dosis por Grupo Etario'][grupo_etario] = estadisticas['Dosis por Grupo Etario'].get(grupo_etario, 0) + 1
                
            except ValueError:
                pass  # Ignorar el error de edad no válida

            condicion_aplicacion = fila['condicion_aplicacion']
            estadisticas['Dosis por Condición de Aplicación'][condicion_aplicacion] = estadisticas['Dosis por Condición de Aplicación'].get(condicion_aplicacion, 0) + 1
            
            fecha_aplicacion = fila['fecha_aplicacion']
            estadisticas['Vacunas Administradas por Fecha'][fecha_aplicacion] = estadisticas['Vacunas Administradas por Fecha'].get(fecha_aplicacion, 0) + 1

        total_vacunas = sum(estadisticas['Vacunas Aplicadas por Tipo'].values())
        if total_vacunas > 0:
            for vacuna in estadisticas['Vacunas Aplicadas por Tipo']:
                cantidad = estadisticas['Vacunas Aplicadas por Tipo'][vacuna]
                porcentaje = (cantidad / total_vacunas) * 100  # Calcula el porcentaje como un número
                estadisticas['Vacunas Aplicadas por Tipo'][vacuna] = porcentaje  # Almacenar como número

        return estadisticas
    
    def obtener_grupo_etario(self, edad):
        # Definición de los grupos etarios
        if edad < 18:
            return 'Menores de 18'
        elif 18 <= edad < 30:
            return '18-29'
        elif 30 <= edad < 60:
            return '30-59'
        else:
            return '60 y más'
