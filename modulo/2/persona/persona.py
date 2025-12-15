class Persona:
    def __init__(self, nombre, edad, email="sin_email@ejemplo.com"):
        self.nombre = nombre
        self.edad = edad
        self.email = email

def debug_persona(persona):

    print(f"=== DEBUG DE {persona.nombre} ===")
    print(f"Tipo: {type(persona)}")
    print(f"ID en memoria: {id(persona)}")
    print(f"Atributos públicos: {[attr for attr in dir(persona) if not attr.startswith('_')]}")
    print(f"Diccionario interno: {vars(persona)}")
    print(f"Representación: {repr(persona)}")

if __name__ == "__main__":
    persona = Persona("Ana", 28,)
    debug_persona(persona)
