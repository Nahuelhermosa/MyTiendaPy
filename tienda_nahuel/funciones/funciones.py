from clases.cliente import Cliente

clientes = []  

def registrar_cliente(nombre, contraseña, email):
    nuevo = Cliente(nombre, contraseña, email)
    clientes.append(nuevo)
    print(f" Cliente registrado: {nuevo}")

def iniciar_sesion(nombre, contraseña):
    for cliente in clientes:
        if cliente.nombre == nombre and cliente.verificar_contraseña(contraseña):
            print(f" Bienvenido {cliente.nombre}!")
            return True
    print(" Usuario o contraseña incorrectos")
    return False

def mostrar_clientes():
    if clientes:
        print("\n=== Lista de clientes ===")
        for c in clientes:
            print(c)
    else:
        print("No hay clientes registrados.")
