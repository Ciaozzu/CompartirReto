import os
print(os.getcwd())
# Resgistrar inventario
# Resgistrar inventario
# Resgistrar inventario
def regV(): # Esta sección fue hecha por Valería
    """ Hace el string necesario
        para updateEmpleadosLista """
    with open("EmpleadosLista.txt","r") as myFile:
        dataString = myFile.readlines()
        
        
    dataNoBS = [] 
    for person in dataString:
        noBS = person.rstrip()
        dataNoBS.append(noBS.split(","))
         
    finalData = [] 
    for person in dataNoBS:
        name = person[0]
        num = int(person[1])
        finalData.append([name,num])
        
    return finalData

def updateEmpleadosLista(name,venta): # Esta sección fue hecha por Valeria
    """Crea la lista nueva con
        nuestras ventas actualizadas"""
    index = 0
    for register in venta:
        if name in register:
            venta[index] [1] += 1
        index += 1
    return venta
data = regV() #Este valor se debe de asignar en "venta"  en la funcion de arribita

def creaLE(venta): #Esta sección fue hecha por Ángel
    """Crea la lista necesaria
        para pasarla a csv"""
    listaNB = []
    for elemento in venta:
        listaN = elemento[0] + ","
        listaN += str(elemento[1]) + "\n"
        print(listaN)
        listaNB.append(listaN)
    return listaNB

def

def geneA(nombreA,listaNB): #Esta sección fue hecha por Ángel
    """Genera el archivo
        EmpleadosLista.txt"""
    with open(nombreA + ".txt", "w") as archivo:
        archivo.write(listaNB) 
# Resgistrar inventario
# Resgistrar inventario
# Resgistrar inventario

#def regVE(): #Agrega la venta realizada del empleado al registro

#def regLA(): #Registra la llegada de artículos al almacen

    
    
#def agreI(): #Agrega el artículo registrado al inventario


def consultI(listaI): #Consulta los datos del  inventario
    for fila in listaI:
        print("\n")
        for elemento in fila:
            print(elemento + "\t",end = "")
        
def creaLI(nombreAr): #Crea una lista
    with open(nombreAr + ".txt", "r") as inventario:
        info = inventario.readlines()
    listaB = [] #Aquí guardamos la lista buena que usaremos
    for ele in info:
        eleme = ele.rstrip()
        listaB.append(eleme.split(","))
    return listaB

    

          
#def consultV #Consulta los datos de las ventas


#def reporteVA():
  #print("Mostrar reporte de ventas por:  1. Por vendedor 2. Por articulo")
  #resp = input("respuesta: ")
  #if resp == 1
      #juan Karla Sam Margaret Jose Henry
  #elif resp == 2
      #Articulo
          
#def prodPA(): #Te despliega los productos que estan por agotarse
    

def menu(): #Crea el Menu #Esta sección fue hecha por Ángel Márquez
    print("Menu:\n1. Registrar ventas\n2. Registrar llegada de artículos al almacen\n3. Consultar datos del inventario\n4. Consultar datos de las ventas\n5. Mostrar reportes de ventas por vendedor o por artículo\n")
    ans = input("\nElige la opción que deseas seleccionar")
    if ans == 1
        print()
        input()
    elif ans == 2
        
    elif ans == 3
        consultI(creaLI("Inventario.csv"))
    elif ans == 4
        
    elif ans == 5
        
    elif ans == 6
        
    
    regV("ventas", creadorRegV())
    
