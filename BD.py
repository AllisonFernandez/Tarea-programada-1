import names
import random 
import re
def formar_nombre(px): #forma los nombres aleatorios de la bd
    lista=[]
    i=0
    while i<px:
        nombrelista=[]
        genero=random.choice(["male","female"])
        nombre=names.get_first_name(gender=genero)
        apellido1=names.get_last_name()
        apellido2=names.get_last_name()
        tupla=(nombre,apellido1,apellido2)
        nombrelista.append(tupla)
        if genero=="male":
            x=True
            nombrelista.append(x)
        else: 
            x=False
            nombrelista.append(x)
        lista.append(nombrelista)
        i+=1
    return lista
def lista_estudiantes():
    lista=[]
    estu=open("estudiantes.txt","r")
    for i in estu:
        cadena=re.split(",|\n",i) #,|\n significa , o salto de línea
        cadena.pop(-1)
        tupla=tuple(cadena[:3])
        cadena=[tupla]+cadena[3:]
        lista.append(cadena)
    estu.close()
    return lista
def correción_de_genero():
    lista=lista_estudiantes()
    for i in lista:
        if i[-1]=="Masculino":
           i[-1]=True 
        else:
            i[-1]=False
    return lista
def formar_listadenombres(px,cy): #devuelve los nombres de la lista según el porcentaje 
    lista_Final=[]
    x=formar_nombre(px)
    a=1
    while a<=cy:
        w=random.choice(correción_de_genero()) #de la función de lista estdudiantes escoge una cantidad aleatoria
        if w not in lista_Final:
            lista_Final.append(w)
            a+=1
    for i in x[:cy]:
        lista_Final.append(i)
    return lista_Final   
def codigossedes(): #forma los códigos correspondientes de las sedes
    codigos=[]
    textsedes=open("sedes.txt","r")
    for i, linea in enumerate(textsedes):
        codigo="0"+str(i+1)
        codigos.append(codigo)
    return codigos
def carne(pannoinicial,pannofinal,listaEstudiantes): #crear los carnets
    listaannos=[]
    listasedes=codigossedes()
    listacarnets=[]
    for a in range(pannoinicial,pannofinal+1):
        listaannos.append(a)
    for n in listaEstudiantes:
        numrandom=""
        for e in range(4):
            numrandom+=str(random.randint(1,9))
        anno=str(random.choice(listaannos))
        sede=random.choice(listasedes)
        carnet=anno+sede+numrandom
        if carnet not in listacarnets: 
            listacarnets.append(carnet)
    return listacarnets
def formarCorreo(carnets,listaEstudiantes):
    listacorreos=[]
    for i in range(len(carnets)): 
        estudiante=listaEstudiantes[i]
        carnet=carnets[i]
        nombrecompleto=estudiante[0]
        nombre=nombrecompleto[0]
        inicial=nombre[0].lower()
        apellido=nombrecompleto[1].lower()
        numero=carnet[6:]
        correo=inicial+apellido+numero+"@estudiantec.ac.cr"
        if correo not in listacorreos:
            listacorreos.append(correo)
    return listacorreos
def generarNotas(pw,pb,pa): #Falta agregar lo del redondeo
    lista=[]
    nota1=random.randint(0,100)
    nota2=random.randint(0,100)
    nota3=random.randint(0,100)
    promedio=(nota1*(pw/100))+(nota2*(pb/100))+(nota3*(pa/100))
    lista.append(nota1)
    lista.append(nota2)
    lista.append(nota3)
    lista.append(promedio)
    return tuple(lista)
def asignarNotas(pw,pb,pa,listaEstudiantes):
    listaNotas=[]
    for i in range(len(listaEstudiantes)):
        notas=generarNotas(pw,pb,pa)
        listaNotas.append(notas)
    return listaNotas
def formar_listaFinal(pannoInicial,pannoFinal,px,cy,pPorcentaje1,pPorcentaje2,pPorcentaje3): #va a formar la lista final con los correos y carnets
    listaEstudiantes=formar_listadenombres(px,cy)
    listaCarnets=carne(pannoInicial,pannoFinal,listaEstudiantes)
    listaCorreos=formarCorreo(listaCarnets,listaEstudiantes)
    listaNotas=asignarNotas(pPorcentaje1,pPorcentaje2,pPorcentaje3,listaEstudiantes)
    for i in range(len(listaEstudiantes)):
        listaEstudiantes[i].append(listaCarnets[i])
        listaEstudiantes[i].append(listaCorreos[i])
        listaEstudiantes[i].append(listaNotas[i])
    return listaEstudiantes
def bd(pannoInicial,pannoFinal,px,cy,pPorcentaje1,pPorcentaje2,pPorcentaje3): #crea la bd
    lista_bd=formar_listaFinal(pannoInicial,pannoFinal,px,cy,pPorcentaje1,pPorcentaje2,pPorcentaje3) ##---------------
    base=open("basesnombres.txt","w")
    for i in lista_bd:
        for a in i:
            if a==i[-1]:
                base.write(f"{a}")
            else:
                base.write(f"{a},")
        base.write("\n")
    base.close()
    return ""
def es():#entradas y salidas 
    px=int(input("Cantidad: "))
    py=int(input("Porcentaje: "))
    cy=int(px*(py/100))
    a=True
    while a==True:
        annoInicial=int(input("Digite el año inicial: "))
        annoFinal=int(input("Digite el año final: "))
        if annoInicial<=annoFinal:
            break
        print("El año incial debe ser menor o igual al año final.")
    while a==True:
        porcentaje1=int(input("Digite el primer porcentaje: "))
        porcentaje2=int(input("Digite el segundo porcentaje: "))
        porcentaje3=int(input("Digite el tecer porcentaje: "))
        if porcentaje1+porcentaje2+porcentaje3==100:
            break
        print("Los tres porcentajes deben sumar 100.")
    return bd(annoInicial,annoFinal,px,cy,porcentaje1,porcentaje2,porcentaje3)

#Programa principal 
es()