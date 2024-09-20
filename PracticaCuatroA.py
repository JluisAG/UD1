class Triangulo:
	def __init__(self, b, h):
		self.b = b
		self.h = h
	def area(self):
		r=(self.b * self.h)/2
		return r
ba=float(input("Escribe la base  "))
ha=float(input("Escribe la alturta  "))
triangulo = Triangulo(ba, ha)
print("Área del triangulo que tiene de una base de:",ba,"  altura   ",ha,"  su area es:  ", triangulo.area())
