import mysql.connector
class crearDataBase :
        database = mysql.connector.connect (
            host = "localhost",
            user = "root",
            passwd = "",
            database = "terminal_app_db",
            port = 3306
        )
        cursor = database.cursor(buffered=True)
