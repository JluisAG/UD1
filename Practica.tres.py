"""class saludo:
  def __init__(self, nombre):
    self.nombre= nombre

  def decir_hola(self):
    return f"Hola, {self.nombre}!"

nombre_usuario = input("¿Cual es tu nombre?")

saludo= saludo(nombre_usuario)

print(saludo.decir_hola())"""

class Alumno:
	def __init__(self,nombre):
		self.nom = nombre
	def saludar(self):
			"""Imprime un saludo en pantalla."""
			print(f"¡Hola, {self.nom}!")
n=input("Escreibe tu nombre")
x=Alumno(n)
x.saludar()
"""print(x.nombre)"""
