import datetime
import hashlib
import usuarios.conexion as conexion
database = conexion.crearDataBase().database
cursor = conexion.crearDataBase().cursor
#buffered a true para permitir muchas consultas
class Usuario : 
    def __init__(self,nombre,apellidos,email,password) :
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
        self.password = password
  
    def registro(self) :
        fecha = datetime.datetime.now()
        sql = "INSERT INTO usuarios VALUES (null,%s,%s,%s,%s,%s)"
        
        #cifrar contraseña
        cifrado = hashlib.sha256()
        cifrado.update(self.password.encode('utf8'))
        
        usuario = (self.nombre,self.apellidos,self.email,cifrado.hexdigest(),fecha)
        try :
          cursor.execute(sql, usuario)
          database.commit()
          result = [cursor.rowcount, self]
        except :
          result=[0,self]    
        return result    

      
    def login(self) :
        sql ="SELECT * FROM usuarios WHERE nombre = %s AND password = %s"
        cifrado = hashlib.sha256()
        cifrado.update(self.password.encode('utf8'))
        usuario = (self.nombre,cifrado.hexdigest())
        cursor.execute(sql,usuario)
        result = cursor.fetchone()
        return result