
v1 = 135 #platano
v2 = 250 #manzana
v3 = 150 #pera
v4 = 200 #naranja
v5 = 350 #Uva

fruta = int(input(print('''Bienvenido, Que fruta decea comprar:
1. platano = 135
2. manzana = 250
3. pera = 150
4. naranza = 200
5. Uva = 350
Por favor ingrese el numero que correponde a la fruta a la fruta a comprar.''')))

kilos = int(input("Por favor ingrese el numero de kilos a comprar "))

if fruta==1:
    valor=(v1*kilos)
    print ("La compra es ", kilos, "kilo(s) de platano y cuesta: ",valor)
elif fruta==2:
    valor=v2*kilos
    print ("La compra es ", kilos, "kilo(s) de manzana y cuesta: ",valor)    
elif fruta==3:
    valor=v3*kilos
    print ("La compra es ", kilos, "kilo(s) de pera y cuesta: ",valor)    
elif fruta==4:
    valor=v4*kilos
    print ("La compra es ", kilos, "kilo(s) de naranja y cuesta: ",valor)  
elif fruta==5:
    valor=v5*kilos
    print ("La compra es ", kilos, "kilo(s) de Uva y cuesta: ",valor)  
else:
    print("La fruta seleccionada no es valida")