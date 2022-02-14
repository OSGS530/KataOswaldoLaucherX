# Declaramos 2 variables

new_planet = ''
planets = []

# Escribe el ciclo while solicitado

while new_planet.lower() != 'done':
    if new_planet:
        planets.append(new_planet)
    new_planet = input('Enter a new planet ')

# Escribe tu ciclo for para iterar en una lista de planetas
for planet in planets:
    print(planet)
