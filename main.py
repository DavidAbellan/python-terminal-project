import usuarios.acciones as ac
print ( """
Acciones disponibles :
       -registro
       -login
""")
accion = input("¿Qué quieres hacer? ")
hazEl = ac.Acciones()
if accion == "registro" :
    hazEl.registro() 
  
elif accion == 'login' :
    hazEl.login()

else : 
    print("Puede seleccionar registro o login")    