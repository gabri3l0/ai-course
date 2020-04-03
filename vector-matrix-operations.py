""" ia3.py
    Este trabajo mostrara como con numpy y por medio del index
    puedes hacer operaciones basicas

    Author: Gabriel Aldahir Lopez Soto
    Email: gabriel.lopez@gmail.com
    Institution: Universidad de Monterrey
    First created: Thu 16 Feb, 2020
"""
#Importa las librerias estandard
import numpy as np

def suma_vector(x,y, implementacion):
	"""
	Esta funcion es para la suma de dos vectores

	INPUTS
	:parametro 1: vector int8 
	:parametro 2: vector int8
	:parametro 3: atributo con string para saber que metodo de realizacion

	OUTPUTS
	:return: vector int8 con la suma de las vectores x+y

	"""
	tamano_x = len(x)
	tamano_y = len(y)

	if tamano_x==tamano_y:
		if implementacion in 'numpy':
			resultado = np.add(x,y)
		elif implementacion in 'index':
			resultado = list()
			for xi,yi in zip(x,y):
				resultado.append(xi+yi)
			resultado = np.asarray(resultado)
	return resultado

def resta_vector(x,y, implementacion):
	"""
	Esta funcion es para la resta de dos vectores

	INPUTS
	:parametro 1: vector int8 
	:parametro 2: vector int8
	:parametro 3: atributo con string para saber que metodo de realizacion

	OUTPUTS
	:return: vector int8 con la resta de las vectores x+y

	"""
	tamano_x = len(x)
	tamano_y = len(y)

	if tamano_x==tamano_y:
		if implementacion in 'numpy':
			resultado = np.subtract(x,y)
		elif implementacion in 'index':
			resultado = list()
			for xi,yi in zip(x,y):
				resultado.append(xi-yi)
			resultado = np.asarray(resultado)
	return resultado

def transpuesta_vector(x, implementacion):
	"""
	Esta funcion es para hacer la transpuesta de x 

	INPUTS
	:parametro 1: vector int8 
	:parametro 2: atributo con string para saber que metodo de realizacion

	OUTPUTS
	:return: vector int8 transpuesto

	"""

	if implementacion in 'numpy':
		resultado = np.transpose(x)
	elif implementacion in 'index':
		resultado = list()
		z=list()
		for xi in x:
			z.append(int(xi))
		resultado.append(z)
		resultado = np.asarray(resultado)
	return resultado

def transpuesta_multiplicado_vector(x,y,implementacion):
	"""
	Esta funcion es para multiplicacion de x^T * y, es decir, el producto punto

	INPUTS
	:parametro 1: vector int8 
	:parametro 2: vector int8
	:parametro 3: atributo con string para saber que metodo de realizacion

	OUTPUTS
	:return: escalar

	"""
	tamano_x = len(x)
	tamano_y = len(y)

	if tamano_x==tamano_y:
		if implementacion in 'numpy':
			x = np.transpose(x)
			resultado = np.dot(x, y)
		elif implementacion in 'index':
			resultado = list()
			z=list()
			for xi in x:
				z.append(int(xi))
			resultado.append(z)
			x = np.asarray(resultado)
			suma = 0
			for xi in range(len(x[0])):
				suma+=(x[0][xi]*y[xi])
			resultado = list()
			resultado.append(suma)
			resultado = np.asarray(resultado)
	return resultado

def const_vector(x,numero,implementacion):
	"""
	Esta funcion es para la multiplicacion de un vector por una constante

	INPUTS
	:parametro 1: vector int8 
	:parametro 2: constante
	:parametro 3: atributo con string para saber que metodo de realizacion

	OUTPUTS
	:return: vector int8 con la resta de las vectores x+y

	"""

	if implementacion in 'numpy':
		resultado = np.multiply(numero, x)
	elif implementacion in 'index':
		resultado = list()
		for xi,y1 in zip(x,x):
			resultado.append(xi*5)
		resultado = np.asarray(resultado)
	return resultado

