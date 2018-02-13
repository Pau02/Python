# coding utf8

dividiendo 	= input ('Escriba el Dividendo:')
divisor 	= input ('Escriba el Divisor:')
cociente 	= dividendo / divisor
resto 		= dividendo % divisor

if (resto == 0):
    print ("La División es Exacta. Cociente:" , cociente)
else:
    print ("La División no es Exacta. Cociente:" , cociente , "Resto:" , resto")
