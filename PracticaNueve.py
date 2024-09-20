#pedir un numeor y que de la tabla de multiplicar utilizando r for u hwhile


num = int(input("Ingrese el número para mostrar : "))
i = 1
print(f"\n### Tabla del {num} ###")
while i < 11:
    print(f"{num} X {i} = {num * i}")
    i += 1

