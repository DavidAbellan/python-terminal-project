import mysql.connector
import datetime
import hashlib
database = mysql.connector.connect (
    host = "localhost",
    user = "root",
    passwd = "",
    database = "terminal_app_db",
    port = 3306
)
cursor = database.cursor(buffered=True)
#buffered a true para permitir muchas consultas
class Usuario : 
    def __init__(self,nombre,apellidos,email,password) :
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
        self.password = password
  
    def registro(self) :
        fecha = datetime.datetime.now()
        sql = "INSERT INTO usuarios VALUES (null,%s,%s,%s,%s,'"+str(fecha)+"')"
        
        #cifrar contraseña
        #cifrado = hashlib.sha256()
        #cifrado.update(self.password.encode('utf8'))
        #print(cifrado)
        
        usuario = (self.nombre,self.apellidos,self.email,self.password)
        print(usuario)
      #  try :
        cursor.execute(sql, usuario)
        database.commit()
        result = [cursor.rowcount, self]
       # except :
       #  result=[0,self]    
        return result    

      
    def login(self) :
        return self.apellidos