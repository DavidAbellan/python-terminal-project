import notas.nota as modelo
class Acciones:
    def crear(self, usuario) :
          print(f"Nota de {usuario[1]} {usuario[2]}")
          titulo = input("Introduce un título : ")
          contenido = input(". . .")
          nota = modelo.Nota(usuario[0],titulo,contenido)
          guardar = nota.guardar()
          if guardar[0] >= 1 :
              print(f"Nota guardada : {titulo} --- {usuario[2]}")
          else :
              print("Error - no se ha guardado la nota") 

    def mostrar(self,usuario) :
          print(f"lista de notas del usuario : {usuario[1]} {usuario[2]}") 
          
          nota = modelo.Nota(usuario[0])
          notas = nota.listar()
          for n in notas :
            print("*************")  
            print(n[2])

    def borrar (self,usuario) :
        print("Borrando ... ")
        titulo = input("Título para borrar : ")
        nota = modelo.Nota(usuario[0],titulo)
        eliminar = nota.eliminar()
        if eliminar[0] >= 1 :
            print(f"Se ha eliminado el titulo : {titulo}")
        else :
            print("No se ha podido borrar")    

