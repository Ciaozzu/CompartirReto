import os
print(os.getcwd())

def regV(nombreArch, crv): #Registra nuestras ventas
    with open(nombreArch + ".txt", "a") as textoVentas:
        textoVentas.write(crv)
    
def creadorRegV(): #Hace el string necesario regV
    registro = "hola"
    return registro

    #regV()
regV("ventas", creadorRegV())    
#def regVE(): #Agrega la venta realizada del empleado al registro
def regV(): #
    with open("EmpleadosLista.txt","r") as myFile:
        dataString = myFile.readlines()
        
    dataNoBS = [] #
    for person in dataString:
        noBS = person.rstrip()
        dataNoBS.append(noBS.split(","))
        
    finalData = [] #
    for person in dataNoBS:
        name = person[0]
        num = int(person[1])
        finalData.append([name,num])
        
    return finalData

def updateEmpleadosLista(name,role): #
    index = 0
    for register in role:
        if name in register:
            role[index] [1] += 1
        index += 1

    return role
data = regV()

#def regLA(): #Registra la llegada de artículos
    
    
#def agreI(): #Agrega el artículo registrado al inventario

#def consultI(): #Consulta los datos del  inventario
          
#def consultV #Consulta los datos de las ventas


#def reporteVA():
  #print("Mostrar reporte de ventas por:  1. Por vendedor 2. Por articulo")
  #resp = input("")
  #if resp == 1
      #juan Karla Sam Margaret Jose Henry
  #elif resp == 2
      #Articulo
          
#def prodPA(): #Te despliega los productos que estan por agotarse
    

#def menu():
    
    #regV("ventas", creadorRegV())
