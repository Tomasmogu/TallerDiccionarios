# TallerDiccionarios
diccionarios
import math

g = float(input("Introduce un numero en grados que desee pasar a radianes: "))

rad1 = math.radians(g)

print("Con Math\n")
print(str(g) + " grados son " + str(rad1) + " radianes\n")

import math

peso = float(input("Cuantos kg pesa usted ?: "))
estatura = float(input("Cuantos metros mide usted ?: "))

Masa = round(peso/math.pow(estatura,2),1)

print("Su Indice de Masa Corporal es de "+str(Masa))

kmh = int(input('Ingrese los km/h: '))
mph =kmh* 0.2778
print('Velocidad en Km/h: ', kmh)
print('Velocidad en M/s: ', mph)
