
class Menu:
    def __init__(self):
        self.opcion = 0

    def mostrar_menu(self):
        while self.opcion != 4:
            print("\n--- Menú ---")
            print("1: Opción 1")
            print("2: Opción 2")
            print("3: Opción 3")
            print("4: Salir")

            try:
                self.opcion = int(input("Selecciona una opción: "))
            except ValueError:
                print("Por favor, ingresa un número válido.")
                continue

            self.ejecutar_opcion()

    def ejecutar_opcion(self):
        if self.opcion == 1:
            print("Elegiste la opción uno")
        elif self.opcion == 2:
            print("Elegiste la opción dos")
        elif self.opcion == 3:
            print("Elegiste la opción tres")
        elif self.opcion == 4:
            print("Saliste del menú")
        else:
            print("Opción no válida, intenta nuevamente.")

menu = Menu()
menu.mostrar_menu()
