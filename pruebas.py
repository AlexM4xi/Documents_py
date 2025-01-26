'''
	this file be of test for algoritm
'''
import random

n = ''

for i in range(8):
	n += str(random.randint(0,9))

'''
	introducir cada numero de n en una lista,
	rrecorrer la misma y reemplazar el 3er
	digito sabiendo que las opciones son 3
	4, 5 y 6, si el 3er digito es 4 se reemplaza
	por un 5 o si es 5 el reemlazo es 6 o
	si es 6, el cambio es por un 4, imprimir
	en pantalla el numero completo antes y
	despues de reemplazarlo.

'''
n_list = []
for num in n:
	n_list.append(num)

for num in n_list: # recorremos la lista
	if num.index() == 3: # selecciona el indice
		if int(num) == 4: # si el num es 4
			# reemplazamos el num
			n_list[num.index()] = '5'
			n_list = n_list
		break



