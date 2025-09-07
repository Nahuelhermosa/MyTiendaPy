class Cliente:
    def __init__(self, nombre, contraseña, email):
        self.nombre = nombre
        self.contraseña = contraseña
        self.email = email

    def __str__(self):
        return f"Cliente: {self.nombre} | Email: {self.email}"

    def __eq__(self, other):
        if isinstance(other, Cliente):
            return self.email == other.email
        return False

    def verificar_contraseña(self, contraseña):
        return self.contraseña == contraseña

    def actualizar_email(self, nuevo_email):
        self.email = nuevo_email
        return f"Email actualizado a: {self.email}"
