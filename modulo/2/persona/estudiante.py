class Persona:
    def __init__(self, nombre, edad, email="sin_email@ejemplo.com"):
        self.nombre = nombre
        self.edad = edad
        self.email = email

class Estudiante(Persona):
    def __init__(self, nombre, edad, email, carrera):
        super().__init__(nombre, edad, email)
        self.carrera = carrera
        self.materias = {}

    def inscribir_materia(self, materia, creditos):
        self.materias[materia] = {'creditos': creditos, 'calificacion': None}

    def calcular_promedio(self):
        calificaciones = [m['calificacion'] for m in self.materias.values() if m['calificacion'] is not None]
        return sum(calificaciones)/len(calificaciones) if calificaciones else 0

estudiante1 = Estudiante("Carlos", 21, "carlos@email.com", "Ingeniería")
estudiante1.inscribir_materia("Matemáticas", 4)
estudiante1.materias["Matemáticas"]["calificacion"] = 90
print(f"Promedio: {estudiante1.calcular_promedio()}")

