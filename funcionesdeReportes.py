def reporteHtml():
    base=open("basesnombres.txt","r")
    lineas=base.readlines()
    reporte=open("reporte.html","w")
    reporte.write("<html>\n<head><title>Reporte de Detalle de Notas</title></head>\n<body>\n")
    reporte.write("<h1>Reporte de HTML</h1>")
    reporte.write('<table border="1">\n')
    reporte.write("<tr><th colspan='7'><strong>Detalle de notas</strong></th></tr>")
    reporte.write("<tr><th>Nombre<th>Apellidos</th><th>Género</th><th>Carné</th><th>Correo</th><th>Notas</th><th>Estado</th></tr>\n")
    contadorDeFilas=0
    contadorReprobados=0
    contadarAprobados=0
    contardorReposicion=0
    cantidadDeEstudiantes=len(lineas)
    for linea in lineas:
        datos=linea.strip("").split(",")
        nombre=datos[0]
        apellido1=datos[1]
        apellido2=datos[2].strip("()")
        apellidos=f"{apellido1}, {apellido2}"
        genero=datos[3]
        if genero=="True":
            genero="Masculino"
        else: 
            genero="Femenino"
        carnet=datos[4]
        correo=datos[5]
        notas=datos[-1].strip("() \n")#esto es para quitar el salto de linea y el parentesis
        promedio=float(notas)
        if promedio<60:
            estado="Reprobado"
            contadorReprobados+=1
        elif promedio<70:
            estado="Reposición"
            contardorReposicion+=1
        else:
            estado="Aprobado"
            contadarAprobados+=1
        if contadorDeFilas%2==0:
            reporte.write("<tr bgcolor=#aee3ff>\n")
        else:
            reporte.write("<tr>\n")
        reporte.write(f"<td>{nombre}</td>")
        reporte.write(f"<td>{apellidos}</td>")
        reporte.write(f"<td>{genero}</td>")
        reporte.write(f"<td>{carnet}</td>")
        reporte.write(f"<td>{correo}</td>")
        reporte.write(f"<td>{promedio}</td>")
        reporte.write(f"<td>{estado}</td>")
        reporte.write(f"</tr>\n")
        contadorDeFilas+=1
    reporte.write(f"</table>\n")
    reporte.write(f"<p>La base de datos posee {cantidadDeEstudiantes}(....), de los cuales hay: {contadarAprobados} aprobados para un {(contadarAprobados*100)/cantidadDeEstudiantes}, {contardorReposicion} a reposición para un {(contardorReposicion*100)/cantidadDeEstudiantes}, {contadorReprobados} para un {(contadorReprobados*100)/cantidadDeEstudiantes}.</p>")
    reporte.write(f"</body></html>")#esto cierra el html    
    reporte.close()
    base.close()
    return ""
reporteHtml()