def suma_matriz(x,y, implementacion):
	"""
	Esta funcion es para la suma de dos matrices

	INPUTS
	:parametro 1: matriz int8 
	:parametro 2: matriz int8
	:parametro 3: atributo con string para saber que metodo de realizacion

	OUTPUTS
	:return: matriz int8 con la suma de las vectores x+y

	"""
	tamano_x = len(x)
	tamano_y = len(y)

	if tamano_x==tamano_y:
		if implementacion in 'numpy':
			resultado = np.add(x,y)
		elif implementacion in 'index':
			resultado = list()
			for xi,yi in zip(x,y):
				resultado.append(xi+yi)
			resultado = np.asarray(resultado)
	return resultado

def resta_matriz(x,y, implementacion):
	"""
	Esta funcion es para la resta de dos matrices

	INPUTS
	:parametro 1: matriz int8 
	:parametro 2: matriz int8
	:parametro 3: atributo con string para saber que metodo de realizacion

	OUTPUTS
	:return: matriz int8 con la resta de las vectores x+y

	"""
	tamano_x = len(x)
	tamano_y = len(y)

	if tamano_x==tamano_y:
		if implementacion in 'numpy':
			resultado = np.subtract(x,y)
		elif implementacion in 'index':
			resultado = list()
			for xi,yi in zip(x,y):
				resultado.append(xi-yi)
			resultado = np.asarray(resultado)
	return resultado

def multiplicacion_matriz(x,y, implementacion):
	"""
	Esta funcion es para multiplicacion de dos matrices

	INPUTS
	:parametro 1: matriz int8 
	:parametro 2: matriz int8
	:parametro 3: atributo con string para saber que metodo de realizacion

	OUTPUTS
	:return: matriz int8 con la multiplicacion de las matrices x*y

	"""

	tamano_x = len(x)
	tamano_y = len(y)

	if tamano_x==tamano_y:
		if implementacion in 'numpy':
			resultado = np.multiply(x,y)
		elif implementacion in 'index':
			resultado = list()
			for xi,yi in zip(x,y):
				resultado.append(xi*yi)
			resultado = np.asarray(resultado)
	return resultado

def division_matriz(x,y, implementacion):
	"""
	Esta funcion es para la division de matrices

	INPUTS
	:parametro 1: matriz int8 
	:parametro 2: matriz int8
	:parametro 3: atributo con string para saber que metodo de realizacion

	OUTPUTS
	:return: matriz int8 con la division de las matrices x/y

	"""

	tamano_x = len(x)
	tamano_y = len(y)

	if tamano_x==tamano_y:
		if implementacion in 'numpy':
			resultado = np.divide(x,y)
		elif implementacion in 'index':
			resultado = list()
			for xi,yi in zip(x,y):
				resultado.append(xi/yi)
			resultado = np.asarray(resultado)
	return resultado

def transpuesta_matriz(x, implementacion):
	"""
	Esta funcion es para la transpuesta de la matriz x 

	INPUTS
	:parametro 1: matriz int8 
	:parametro 2: atributo con string para saber que metodo de realizacion

	OUTPUTS
	:return: matriz int8 con la transpuesta de la matriz x

	"""

	if implementacion in 'numpy':
		resultado = np.transpose(x)
	elif implementacion in 'index':
		resultado =list()
		cont = 0
		for c in range(len(x)):
			z =list()
			for xi,yi in zip(x,x):
				z.append(xi[c])
			resultado.append(z)
		resultado = np.asarray(resultado)
	return resultado

def const_matriz(x,numero,implementacion):
	"""
	Esta funcion es para multiplicacion de la matriz por una constante

	INPUTS
	:parametro 1: matriz int8 
	:parametro 2: matriz int8
	:parametro 3: atributo con string para saber que metodo de realizacion

	OUTPUTS
	:return: matriz int8 

	"""

	if implementacion in 'numpy':
		resultado = np.multiply(numero, x)
	elif implementacion in 'index':
		resultado = list()
		for xi,x1 in zip(x,x):
			resultado.append(xi*numero)
		resultado = np.asarray(resultado)
	return resultado



