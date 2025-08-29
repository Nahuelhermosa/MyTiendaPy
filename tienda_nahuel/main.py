import cliente

def menu_principal():
    while True:
        print("\n=== LA TIENDA DE NAHUEL ===")
        print("1. Iniciar sesion para ver mercaderia")
        print("2. Registrar nuevo cliente")
        print("3. Salir")
        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            usuario = cliente.login()
            if usuario:
                menu_usuario(usuario)
        elif opcion == "2":
            cliente.registrar_usuario()
        elif opcion == "3":
            print(" Gracias por su visita")
            break
        else:
            print(" Opción invalida")

def menu_usuario(cliente_activo):
    while True:
        print("\n=== MENU DE USUARIOS ===")
        print("1. Ver productos")
        print("2. Comprar producto")
        print("3. Cerrar sesion")
        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            cliente.mostrar_productos()
        elif opcion == "2":
            cliente.comprar_producto(cliente_activo) 
        elif opcion == "3":
            print(f" Sesion cerrada ({cliente_activo.usuario})")
            break
        else:
            print(" Opcion invalida")

if __name__ == "__main__":
    menu_principal()
