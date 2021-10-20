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

def mostrEmpl(finalData): #Esta sección fue hecha por Valería
    """Esta función muestra los
        empleados que hay"""
    print("A continuación se muestran todos los empleados: ")
    for elemento in finalData:
        nombre = elemento[0]
        print("- " + nombre)
        
def mostrEmpl2(finalData): #Esta sección fue hecha por Ángel
    """Crea una lista unicamente
        con los empleados"""
    listaUE = []
    for elemento in finalData:
        nombre = elemento[0]
        listaUE.append(nombre)   
    return listaUE


def updateEmpleadosLista(name,venta): #Esta sección fue hecha por Valeria
    """Crea la lista nueva con
        nuestras ventas actualizadas"""
    index = 0
    for register in venta:
        if name in register:
            venta[index] [1] += 1
        index += 1
    return venta

data = regV() #Esta variable la creamos para facilitar el uso del retorno que da regV()
listaUCE = mostrEmpl2(data) #variable que utilizamos en menu para hacer el ciclo while del n° 1 posible

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
        producto = int(input("Introduce el número del producto vendido: "))
        cantiProd = int(input("Ingresa la cantidad que fue vendida de este mismo producto: "))
        geneLRB(fecha, empleado, producto, cantiProd)
        listaIM = crearLBI()
        geneAI(crearLIA(actualizarLBI(producto,listaIM,cantiProd)))
        genlisRegVen(fecha, empleado, producto, cantiProd)
        resp = int(input("Se vendieron más artículos 1. Sí 2. No: "))
        
def geneLRB(fech, emplead, product, cantPro):
    """Genera el archivo llamado
        registroVentas"""
    listaF = []
    linea1 = "\nRegistro de venta:\n"
    linea2 = f"Fecha de ventas: {fech}\n"
    linea3 = f"Empleado: {emplead}\n"
    if product == 0:
        pro = "Disney Cruella De Vil Diamond Funko Pop Exclusivo"
    elif product == 1:
        pro = "Funko Pop Board Games Silver Mr. Monopoly - Figura de vinilo"
    elif product == 2:
        pro = "Funko Pop Daenerys Targaryen 59 Game of Thrones"
    elif product == 3:
        pro = "Funko Pop Flocked Iceman 504 Marvel 80 Years"
    elif product == 4:
        pro = "Funko Pop Glowing Mr Burns 1162 The Simpsons"
    elif product == 5:
        pro = "Funko Pop Grogu Con Galleta 464 Star Wars The Mandalorian"
    elif product == 6:
        pro = "Funko Pop Keychain Pogo The Umbrella Academy"
    elif product == 7:
        pro = "Funko Pop Keychain The Flash DC The Flash"
    elif product == 8:
        pro = "Funko Pop Marvel: Avengers - Wanda Maximoff Exclusivo Disney Collector Zone"
    elif product == 9:
        pro = "Funko Pop Venom 888 Marvel Venom"
    elif product == 10:
        pro = "Llavero Funko Pop Zoey Fortnite"
    elif product == 11:
        pro = "Lucky The Leprechaun Edición Limitada"
    linea4 = f"Producto vendido(s): {pro}\n"
    linea5 = f"Cantidad: {cantPro}\n"
    listaF.append(linea1)
    listaF.append(linea2)
    listaF.append(linea3)
    listaF.append(linea4)
    listaF.append(linea5)
    with open("registroVentas.txt", "a") as regVen:
        regVen.writelines(listaF)
        
def genlisRegVen(fechaa, emplead, produc, cantiProdu):
    if produc == 0:
        pro = "Disney Cruella De Vil Diamond Funko Pop Exclusivo"
    elif produc == 1:
        pro = "Funko Pop Board Games Silver Mr. Monopoly - Figura de vinilo"
    elif produc == 2:
        pro = "Funko Pop Daenerys Targaryen 59 Game of Thrones"
    elif produc == 3:
        pro = "Funko Pop Flocked Iceman 504 Marvel 80 Years"
    elif produc == 4:
        pro = "Funko Pop Glowing Mr Burns 1162 The Simpsons"
    elif produc == 5:
        pro = "Funko Pop Grogu Con Galleta 464 Star Wars The Mandalorian"
    elif produc == 6:
        pro = "Funko Pop Keychain Pogo The Umbrella Academy"
    elif produc == 7:
        pro = "Funko Pop Keychain The Flash DC The Flash"
    elif produc == 8:
        pro = "Funko Pop Marvel: Avengers - Wanda Maximoff Exclusivo Disney Collector Zone"
    elif produc == 9:
        pro = "Funko Pop Venom 888 Marvel Venom"
    elif produc == 10:
        pro = "Llavero Funko Pop Zoey Fortnite"
    elif produc == 11:
        pro = "Lucky The Leprechaun Edición Limitada"
    linea1 = f"{fechaa},{emplead},{pro},{cantiProdu}"
    with open("listaRegVen.txt", "a") as listaRegVenta:
         listaRegVenta.write(linea1)
    
 
