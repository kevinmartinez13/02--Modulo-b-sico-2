class Persona:
    def __init__(self, nombre, edad, email="sin_email@ejemplo.com"):
        if not isinstance(nombre, str) or len(nombre.strip()) == 0:
            raise ValueError("El nombre debe ser un texto no vacío")
        if not isinstance(edad, int) or edad < 0:
            raise ValueError("La edad debe ser un número entero positivo")
        self.nombre = nombre.strip().title()
        self.edad = edad
        self.email = email.lower()
        self._activo = True
        self.__id_interno = id(self)

    def saludar(self):
        return f"¡Hola! Mi nombre es {self.nombre} y tengo {self.edad} años."

    def cumplir_años(self):
        self.edad += 1
        return f"¡Feliz cumpleaños {self.nombre}! Ahora tienes {self.edad} años."

    def cambiar_email(self, nuevo_email):
        if "@" not in nuevo_email or "." not in nuevo_email:
            raise ValueError("Email inválido")
        self.email = nuevo_email.lower()
        return f"Email actualizado a: {self.email}"

    def __str__(self):
        return f"Persona(nombre='{self.nombre}', edad={self.edad})"

    def __repr__(self):
        return f"Persona('{self.nombre}', {self.edad}, '{self.email}')"

    def __eq__(self, otra_persona):
        if not isinstance(otra_persona, Persona):
            return False
        return self.nombre == otra_persona.nombre and self.edad == otra_persona.edad

    def __lt__(self, otra_persona):
        return self.edad < otra_persona.edad

    @property
    def es_mayor_edad(self):
        return self.edad >= 18

    @property
    def activo(self):
        return self._activo

    @activo.setter
    def activo(self, valor):
        if not isinstance(valor, bool):
            raise ValueError("El estado activo debe ser True o False")
        self._activo = valor

    @classmethod
    def desde_string(cls, datos_string):
        try:
            nombre, edad, email = datos_string.split(',')
            return cls(nombre.strip(), int(edad.strip()), email.strip())
        except ValueError:
            raise ValueError("Formato inválido. Use: 'Nombre,Edad,Email'")

    @staticmethod
    def es_nombre_valido(nombre):
        return isinstance(nombre, str) and len(nombre.strip()) > 0 and nombre.strip().isalpha()


if __name__ == "__main__":
    print("=== CREANDO PERSONAS ===")
    
    persona1 = Persona("juan pérez", 25, "juan@email.com")
    print(f"Persona creada: {persona1}")
    print(f"¿Es mayor de edad? {persona1.es_mayor_edad}")
    
    print(f"\n{persona1.saludar()}")
    print(persona1.cumplir_años())
    
    persona2 = Persona.desde_string("María García,30,maria@email.com")
    print(f"Desde string: {persona2}")
    
    persona3 = Persona("Juan Pérez", 26)
    print(f"\n¿Son iguales persona1 y persona3? {persona1 == persona3}")
    print(f"¿persona1 es menor que persona2? {persona1 < persona2}")
    
    personas = [persona1, persona2, persona3]
    personas_ordenadas = sorted(personas)
    print(f"\nPersonas ordenadas por edad:")
    for p in personas_ordenadas:
        print(f" - {p}")
    
    nombres_test = ["Ana", "123", "", "José María"]
    for nombre in nombres_test:
        valido = Persona.es_nombre_valido(nombre)
        print(f"¿'{nombre}' es válido? {valido}")
    
    try:
        persona_error = Persona("", -5)
    except ValueError as e:
        print(f"\nError capturado: {e}")
    
    persona1.activo = False
    print(f"\n¿Persona1 está activa? {persona1.activo}")
