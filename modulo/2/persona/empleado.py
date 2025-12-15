class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
 

class Empleado(Persona):
    def __init__(self, nombre, edad, salario):
        super().__init__(nombre, edad,)

        self.salario = salario

    def aumentar_salario(self, porcentaje):
        self.salario *= (1 + porcentaje / 100)
        return f"Nuevo salario de {self.nombre}: ${self.salario:,.2f}"


empleado1 = Empleado("Luis", 30, 2000)
print(empleado1.aumentar_salario(10)) 