


class Alumno:
    def __init__(self, nombre, A, B, C):
        self.nom = nombre
        self.A = A
        self.B = B
        self.C = C
    def datos():
        self.nom = input("Ingresa el nombre del alumno: ")
        self.A = int(input("Ingresa la primera calificación: "))
        self.B = int(input("Ingresa la segunda calificación: "))
        self.C = int(input("Ingresa la tercera calificación: "))
        return Alumno(nom, A, B, C)

    def promedio(self):
        p = (self.A + self.B + self.C) / 3
        return p

    def comparacion(promedio):
         if self.promedio() >70:
            x="El alumno ha reprobado."
        else:
            x= "El alumno ha aprobado."
        return x
alumno = Alumno()
alumno.datos()  

print(f"El promedio de {alumno.nom} es {alumno.promedio}",alumnos.comparacion)
print(alumno.comparacion())

    




