import pandas as pd
import ast

with open("basesnombres.txt", "r") as estadistica:
    lineas = estadistica.readlines()

datos = []
for linea in lineas:
    partes = linea.strip().split(",", 5)
    numeroCarnet = int(partes[4].strip())
    notas = ast.literal_eval(partes[5].strip())  # Extrae la tupla de notas
    notaFinal = notas[-1]  # Última nota es la nota final
    generacion = int(str(numeroCarnet)[:4])
    datos.append((numeroCarnet, notaFinal))

resumen = {}
for numeroCarnetarnet, notaFinal in datos:
    generacion = int(str(numeroCarnet)[:4])

    if generacion not in resumen:
        resumen[generacion] = {
            "Aprobados": 0,
            "Reposición": 0,
            "Reprobados": 0
        }

    if notaFinal >= 67.5:
        resumen[generacion]["Aprobados"] += 1
    elif 57.5 <= notaFinal < 67.5:
        resumen[generacion]["Reposición"] += 1
    else:
        resumen[generacion]["Reprobados"] += 1

df = pd.DataFrame.from_dict(resumen, orient='index')
df['Totales'] = df.sum(axis=1) #suma el valor de todas las comunas horizontalmente
df = df.sort_index() #ordena de menor a mayor

#df.loc['Totales'] = df.sum(numeric_only=True)
df.loc['Totales'] = df.sum()

# Guardar a Excel
df.to_excel("resumenGeneraciones.xlsx")
print("Archivo 'resumenGeneraciones.xlsx' generado con éxito.")













"""
import ast
from openpyxl import Workbook

# Leer datos del archivo
with open('basesnombres.txt', "r") as archivo:
    lineas= archivo.readlines()

# Procesar líneas y clasificar por generación
def procesarDatos(lineas):
    resumenPorGeneracion = {}
    for linea in lineas:
        try:
            partes = linea.strip().split(",", 4)
            numeroCarnet = int(partes[2].strip())
            notas = ast.literal_eval(partes[4])
            notaFinal = notas[-1]
            generacion = int(str(numeroCarnet)[:4])

            if notaFinal >= 67.5:
                resumenPorGeneracion[generacion]["aprobados"] += 1
            elif 57.5 <= notaFinal < 67.5:
                resumenPorGeneracion[generacion]["reposicion"] += 1
            else:
                resumenPorGeneracion[generacion]["reprobados"] += 1

        except Exception as error:
            print(f"Error procesando línea: {linea}")
            print(error)
    return resumenPorGeneracion

# Crear y guardar archivo Excel
def generarArchivoExcel(resumenPorGeneracion, ResumenPorGeneracion):
    libro = Workbook()
    hoja = libro.active
    hoja.title = "ResumenPorGeneracion"

    hoja.append(["Generacion", "Aprobados", "Reposicion", "Reprobados", "Totales"])

    totalAprobados = totalReposicion = totalReprobados = totalEstudiantes = 0

    for generacion in sorted(resumenPorGeneracion.keys()):
        datos = resumenPorGeneracion[generacion]
        total = datos["aprobados"] + datos["reposicion"] + datos["reprobados"]
        hoja.append([
            generacion,
            datos["aprobados"],
            datos["reposicion"],
            datos["reprobados"],
            total
        ])
        totalAprobados += datos["aprobados"]
        totalReposicion += datos["reposicion"]
        totalReprobados += datos["reprobados"]
        totalEstudiantes += total

    hoja.append(["Totales", totalAprobados, totalReposicion, totalReprobados, totalEstudiantes])
    libro.save(ResumenPorGeneracion)
    print(f"Archivo '{ResumenPorGeneracion}' generado correctamente.")

# Ejecución principal
resumen = procesarDatos(lineas)
generarArchivoExcel(resumen, "resumenGeneraciones.xlsx")
"""
