#desarrollar un sistema de caja de cambio donde se le indica un cantidad a cambiar el sistema devuelve la cantidad en monedas de 10,5 y un peso 
#regla: no se puede devolver todo de una sola moneda, tiene queregresar al menos una de cada denominacion
#ejemplo: 100 pesos

class Caja:
	def __init__(self):
		self.L = 0  
		self.M10 = 0  
		self.M5 = 0   
		self.M1 = 0   

	def monedas(self):
		self.L = int(input("Ingresa el billete: "))  

		while self.L > 0:  
			print("\n--- Caja de cambios ---")

			self.M10 = self.L // 10
			self.L = self.L % 10 

			self.M5 = self.L // 5
			self.L = self.L % 5   

			self.M1 = self.L // 1
			self.L = self.L % 1   
          
			if self.M10 > 0 and self.M5 > 0 and self.M1 > 0:

			print(f"Monedas de 10: {self.M10}")
            print(f"Monedas de 5: {self.M5}")
            print(f"Monedas de 1: {self.M1}")
				else:
			print("\nNo se utilizaron todas las monedas (10, 5 y 1). Intenta de nuevo.")
            
            
            self.L = int(input("\nIngresa otra cantidad o 0 para salir: "))
caja = Caja()
caja.monedas()
