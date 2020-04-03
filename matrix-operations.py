""" ia2.py
    Este trabajo mostrara como con numpy puedes sumar, 
    restar, hacer traspuesta, multiplicar y sacar la 
    longitud de matrices por medio de numpy

    Author: Gabriel Aldahir Lopez Soto
    Email: gabriel.lopez@gmail.com
    Institution: Universidad de Monterrey
    First created: Thu 07 Feb, 2020
"""
#Importa las librerias estandard
import numpy as np

def suma_matrices(x,y):
	"""
	Esta funcion es para la suma de dos matrices

	INPUTS
	:parametro 1: matriz int8 
	:parametro 2: matriz int8

	OUTPUTS
	:return: matriz int8 con la suma de las matrices x+y

	"""
	resultado = np.add(x,y)
	return resultado

def resta_matrices(x,y):
	"""
	Esta funcion es para la resta de dos matrices

	INPUTS
	:parametro 1: matriz int8 
	:parametro 2: matriz int8

	OUTPUTS
	:return: matriz int8 con la resta de las matrices x-y

	"""
	resultado = np.subtract(x, y)
	return resultado

def multiplicacion_matrices(x,y):
	"""
	Esta funcion es para la multiplicacion de dos matrices

	INPUTS
	:parametro 1: matriz int8 
	:parametro 2: matriz int8

	OUTPUTS
	:return: matriz int8 con la multiplicacion de las matrices x*y

	"""
	resultado = np.multiply(x, y)
	return resultado

def multiplicacion_matrices2(y,x):
	"""
	Esta funcion es para la multiplicacion de dos matrices

	INPUTS
	:parametro 1: matriz int8 
	:parametro 2: matriz int8

	OUTPUTS
	:return: matriz int8 con la multiplicacion de las matrices y*x

	"""
	resultado = np.multiply(y, x)
	return resultado

def multiplicacion_matrices3(numero,x):
	"""
	Esta funcion es para la multiplicacion de una matriz por una constante

	INPUTS
	:parametro 1: numero constante
	:parametro 2: matriz int8

	OUTPUTS
	:return: matriz int8 

	"""
	resultado = np.multiply(numero, x)
	return resultado

def inversa_matriz(x):
	"""
	Esta funcion es para inversa de una matriz

	INPUTS
	:parametro 1: matriz int8 
	:parametro 2: matriz int8

	OUTPUTS
	:return: matriz int8 inversa

	"""
	resultado = np.linalg.inv(x)
	return resultado

def division_matrices(x,y):
	"""
	Esta funcion es para la division de dos matrices

	INPUTS
	:parametro 1: matriz int8 
	:parametro 2: matriz int8

	OUTPUTS
	:return: matriz int8 con la division de las matrices x/y

	"""
	resultado = np.divide(x, y)
	return resultado

def division_matrices2(y,x):
	"""
	Esta funcion es para la division de dos matrices

	INPUTS
	:parametro 1: matriz int8 
	:parametro 2: matriz int8

	OUTPUTS
	:return: matriz int8 con la division de las matrices y/x

	"""
	resultado = np.divide(y,x)
	return resultado

def traspuesta_matrices(x):
	"""
	Esta funcion es para la traspuesta de x

	INPUTS
	:parametro 1: matriz int8

	OUTPUTS
	:return: matriz int8 traspuesta de x

	"""
	resultado = x.T
	return resultado

def zeros_matriz(x):
	"""
	Esta funcion es para crear una matriz llena de 0

	INPUTS
	:parametro 1: matriz int8

	OUTPUTS
	:return: matriz int8 

	"""
	resultado = np.zeros(shape=x.shape)
	return resultado

def identity_matriz(x):
	"""
	Esta funcion es crear la identidad de una matriz

	INPUTS
	:parametro 1: matriz int8

	OUTPUTS
	:return: matriz int8 

	"""
	resultado = np.identity(x.ndim+1)
	return resultado


def main():
	"""
	Aqui se declaran las matrices a usar y se usan las funciones

	Datos de entrada:
	Nada

	Datos de salida:
	Nada
	"""
	# Inicialización de dos matrices de 1 dimensión

	x = np.array([[1,2,3],[4,5,6],[7,8,9]], dtype=np.int8)
	y = np.array([[10,11,12],[13,14,15],[16,17,18]], dtype=np.int8)

	#Operaciones con matriz
	suma = suma_matrices(x,y)
	resta = resta_matrices(x,y)
	multiplicacion = multiplicacion_matrices(x,y)
	multiplicacion2 = multiplicacion_matrices2(y,x)
	exponente = inversa_matriz(x)
	division = division_matrices(x,y)
	division2 = division_matrices2(y,x)
	multiplicacion3 = multiplicacion_matrices3(5,x)
	traspuesta = traspuesta_matrices(x)
	zeros = zeros_matriz(x)
	identity = identity_matriz(x)

	#Formato de impresion
	print("\n" + 28*"-")
	print ("Operaciones de Matrices: ") 
	print(28*"-")
	print("x :\n", x)
	print("y :\n", y)
	print ("x + y :\n" , suma)
	print ("x - y :\n" , resta)
	print ("x * y :\n" , multiplicacion)
	print ("y * x :\n" , multiplicacion2)
	print ("x^-1 :\n" , exponente)
	print ("x / y :\n" , division)
	print ("y / x :\n" , division2)
	print ("5 * y :\n" , multiplicacion3)
	print ("x^T * y :\n" , traspuesta)
	print ("Matriz generado de pueros ceros :\n" , zeros)
	print ("Matriz de identity :\n" , identity)

	return None

# Se llama al programa principal
main()

#Doy mi palabra que he realizado este trabajo con Integridad Academica