import gestor

class Cliente:
    def __init__(self, usuario, password):
        self.usuario = usuario
        self.password = password

def login():
    usuarios = gestor.cargar_json("usuarios.json")
    usuario = input("Usuario: ").strip()
    password = input("Contraseña: ").strip()

    for u in usuarios:
        if u["usuario"] == usuario and u["password"] == password:
            print(f"\n Bienvenido {usuario}!\n")
            return Cliente(usuario, password)
    print(" Usuario o contraseña incorrectos")
    return None

def registrar_usuario():
    usuarios = gestor.cargar_json("usuarios.json")
    nuevo_usuario = input("Ingrese un nombre de usuario: ").strip()

    if any(u["usuario"] == nuevo_usuario for u in usuarios):
        print("El usuario ya existe, intente con otro nombre")
        return
    nueva_password = input("Ingrese una contraseña: ").strip()
    usuarios.append({
        "usuario": nuevo_usuario,
        "password": nueva_password
    })
    gestor.guardar_json("usuarios.json", usuarios)
    print(f" Usuario {nuevo_usuario} registrado con exito!")

def obtener_productos():
    return gestor.cargar_json("productos.json")

def mostrar_productos():
    productos = obtener_productos()
    print("\n--- PRODUCTO DE LA TIENDA ---")
    for p in productos:
        print(f"{p['id']}. {p['nombre']} - ${p['precio']}")

def comprar_producto(usuario):
    productos = obtener_productos()
    mostrar_productos()
    try:
        opcion = int(input("\nSeleccione el ID del producto que desea comprar: "))
        producto = next((p for p in productos if p["id"] == opcion), None)
        if producto:
            print(f"\ Gracias por su compra, {usuario.usuario}! Compraste: {producto['nombre']}\n")
        else:
            print("Producto sin stock")
    except ValueError:
        print(" Ingresar un id del stock en la tienda")
