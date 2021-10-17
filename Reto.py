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