def main():
	"""
	Aqui se declaran las matrices, vectores a usar y se usan las funciones

	Datos de entrada:
	Nada

	Datos de salida:
	Nada
	"""

	# ---- Operaciones con vector ----

	x_vector = np.array([[1],[2],[3]], dtype=np.int8)
	y_vector = np.array([[4],[5],[6]], dtype=np.int8)

	#Operaciones con vector
	suma_np = suma_vector(x_vector,y_vector,implementacion='numpy')
	suma_index = suma_vector(x_vector,y_vector,implementacion='index')

	resta_np = resta_vector(x_vector,y_vector,implementacion='numpy')
	resta_index = resta_vector(x_vector,y_vector,implementacion='index')

	transpuesta_np = transpuesta_vector(x_vector,implementacion='numpy')
	transpuesta_index = transpuesta_vector(x_vector,implementacion='index')

	transpuesta_multiplicado_np = transpuesta_multiplicado_vector(x_vector,y_vector,implementacion='numpy')
	transpuesta_multiplicado_index = transpuesta_multiplicado_vector(x_vector,y_vector,implementacion='index')

	numero=5
	const_np = const_vector(y_vector,numero,implementacion='numpy')
	const_index = const_vector(y_vector,numero,implementacion='index')
	
	#Formato de impresion
	print("\n" + 28*"-")
	print ("Operaciones de Matrices: ") 
	print(28*"-")
	print("x :\n", x_vector)
	print("y :\n", y_vector)
	print("x+y:(numpy) \n", suma_np)
	print("x+y:(index) \n", suma_index)
	print("x-y:(numpy) \n", resta_np)
	print("x-y:(index) \n", resta_index)
	print("xT:(numpy) \n", transpuesta_np)
	print("xT:(index) \n", transpuesta_index)
	print("xT*y:(numpy) \n", transpuesta_multiplicado_np)
	print("xT*y:(index) \n", transpuesta_multiplicado_index)
	print("a*y:(numpy) \n", const_np)
	print("a*y:(index) \n", const_index)

	# ---- Fin de Operaciones con vector ----

	# ---- Operaciones con matriz ----

	x_matriz = np.array([[1,2,3],[4,5,6],[7,8,9]], dtype=np.int8)
	y_matriz = np.array([[10,11,12],[13,14,15],[16,17,18]], dtype=np.int8)

	#Operaciones con matriz
	suma_np = suma_matriz(x_matriz,y_matriz,implementacion='numpy')
	suma_index = suma_matriz(x_matriz,y_matriz,implementacion='index')

	resta_np = resta_matriz(x_matriz,y_matriz,implementacion='numpy')
	resta_index = resta_matriz(x_matriz,y_matriz,implementacion='index')

	multiplicacion_np = multiplicacion_matriz(x_matriz,y_matriz,implementacion='numpy')
	multiplicacion_index = multiplicacion_matriz(x_matriz,y_matriz,implementacion='index')

	division_np = division_matriz(x_matriz,y_matriz,implementacion='numpy')
	division_index = division_matriz(x_matriz,y_matriz,implementacion='index')

	numero=5
	const_np = const_matriz(x_matriz,numero,implementacion='numpy')
	const_index = const_matriz(x_matriz,numero,implementacion='index')

	transpuesta_np = transpuesta_matriz(x_matriz,implementacion='numpy')
	transpuesta_index = transpuesta_matriz(x_matriz,implementacion='index')
	
	#Formato de impresion
	print("\n" + 28*"-")
	print ("Operaciones de Matrices: ") 
	print(28*"-")
	print("X :\n", x_matriz)
	print("Y :\n", y_matriz)
	print("X+Y:(numpy) \n", suma_np)
	print("X+Y:(index) \n", suma_index)
	print("X-Y:(numpy) \n", resta_np)
	print("X-Y:(index) \n", resta_index)
	print("X*Y:(numpy) \n", multiplicacion_np)
	print("X*Y:(index) \n", multiplicacion_index)
	print("X/Y:(numpy) \n", division_np)
	print("X/Y:(index) \n", division_index)
	print("a*X:(numpy) \n", const_np)
	print("a*X:(index) \n", const_index)
	print("xT:(numpy) \n", transpuesta_np)
	print("xT:(index) \n", transpuesta_index)


	# ---- Fin de Operaciones con vector ----


	return None

# Se llama al programa principal
main()

#Doy mi palabra que he realizado este trabajo con Integridad Academica