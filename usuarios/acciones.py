import usuarios.usuario as modelo
class Acciones :
    def registro(self) :
        print("Vamos a registrarte en el sistema...\n")
        nombre = input("¿Cual es tu nombre?")
        apellidos = input("¿Cuales son tus apellidos?")
        email = input("¿Cual es tu email?")
        password = input("Introduce una contraseña:")

        usuario = modelo.Usuario(nombre,apellidos,email,password)
        registro = usuario.registro()
        if registro[0] >=1 :
            print(f"Usuario Registrado {registro[1].nombre}")
        else :
            print("El registro ha fallado")    

    def login(self) :
       print("Indentifícate\n") 
       nombre = input("¿Cual es tu nombre?")
       password = input("Contraseña:")     