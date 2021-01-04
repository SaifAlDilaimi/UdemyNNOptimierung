# Eine unbekannte Anzahl von Strings ausgeben
def print_cities(*cities):
    for city in cities:
        print(city)

print_cities("Berlin", "Paris", "London")

print_cities("Berlin", "Paris", "London", 45)

print_cities("Berlin", "Paris")

def print_city(city, *cities):
    print(city)
    for city in cities:
        print(city)

print_city("Berlin", "London", "Paris", "Prag")

def numbers(a, b, c):
    print(a, b, c)


z = (2, 4, 6)
numbers(*z)