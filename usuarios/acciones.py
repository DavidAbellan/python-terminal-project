import usuarios.usuario as modelo
import notas.acciones as accionesDeNotas
import datetime

class Acciones :
    def registro(self) :
        print("Vamos a registrarte en el sistema...\n")
        nombre = input("¿Cual es tu nombre? ")
        apellidos = input("¿Cuales son tus apellidos? ")
        email = input("¿Cual es tu email? ")
        password = input("Introduce una contraseña: ")

        usuario = modelo.Usuario(nombre,apellidos,email,password)
        registro = usuario.registro()
        if registro[0] >=1 :
            print(f"Usuario Registrado {registro[1].nombre}")
        else :
            print("El registro ha fallado")    

    def login(self) :
        print("Indentifícate\n") 
        try :
            nombre = input("¿Cual es tu nombre? ")
            password = input("Contraseña: ")    
            usuario = modelo.Usuario(nombre,'','',password)
            login = usuario.login()
            if nombre == login[1] :
                print(f"Usuario {nombre} logueado correctamente, {datetime.datetime.now()}") 
                self.proximasAcciones(login)
        except Exception as e :
            print(type(e))
            print(e)
            print("No ha podido loguearse, inténtelo más adelante")      

    def proximasAcciones(self,usuario) :
            print ( """
            Acciones disponibles :
            --Crear Nota(crear)
            --Mostrar tus Notas (mostrar)
            --Eliminar Nota(eliminar)
            --Salir(salir)
            
            
            """)
            accion = 'nothing'
            while accion != "crear" or accion != "mostrar" or accion != "eliminar" or accion != "salir" :
                accion = input ("¿Qué desea hacer ? ")     
                hazEl = accionesDeNotas.Acciones() 
                if accion == "crear":
                    hazEl.crear(usuario)

                elif accion == "mostrar":
                    hazEl.mostrar(usuario)


                elif accion == "eliminar" :
                    hazEl.borrar(usuario)

                elif accion == 'salir':
                    print(f"Vuelve pronto {usuario[1]} !!!")
                    exit()
