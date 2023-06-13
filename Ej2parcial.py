
from collections import deque

avengers = [
    ["Star Lord", "Peter Quill", "Guardianes de la galaxia", 1976],
    ["Capitana Marvel", "", "", 1982],
    ["Iron Man", "Tony Stark", "Avengers", 1963],
    ["Thor", "", "Avengers", 1962],
    ["Black Widow", "Vlanck Widow", "Avengers", 1964],
    ["Hawkeye", "Clint Barton", "Avengers", 1964],
    ["SpiderMan", "Peter Parker", "Avengers", 1962],
    ["Capian America", "Steve Rogers", "Avengers", 1941],
    ["Hulk", "Bruce Banner", "Avengers", 1962],
    ["Doctor Strange", "", "Avengers", 1963],
    ["Scarlet Witch", "Wanda Maximoff", "Avengers", 1964],
    ["Ant-Man", "Scott Lang", "Avengers", 1979],
    ["Wasp", "Hope van Dyne", "Avengers", 1963],
    ["Vision", "", "Avengers", 1968],
    ["Falcon", "Sam Wilson", "Avengers", 1969],
    ["Hulk", "", "", 0],
    ["Groot", "", "Guardianes de la galaxia", 1960],
    ["Captain Marvel", "Carol Danvers", "Avengers", 1968],
    ["Thanos", "", "", 1973],
    ["Gamora", "", "Guardianes de la galaxia", 1975],
    ["Deadpool", "", "", 1991],
    ["Vision", "Vision", "Avengers", 1968],
    ["Kang the Conqueror", "", "", 1963],
]

capitana_marvel_nombre = ""
for heroe in avengers:
    if heroe[0] == "Capitana Marvel":
        capitana_marvel_nombre = heroe[1]

if capitana_marvel_nombre:
    print("El nombre de personaje de Capitana Marvel es:", capitana_marvel_nombre)
else:
    print("Capitana Marvel no está en la lista.")

guardianes = deque()
for heroe in avengers:
    if heroe[2] == "Guardianes de la galaxia":
        guardianes.append(heroe[0])

print("Hay", len(guardianes), "superhéroes en el grupo Guardianes de la galaxia:", list(guardianes))

fantasticos = []
for heroe in avengers:
    if heroe[2] == "Los cuatro fantásticos" or heroe[2] == "Guardianes de la galaxia":
        fantasticos.append(heroe[0])

fantasticos.sort(reverse=True)
print("Superhéroes en el grupo Los cuatro fantásticos y Guardianes de la galaxia (en orden descendente):", fantasticos)

posteriores_1960 = []
for heroe in avengers:
    if heroe[1] and heroe[3] > 1960:
        posteriores_1960.append(heroe[0])

print("Superhéroes con nombre de personaje cuyo año de aparición es posterior a 1960:", posteriores_1960)

for heroe in avengers:
    if heroe[0] == "Black Widow" and heroe[1] == "Vlanck Widow":
        heroe[1] = "Black Widow"

personajes_auxiliares = ['Black Cat', 'Hulk', 'Rocket Racoonn', 'Loki']
for personaje_auxiliar in personajes_auxiliares:
    encontrado = False
    for heroe in avengers:
        if heroe[0] == personaje_auxiliar:
            encontrado = True

    if not encontrado:
        avengers.append([personaje_auxiliar, "", "", 0])

personajes_cps = []
for heroe in avengers:
    nombre_personaje = heroe[1]
    if nombre_personaje and nombre_personaje[0] in ["C", "P", "S"]:
        personajes_cps.append(nombre_personaje)

print("Personajes que comienzan con C, P o S:", personajes_cps)