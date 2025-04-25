import random
def codigossedes():
    codigos=[]
    textsedes=open("sedes.txt","r")
    for i, linea in enumerate(textsedes):
        codigo="0"+str(i+1)
        codigos.append(codigo)
    return codigos

def carne(pannoinicial,pannofinal):
    listaannos=[]
    listasedes=codigossedes()
    numrandom=""
    for a in range(pannoinicial,pannofinal):
        listaannos.append(a)
    for e in range(4):
        numrandom+=str(random.randint(1,9))
    anno=str(random.choice(listaannos))
    sede=random.choice(listasedes)
    carnet=anno+sede+numrandom
    return carnet
    
def es():
    a=True
    while a==True:
        annoInicial=int(input("Digite el año inicial: "))
        annoFinal=int(input("Digite el año final: "))
        if annoInicial<=annoFinal:
            break
        print("El año incial debe ser menor o igual al año final.")
    print(carne(annoInicial,annoFinal))
    return ""

print(es())