class Persona:
    def __init__(self, nombre, edad, email="sin_email@ejemplo.com"):
        self.nombre = nombre
        self.edad = edad
        self.email = email

class UsuarioRedSocial(Persona):
    def __init__(self, nombre, edad, email, username):
        super().__init__(nombre, edad, email)
        self.username = username
        self.seguidores = []
        self.publicaciones = []

    def publicar(self, contenido):
        publicacion = {'contenido': contenido, 'likes': 0}
        self.publicaciones.append(publicacion)
        return publicacion

    
usuario1 = UsuarioRedSocial("Marta", 22, "marta@email.com", "martita")
print(usuario1.publicar("Hola, mundo!"))
print(usuario1.publicaciones)

