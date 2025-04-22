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

def formar_listafinal(px,cy): #devuelve los nombres de la lista según el porcentaje 
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

def bd(px,cy): #crea la bd
    lista_bd=formar_listafinal(px,cy) 
    base=open("basesnombres.txt","w")
    for i in lista_bd:
        for a in i:
            base.write(f"{a},")
        base.write("\n")
    base.close()
    return ""
def es():#entradas y salidas 
    px=int(input("Cantidad: "))
    py=int(input("Porcentaje: "))
    cy=int(px*(py/100))
    return bd(px,cy)

#Programa principal 
es()
