

print ("+++ 1 ++++")
datos = []
with open("listas/frases.txt") as fname:
	lineas = fname.readlines()
	for linea in lineas:
		datos.append(linea.strip('\n'))
print (datos[2])
print(len(datos))
print ("+++")