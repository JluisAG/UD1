class Calificaciones:
    def __init__(self):
        self.nombre = input("Ingresa el nombre: ")
        self.c1 = int(input("Ingresa la primera calificación: "))
        self.c2 = int(input("Ingresa la segunda calificación: "))
        self.c3 = int(input("Ingresa la tercera calificación: "))
        self.promedio = 0

class Promedio(Calificaciones):
    def prom(self):
        if self.c1 >= 70 and self.c2 >= 70 and self.c3 >= 70:
            self.promedio = (self.c1 + self.c2 + self.c3) / 3
        else:
            self.promedio = 0

class Comparacion(Promedio):
    def comparacion(self):
        if self.promedio >= 70:
            rs = "aprobado"
        else:
            rs = "reprobado"
        return rs

class Imprimir(Comparacion):
    def imprimir(self):
        print(f"El alumno {self.nombre}, con calificaciones:")
        print(f"Calificación 1: {self.c1}")
        print(f"Calificación 2: {self.c2}")
        print(f"Calificación 3: {self.c3}")
        print(f"Promedio: {self.promedio}")
        print(f"Resultado: {self.comparacion()}")

cal = Imprimir()
cal.prom()
cal.imprimir()
