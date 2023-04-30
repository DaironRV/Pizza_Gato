print("Adopciòn de una gato")
respuesta= input ("¿Tienes lo necesario para adoptar un gato? (si/no)")
if respuesta == "si":
    print(" genial, acontinuacion una lista de las cosas que necesitas")
    cosas_para_gato=["cama", "comida", "jugetes", "arenero", "tazon"]
    print (cosas_para_gato)
elif respuesta == "no": 
    respuesta_dinero=input ("tienes el dinero para las las cosas del gato? si/no")
    if respuesta_dinero == "no":
        print ("Fin de la adopciòn")

respuesta_dinero=( "tienes el dinero para las cosas del gato? si:1/no:2")
if respuesta == "1":
    cosas_para_gato=["cama", "comida", "jugetes", "arenero", "tazon"]
    print(cosas_para_gato)

respuesta=print (" ¿ donde vas a adopatr a el gato? (1)refugio/2)persona del comun)")
if respuesta == "1":
    print("genial! ahora los pasos a seguir para el fin de la adopcion", "paso 1: ir al refugio", "paso 2: encontrar al gato", "paso 3: frrmar los papeles")
elif respuesta == "2":
    print ("Con una persona del comun, que bien. Ahora los pasos que faltan", "paso 1: ir al refugio", "paso 2: encontrar al gato", "paso 3: frrmar los papeles")
else: 
    print("Esa respuesta no es valida, escoge entre 1 y 2")

print("fin de la adopcion")