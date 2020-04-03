""" ia1.py
    Este trabajo mostrara como con numpy puedes sumar, 
    restar, hacer traspuesta, multiplicar y sacar la 
    longitud de un vector por medio de numpy

    Author: Gabriel Aldahir Lopez Soto
    Email: gabriel.lopez@gmail.com
    Institution: Universidad de Monterrey
    First created: Thu 06 Feb, 2020
"""
#Importa las librerias estandard
import numpy as np

def suma_vectores(x,y):
	"""
	Esta funcion es para la suma de dos vectores

	INPUTS
	:parametro 1: vector int8 
	:parametro 2: vector int8

	OUTPUTS
	:return: vector int8 con la suma de los vectores x+y

	"""
	resultado = np.add(x,y)
	return resultado

def resta_vectores(x,y):
	"""
	Esta funcion es para la resta de dos vectores

	INPUTS
	:parametro 1: vector int8 
	:parametro 2: vector int8

	OUTPUTS
	:return: vector int8 con la resta de los vectores x-y

	"""
	resultado = np.subtract(x, y)
	return resultado

def multiplicacion_vectores(x,y):
	"""
	Esta funcion es para la multiplicacion de dos vectores

	INPUTS
	:parametro 1: vector int8 
	:parametro 2: vector int8

	OUTPUTS
	:return: vector int8 con la multiplicacion de los vectores x*y

	"""
	resultado = np.multiply(x, y)
	return resultado

def tamano_vectores(y):
	"""
	Esta funcion es para obtener el tamano del vector y

	INPUTS
	:parametro 1: vector int8 

	OUTPUTS
	:return: tamano del vector y

	"""
	resultado = np.linalg.norm(y)
	return resultado

def traspuesta_vector(x,y):
	"""
	Esta funcion es para la traspuesta de x y la multiplicacion de x * y

	INPUTS
	:parametro 1: vector int8
	:parametro 2: vector int8

	OUTPUTS
	:return: vector int8 multiplicacion del vector y por la traspuesta de x

	"""
	x = x.reshape(-1,1)
	resultado = np.multiply(x, y)
	return resultado

def main():
	"""
	Aqui se declaran los vectores a usar y se usan las funciones

	Datos de entrada:
	Nada

	Datos de salida:
	Nada
	"""
	# Inicialización de dos vectores de 1 dimensión

	x = np.array([1, 2, 3], dtype=np.int8)
	y = np.array([4, 5, 6], dtype=np.int8)

	#Llama la función que suma los vectores y asigna el valor
	suma = suma_vectores(x,y)

	#Llama la función que resta los vectores y asigna el valor
	resta = resta_vectores(x,y)

	#Llama la función que multiplica los vectores y asigna el valor
	multiplicacion = multiplicacion_vectores(x,y)

	#Llama la función que hace la traspuesta del vector x y lo multiplica por y
	traspuesta = traspuesta_vector(x,y)

	#Llama la función que obtiene el tamano los vectores y asigna el valor
	tamano = tamano_vectores(y)

	#Formato de impresion
	print("\n" + 28*"-")
	print ("Operaciones de Vectores: ") 
	print(28*"-")
	print("x =", x)
	print("y =", y)
	print ("x + y =" , suma)
	print ("x - y =" , resta)
	print ("x * y =" , multiplicacion)
	print ("x^T * y =" , traspuesta)
	print("length of y =",tamano)

	return None

# Se llama al programa principal
main()

#Doy mi palabra que he realizado este trabajo con Integridad Academica