######################################################################
#######################"""2222222222222222"""######################### 
######################################################################

def regLA(): # Esta sección fue hecha por Ángel
    """registro de llegada de articulos al almacen"""
    print("A continuación se muestra la lista de productos en el inventario: ")
    creaLprod(creaLI("Inventario"))
    resp = 1
    while resp == 1:
        fecha = input("Fecha de llegada del articulo(dd/mm/aa): ")
        producto = int(input("Introduce el número del producto reabastecido: "))
        cantiProd = int(input("Ingresa la cantidad que fue reabastecida: "))        
        geneRegLleg(fecha, producto, cantiProd)
        listaaIM = crearLBI()
        geneALlegA(crearLIA(actualizarLInv(producto, listaaIM, cantiProd)))
        resp = int(input("Llegaron más artículos 1. Sí 2. No: "))
        if resp == "2":
            menu(listaUCE)
        
def geneRegLleg(fech, product, cantProd):
    """Genera el archivo registroLA"""
    listaF = []
    linea1 = "Registro de llegada de articulo:\n"
    linea2 = f"Fecha de recepecion: {fech}\n"
    if product == 0:
        pro = "Disney Cruella De Vil Diamond Funko Pop Exclusivo"
    elif product == 1:
        pro = "Funko Pop Board Games Silver Mr. Monopoly - Figura de vinilo"
    elif product == 2:
        pro = "Funko Pop Daenerys Targaryen 59 Game of Thrones"
    elif product == 3:
        pro = "Funko Pop Flocked Iceman 504 Marvel 80 Years"
    elif product == 4:
        pro = "Funko Pop Glowing Mr Burns 1162 The Simpsons"
    elif product == 5:
        pro = "Funko Pop Grogu Con Galleta 464 Star Wars The Mandalorian"
    elif product == 6:
        pro = "Funko Pop Keychain Pogo The Umbrella Academy"
    elif product == 7:
        pro = "Funko Pop Keychain The Flash DC The Flash"
    elif product == 8:
        pro = "Funko Pop Marvel: Avengers - Wanda Maximoff Exclusivo Disney Collector Zone"
    elif product == 9:
        pro = "Funko Pop Venom 888 Marvel Venom"
    elif product == 10:
        pro = "Llavero Funko Pop Zoey Fortnite"
    elif product == 11:
        pro = "Lucky The Leprechaun Edición Limitada"
    linea3 = f"Nombre del articulo: {pro}\n"
    linea4 = f"Cantidad: {cantProd}\n"
    listaF.append(linea1)
    listaF.append(linea2)
    listaF.append(linea3)
    listaF.append(linea4)
    with open("registroLA.txt","a") as regProdAlmacen:
        regProdAlmacen.writelines(listaF)
    
    
######################################################################
######################"""333333333333333333"""########################
######################################################################
def consultI(listaI): # Esta sección fue hecha por Ángel
    """Despliega en pantalla el inventario"""
    for fila in listaI:
        print("\n")
        for elemento in fila:
            print(elemento + "\t",end = "")

def creaLprod(ListaProd):
    """Crea una lista de los productos
        existentes en el inventario"""
    cont = 0
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

def crearLIA(listPAI): # Esta sección fue hecha por Ángel
    """crea la lista fea actualizada
        del inventario """
    listaIA = [] #Lista fea del inventario actualizado
    for elemento in listPAI: #listaPAI = lista bonita para actualizar el inventario
        listaNue = elemento[0] + ","
        listaNue += elemento[1] + ","
        listaNue += str(elemento[2]) + ","
        listaNue += elemento[3] + "\n"
        listaIA.append(listaNue)
    return listaIA
    

def crearLBI(): # Esta sección fue hecha por Ángel
    """Crea la lista bonita
        con datos manipulables del inventario """
    with open("Inventario.txt","r") as myFile:
        dataString = myFile.readlines()
    
    dataNoBS = [] 
    for elem in dataString:
        noBS = elem.rstrip()
        dataNoBS.append(noBS.split(","))
        
    listaFinall = [] 
    for elementos in dataNoBS:
        productt = elementos[0]
        precio = elementos[1]
        cantidad = int(elementos[2])
        categoria = elementos[3]
        listaFinall.append([productt,precio,cantidad,categoria])
    return listaFinall


