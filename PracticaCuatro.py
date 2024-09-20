class Rectangulo:
	def __init__(self, b, h):
		self.b = b
		self.h = h
	def area(self):
		return self.b * self.h
ba=float(input("Escribe la base  "))
ha=float(input("Escribe la alturta  "))
rectangulo = Rectangulo(ba, ha)
print("Área del rectangulo que tiene de una base de:",ba,"  altura   ",ha,"  su area es:  ", rectangulo.area())
