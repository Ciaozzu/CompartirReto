import os
print(os.getcwd())
######################################################################
#######################"""111111111111111"""##########################
######################################################################
def regV(): # Esta sección fue hecha por Valería
    """ Crea la lista manipulable, necesaria
        para update EmpleadosVenta.txt """
    with open("EmpleadosVentas.txt","r") as myFile:
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

def mostrEmpl(finalData):
    """Esta función muestra los
        empleados que hay"""
    print("A continuación se muestran todos los empleados: ")
    for elemento in finalData:
        nombre = elemento[0]
        print("- " + nombre)
        
def mostrEmpl2(finalData):
    """Crea una lista unicamente
        con los empleados"""
    listaUE = []
    for elemento in finalData:
        nombre = elemento[0]
        listaUE.append(nombre)   
    return listaUE


def updateEmpleadosLista(name,venta): # Esta sección fue hecha por Valeria
    """Crea la lista nueva con
        nuestras ventas actualizadas"""
    index = 0
    for register in venta:
        if name in register:
            venta[index] [1] += 1
        index += 1
    return venta

data = regV()
listaUCE = mostrEmpl2(data)
def creaLE(venta): #Esta sección fue hecha por Ángel
    """Crea la lista necesaria
        para pasarla a texto"""
    listaPGA = [] # Esto genera la lista necesaria para pasarlo al archivo
    for elemento in venta:
        listaN = elemento[0] + ","
        listaN += str(elemento[1]) + "\n"
        listaPGA.append(listaN)
    return listaPGA

def geneA(nombreA,listaPGA): #Esta sección fue hecha por Ángel
    """Genera el archivo
        EmpleadosVentas.txt"""
    with open(nombreA + ".txt", "w") as archivo:
        archivo.writelines(listaPGA)
    
def regVE(empleado): # Esta sección fue hecha por Ángel
    """registro de ventas"""
    print("A continuación se muestra la lista de productos en el  inventario:\n")
    creaLprod(creaLI("Inventario"))
    resp = 1
    while resp == 1:
        fecha = input("\nFecha en la que se esta realizando el registro de la compra(dd/mm/aa): ")
        producto = int(input("Introduce el numero del producto vendido: "))
        cantiProd = int(input("Ingresa la cantidad que fue vendida de este mismo producto: "))
        geneLRB(fecha, empleado, producto, cantiProd)
        resp = int(input("Se vendieron más artículos 1. Sí 2. No: "))
        
def geneLRB(fech, emplead, product, cantPro):
    """Genera el archivo llamado
        registroVentas"""
    listaF = []
    linea1 = "\nRegistro de venta:\n"
    linea2 = f"Fecha de ventas: {fech}\n"
    linea3 = f"Empleado: {emplead}\n"
    linea4 = f"Producto vendido(s): {product}\n"
    linea5 = f"Costo: {cantPro}\n"
    listaF.append(linea1)
    listaF.append(linea2)
    listaF.append(linea3)
    listaF.append(linea4)
    listaF.append(linea5)
    with open("registroVentas.txt", "a") as regVen:
        regVen.writelines(listaF)
    
 
######################################################################
#######################"""2222222222222222"""#########################
######################################################################

#def regLA(): #Registra la llegada de artículos al almacen
    
    
######################################################################
######################"""333333333333333333"""########################
######################################################################
def consultI(listaI): # Esta sección fue hecha por Ángel
    """Consulta los datos del
        inventario"""
    for fila in listaI:
        print("\n")
        for elemento in fila:
            print(elemento + "\t",end = "")

def creaLprod(ListaProd):
    """Crea una lista de los productos
        existentes en el inventario"""
    cont = 1
    for elem in ListaProd:
        print(f"{cont}. " + elem[0])
        cont += 1
        
def creaLI(nombreAr): # Esta sección fue hecha por Ángel
    """crea la lista de puros strings del
        inventario"""
    with open(nombreAr + ".txt", "r") as inventario:
        info = inventario.readlines()
    listaB = [] #Aquí guardamos la lista buena que usaremos
    for ele in info:
        eleme = ele.rstrip()
        listaB.append(eleme.split(","))
    return listaB

#def crearLIN(product,cantidad): # Esta sección fue hecha por Ángel
    #"""Genera el nuevo archivo Inventario """
    #with open("Inventario.txt","a") as:

def crearLBI(): # Esta sección fue hecha por Ángel
    """Crea la lista bonita con datos manipulables """
    with open("Inventario.txt","r") as myFile:
        dataString = myFile.readlines()
    
    dataNoBS = [] 
    for elem in dataString:
        noBS = elem.rstrip()
        dataNoBS.append(noBS.split(","))
        
    listaFinal = [] 
    for elementos in dataNoBS:
        productt = elementos[0]
        precio = elementos[1]
        cantidad = int(elementos[2])
        categoria = elementos[3]
        listaFinal.append([productt,precio,cantidad,categoria])
    return listaFinal

dataInv = crearLBI() #Guardamos la lista bonita de inventario
#def actualizarLBI(produ,venta): # Esta sección fue hecha por Valeria
    #"""Crea la lista nueva con
        #nuestras ventas actualizadas"""
    #index = 0
    #for register in venta:
        #if name in register:
            #venta[index] [3] += 1
        #index += 1
    #return venta
######################################################################
#####################"""444444444444444444444"""######################
######################################################################

#def consultV #Consulta los datos de las ventas

######################################################################
####################"""555555555555555555555"""#######################
######################################################################

#def reporteVA():
    #print("Mostrar reporte de ventas por:  1. Por vendedor 2. Por articulo")
    #resp = input("respuesta: ")
    #if resp == 1
        #juan Karla Sam Margaret Jose Henry
    #elif resp == 2
        #Articulo



######################################################################
####################"""66666666666666666666666"""#####################
######################################################################

#def prodPA(): #Te despliega los productos que estan por agotarse

######################################################################
###################"""77777777777777777777777777###################
######################################################################
def menu(nomError): #Crea el Menu #Esta sección fue hecha por Ángel Márquez
    print("\nMenu:\n1. Registrar ventas\n2. Registrar llegada de artículos al almacen\n3. Consultar datos del inventario\n4. Consultar datos de las ventas\n5. Mostrar reportes de ventas por vendedor o por artículo\n")
    ans = int(input("Elige la opción que deseas seleccionar: "))
    if ans == 1:
        print("\nA continuación se le mostrara una lista de las personas empleadas:\n")
        mostrEmpl(data)
        nombr = input("\nEscriba el nombre de la persona que se le registrara una venta\n(Es importante que lo escriba tal cual esta escrito en la lista)\n: ")
        while nombr not in nomError:
            nombr = input("\nEscriba el nombre de la persona que se le registrara una venta\n(Es importante que lo escriba tal cual esta escrito en la lista)\n: ")
        geneA("EmpleadosVentas",creaLE(updateEmpleadosLista(nombr,data)))
        regVE(nombr)
        print("\nEl registro fue hecho con exito")
        respu = int(input("\n¿Desea 1. Permanecer en el programa 2. Salir ?\nSeleccione el numero deseado: "))
        if respu == 1:
            menu()
        elif respu == 2:
            print("\n¡Hasta la proxima!")
          
        
    #elif ans == 2:
        
    #elif ans == 3
        #consultI(creaLI("Inventario.csv"))
    #elif ans == 4
        
    #elif ans == 5
        
    #elif ans == 6
######################################################################      
######################################################################
######################################################################
          