def actualizarLBI(produ,datInv,cant): # Esta sección fue hecha por Valeria
    """Crea la lista nueva con
        #nuestras ventas actualizadas""" 
    datInv[produ][2] -= cant
    return datInv

def actualizarLInv(produ,datInv,cant): # Esta sección fue hecha por Valeria
    """Crea lista BONITA nueva con nuestro inventario actualizado""" 
    datInv[produ][2] += cant
    return datInv

def geneAI(listaIA): #Esta sección fue hecha por Ángel
    with open("Inventario.txt", "w") as InventarioAc:
        InventarioAc.writelines(listaIA)
        
def geneALlegA(listaIA): #Esta sección fue hecha por Ángel
    with open("Inventario.txt", "w") as InventarioAc:
        InventarioAc.writelines(listaIA)
        
######################################################################
#####################"""444444444444444444444"""######################
######################################################################

def consultVen(dataNoBs):
    """Despliega el registro de ventas"""
    for fila in dataNoBs:
        for elemento in fila:
            print(elemento + "\t")
            
def consultAVen(): #Consulta los datos de las ventas
    """Crea una lista MEDIO BONITA del archivo registroVentas""" 
    with open("registroVentas.txt", "r") as regVentas:
        dataString = regVentas.readlines()
    
    dataNoBS = [] 
    for person in dataString:
        noBS = person.rstrip()
        dataNoBS.append(noBS.split(","))
        
    return dataNoBS

######################################################################
####################"""555555555555555555555"""#######################
######################################################################

#def reporteVA():
    #print("Mostrar reporte de ventas por:  1. Por vendedor 2. Por articulo")
    #resp = input("respuesta: ")
    #if resp == 1:
    
    #elif resp == 2:
    

#def crearLisRegV(): #Consulta los datos de las ventas
 #   """Crea una lista MEDIO BONITA del archivo registroVentas""" 
  #  with open("LOTENGOQUECAMBIAR.txt", "r") as regVentas:
   #     dataString = regVentas.readlines()
    
   # dataNoBS = [] 
    #for person in dataString:
        #noBS = person.rstrip()
     #   dataNoBS.append(noBS.split(","))
        
   # return dataNoBS


######################################################################
###################"""77777777777777777777777777"""###################
######################################################################
        
def menu(nomError): #Esta sección fue hecha por Ángel Márquez
    print("\nMenu:\n1. Registrar ventas\n2. Registrar llegada de artículos al almacen\n3. Consultar datos del inventario\n4. Consultar datos de las ventas\n5. Mostrar reportes de ventas por vendedor o por artículo\n6. Salir\n")
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
        respu = int(input("\n¿Desea 1. Regresar al menu 2. Salir ?\nSeleccione el número deseado: "))
        if respu == 1:
            menu(listaUCE)
        elif respu == 2:
            print("\n¡Hasta la proxima!")
          
    elif ans == 2:
        print("Llegada de artículos al almacen: ")
        regLA()
        print("\nEl registro fue hecho con exito")
        respu = int(input("\n¿Desea 1. Regresar al menu 2. Salir ?\nSeleccione el número deseado: "))
        if respu == 1:
            menu(listaUCE)
        elif respu == 2:
            print("\n¡Hasta la proxima!")
              
    elif ans == 3:
        print("Datos del inventario")
        print("Leer la lista desplegada en este orden: Nombre\tCosto(MXN)\tCantidad\tCategoría")
        consultI(creaLI("Inventario"))
        respu = int(input("\n¿Desea 1. Regresar al menu 2. Salir ?\nSeleccione el número deseado: "))
        if respu == 1:
            menu(listaUCE)
        elif respu == 2:
            print("\n¡Hasta la proxima!")
    elif ans == 4:
        print("Registro de ventas\n\n**Si no ve nada a continuacion significa que no hay registro alguno de ventas**\nSi desea hacer el registro de una venta en el n° 1 del menu puede hacerlo")
        consultVen(consultAVen())
        print("\n")
        respu = int(input("¿Desea 1. Regresar al menu 2. Salir ?\nSeleccione el número deseado: "))
        if respu == 1:
            menu(listaUCE)
        elif respu == 2:
            print("\n¡Hasta la proxima!")
            
    #elif ans == 5:
        
        
    elif ans == 6:
        resp = input("¿Esta seguro que desea salir del programa\n1. Si 2. No?")
        if resp == 1:
            print("\n¡Hasta la proxima!")
        if respu == 2:
            menu(listaUCE)    
        
######################################################################      
######################################################################
######################################################################
          
