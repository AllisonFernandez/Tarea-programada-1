import names
import random 
def formar_nombre(px): #forma los nombres 
    lista=[]
    i=0
    while i<px:
        nombrelista=[]
        genero=random.choice(["male","female"])
        nombre=names.get_first_name(gender=genero)
        nombrelista.append(nombre)
        apellido1=names.get_last_name()
        nombrelista.append(apellido1)
        apellido2=names.get_last_name()
        nombrelista.append(apellido2)
        if genero=="male":
            x= "Masculino"
            nombrelista.append(x)
        else: 
            x="Femenino"
            nombrelista.append(x)
        lista.append(nombrelista)
        i+=1
    return lista

def es(): #devuelve los nombres de la lista según el porcentaje 
    px=int(input("Cantidad: "))
    py=int(input("Porcentaje: "))
    cy=int(px*(py/100))
    lista_Final=[]
    x=formar_nombre(px)
    for i in x[:cy]:
        lista_Final.append(i)
    return lista_Final   
def bd():
    lista_bd=es() 
    base=open("basepruebas.txt","a")
    for i in lista_bd:
        for a in i:
            base.write(f"{a},")
        base.write("\n")
    base.close()
    return "" 
