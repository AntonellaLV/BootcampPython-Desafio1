from src.cargar_datos import CargarDatos
from src.estadisticas import Estadisticas
from src.guardar_resultados import guardar_estadisticas_en_csv

def main():
    # Cargar datos
    data_loader = CargarDatos()
    try:
        datos = data_loader.cargar_datos('datos_nomivac_parte1.csv')
    except FileNotFoundError:
        print("Error: El archivo 'datos_nomivac_parte1.csv' no fue encontrado.")
        return
    except Exception as e:
        print(f"Error al cargar datos: {e}")
        return

    # Verificar si se cargaron los datos
    if not datos:
        print("No se cargaron datos. Verifica el contenido del archivo CSV.")
        return

    # Generar estadísticas
    statistics_generator = Estadisticas()
    try:
        estadisticas = statistics_generator.generar_estadisticas(datos)
    except Exception as e:
        print(f"Error al generar estadísticas: {e}")
        return

    # Mostrar resultados
    print("\n--- Estadísticas Generadas ---")
    
    print("\nDistribución por Género:")
    for genero, cantidad in estadisticas['Distribucion por Genero'].items():
        print(f"{genero}: {cantidad}")

    print("\nVacunas Aplicadas por Tipo:")
    total_vacunas = sum(estadisticas['Vacunas Aplicadas por Tipo'].values())
    for vacuna, cantidad in estadisticas['Vacunas Aplicadas por Tipo'].items():
        porcentaje = (cantidad / total_vacunas) * 100
        print(f"{vacuna}: {porcentaje:.2f}% ({cantidad} dosis)")

    print("\nDosis por Jurisdicción de Residencia:")
    for jurisdiccion, cantidad in estadisticas['Dosis por Jurisdiccion de Residencia'].items():
        print(f"{jurisdiccion}: {cantidad} dosis")

    print("\nSegunda Dosis por Jurisdicción:")
    for jurisdiccion, cantidad in estadisticas['Segunda Dosis por Jurisdiccion'].items():
        print(f"{jurisdiccion}: {cantidad} dosis")

    print("\nDosis de Refuerzo para Mayores de 60:")
    print(estadisticas['Dosis de Refuerzo para Mayores de 60'])

    print("\nDosis por Condición de Aplicación:")
    for condicion, cantidad in estadisticas['Dosis por Condición de Aplicación'].items():
        print(f"{condicion}: {cantidad} dosis")

    print("\nVacunas Administradas por Fecha:")
    for fecha, cantidad in estadisticas['Vacunas Administradas por Fecha'].items():
        print(f"{fecha}: {cantidad} dosis")

    # Guardar estadísticas en un archivo CSV
    try:
        guardar_estadisticas_en_csv(estadisticas, 'estadisticas.csv')
        print("\nLas estadísticas se guardaron exitosamente en 'estadisticas.csv'.")
    except Exception as e:
        print(f"Error al guardar estadísticas en CSV: {e}")

if __name__ == '__main__':
    main()
