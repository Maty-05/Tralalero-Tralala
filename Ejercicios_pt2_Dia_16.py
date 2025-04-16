#Ejercicio1:

base = 5
altura = 3
area = base * altura
perimetro = 2 * (base + altura)
print("Área del rectángulo: ", area)
print("Perímetro del rectángulo: ", perimetro)

#Ejercicio2:
potencia = 15 ** 2
es_mayor = potencia > 200
print("¿15 elevado a 2 es mayor que 200?: ", es_mayor)

#Ejercicio3:
edad = int(input("Ingresa tu edad: "))
tiene_licencia = input("¿Tienes licencia de conducir? (sí/no): ")
puede_votar = edad >= 18
puede_conducir = tiene_licencia == "sí"

if puede_votar and puede_conducir:
    print("Puedes votar y tienes licencia de conducir.")
elif puede_votar:
    print("Puedes votar, pero no tienes licencia de conducir.")
elif puede_conducir:
    print("Tienes licencia de conducir, pero no puedes votar.")
else:
    print("No puedes votar ni tienes licencia de conducir.")
