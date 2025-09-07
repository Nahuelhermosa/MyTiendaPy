from funciones.funciones import registrar_cliente, iniciar_sesion, mostrar_clientes

def menu_principal():
    while True:
        print("\n=== MENU PRINCIPAL ===")
        print("1. Iniciar sesion")
        print("2. Registrar cliente")
        print("3. Mostrar clientes")
        print("4. Salir")

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            nombre = input("Ingrese su nombre: ")
            contraseña = input("Ingrese su contraseña: ")
            iniciar_sesion(nombre, contraseña)

        elif opcion == "2":
            nombre = input("Ingrese su nombre: ")
            contraseña = input("Ingrese su contraseña: ")
            email = input("Ingrese su email: ")
            registrar_cliente(nombre, contraseña, email)

        elif opcion == "3":
            mostrar_clientes()

        elif opcion == "4":
            print(" Saliendo del sistema...")
            break

        else:
            print("Opcion invalida, intente nuevamente.")

if __name__ == "__main__":
    menu_principal()
