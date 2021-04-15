import usuarios.conexion as conexion
import datetime

cursor = conexion.crearDataBase().cursor
database = conexion.crearDataBase().database

class Nota :
    def __init__ (self, usuarioId, titulo="", contenido="") :
        self.usuarioId = usuarioId
        self.titulo = titulo
        self.contenido = contenido

    def guardar(self) :
        sql = "INSERT INTO notas VALUES (null,%s,%s,%s,NOW())"
        nota = (self.usuarioId,self.titulo,self.contenido)
        cursor.execute(sql,nota)
        database.commit()
        return[cursor.rowcount,self]

    def listar(self) :
        sql =f"SELECT * FROM notas WHERE usuario_id = {self.usuarioId}"
        cursor.execute(sql)
        result = cursor.fetchall() 
        return result   
    def eliminar(self) :
        print(self.titulo)
        sql = f"DELETE FROM notas WHERE titulo = '{self.titulo}'"

        cursor.execute(sql)
        database.commit()
        return(cursor.rowcount,self)