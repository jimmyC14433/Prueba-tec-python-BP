regla_nombre_mujeres="abcdefghijkl"
regla_nombre_hombres="nñopqrstuvwxyz"

nombre = str(input(print("Por favor ingrese su nombre")))
inicial_n = nombre[0]
#print (inicial_n)

sexo = str(input(print("Por favor ingrese su sexo (Masculino/Femenino)")))
inicial_s = sexo[0]
#print (inicial_s)

if  inicial_n in regla_nombre_mujeres and inicial_s=="f" or inicial_n in regla_nombre_hombres and inicial_s=="m":
    print(" - Usted pertenece al grupo A")
elif 1==1:
    print(" - Usted pertenece al grupo B")



