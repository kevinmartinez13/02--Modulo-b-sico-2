class Perro:
    def __init__(self, nombre, edad, color):
        self.nombre = nombre
        self.edad = edad
        self.color = color
        self.energia = 100

firulais = Perro("Firulais", 3, "dorado")
bobby = Perro("Bobby", 1, "negro")
lassie = Perro("Lassie", 5, "marrón y blanco")

print(f"{firulais.nombre} tiene {firulais.edad} años y es {firulais.color}")
print(f"{bobby.nombre} tiene {bobby.edad} año y es {bobby.color}")
print(f"{lassie.nombre} tiene {lassie.edad} años y es {lassie.color}")
