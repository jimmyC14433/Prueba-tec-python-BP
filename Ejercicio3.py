import json

while True:
  operación = int(input ('''Seleccione la operación que decea realizar:
  1 - Para consultar inmuebles
  2 - Para registrar nuevo inmueble
  3 - Para salir
  :'''))
 
  if operación == 1:
    
    def consultar_inmuebles(precio):
        with open("inmuebles.txt", "r") as f:
          datos = json.load(f)
        inmuebles_encontrados = []
        for inmueble in datos:
          if float(inmueble["precio"]) <= precio:
           inmuebles_encontrados.append(inmueble)
        return inmuebles_encontrados

  #Consultar inmueble
    precio_a_consultar = int(input("Ingrese el valor maximo del inmueble que desea ver: "))

    inmuebles_encontrados = consultar_inmuebles(precio_a_consultar)
    print("Inmuebles encontrados:")
    for inmueble in inmuebles_encontrados:
        print(inmueble)

  #Agregar inmueble
  elif operación == 2:
    def agregar_inmueble(nuevo_inmueble):
      with open("inmuebles.txt", "r") as f:
       datos = json.load(f)
       datos.append(nuevo_inmueble)
      with open("inmuebles.txt", "w") as f:
        json.dump(datos, f, indent=4)

    año = input("Ingrese el año: ")
    metros = input("Ingrese los metros: ")
    tipo = input("Ingrese el tipo: ")
    garage = input("Ingrese si tiene garage Si/No: ")
    zona = input("Ingrese la zona: ")
    precio = input("Ingrese el precio: ")

    nuevo_inmueble = {
    "año": año,
    "metros": metros,
    "tipo": tipo,
    "garage": garage,
    "zona": zona,
    "precio": precio
    }

    agregar_inmueble(nuevo_inmueble)
    print("Nuevo inmueble agregado al archivo.")

  elif operación == 3:
    print("Gracias por utilizar nuestro sistema")
    break
    
  else:
    print ("Opcion seleccionada es invalida")




