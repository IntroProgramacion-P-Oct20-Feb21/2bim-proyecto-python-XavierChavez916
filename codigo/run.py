"""
    Proyecto Bimestral
    Segundo Bimestre
    
    Problemática:
"""

def crearFacebook():
    print("*-- Usted eligió la opción para crear una cuenta de Facebook --*")
    usuario = input("Ingrese su nombre de usuario\n> ")
    edad = int(input("Ingrese su edad\n> "))
    ciudad = input("Ingrese su ciudad\n> ")
    pais = input("Ingrese su país\n> ")
    correo = input("Ingrese su correo electrónico\n> ")
    cadena = (f"*--------- Datos Ingresados ---------*\n"
                f"Usuario: {usuario}\nEdad: {edad}\nCiudad: {ciudad}\n"
                f"País: {pais}\nCorreo Electrónico: {correo}\n"
                f"*----------------<***>---------------*")
    return cadena

def crearTwitter():
    print("*-- Usted eligió la opción para crear una cuenta de Twitter --*")
    usuario = input("Ingrese su nombre de usuario\n> ")
    apellidos = input("Ingrese sus apellidos\n> ")
    edad = int(input("Ingrese su edad\n> "))
    ciudad = input("Ingrese su ciudad\n> ")
    pais = input("Ingrese su país\n> ")
    idioma = input("Ingrese su idioma\n> ")
    correo = input("Ingrese su correo electrónico\n> ")
    print(f"*---------* Datos Ingresados *---------*\n"
            f"Usuario: {usuario}\nApellidos: {apellidos}\nEdad: {edad}\n"
            f"Ciudad: {ciudad}\nPaís: {pais}\nIdioma: {idioma}\n"
            f"Correo Electrónico: {correo}\n"
            f"*----------------\<***>/---------------*")

def crearWhatsapp():
    print("*-- Usted eligió la opción para crear una cuenta de Whatsapp --*")
    usuario = input("Ingrese su nombre de usuario\n> ")
    numero = int(input("Ingrese su número de teléfono\n> "))
    edad = int(input("Ingrese su edad\n> "))
    ciudad = input("Ingrese su ciudad\n> ")
    pais = input("Ingrese su país\n> ")
    cadena = (f"*--------- Datos Ingresados ---------*\n"
                f"Usuario: {usuario}\nNúmero de teléfono: {numero}\n"
                f"Edad: {edad}\nCiudad: {ciudad}\nPaís: {pais}\n"
                f"*----------------<***>---------------*")
    return cadena

def crearTelegram():
    print("*-- Usted eligió la opción para crear una cuenta de Telegram --*")
    usuario = input("Ingrese su nombre de usuario\n> ")
    numero = int(input("Ingrese su número de teléfono\n> "))
    ciudad = input("Ingrese su ciudad\n> ")
    pais = input("Ingrese su país\n> ")
    area_interes = input("Ingrese su área de interés\n> ")
    print(f"*--------- Datos Ingresados ---------*\n"
            f"Usuario: {usuario}\nNúmero de teléfono: {numero}\n"
            f"Ciudad: {ciudad}\nPaís: {pais}\nÁrea de Interés: {area_interes}\n"
            f"*----------------<***>---------------*")
    
def crearSignal():
    print("*-- Usted eligió la opción para crear una cuenta de Signal --*")
    usuario = input("Ingrese su nombre de usuario\n> ")
    numero = int(input("Ingrese su número de teléfono\n> "))
    ciudad = input("Ingrese su ciudad\n> ")
    pais = input("Ingrese su país\n> ")
    hobby = input("Ingrese su hobby principal\n> ")
    cadena = (f"*--------- Datos Ingresados ---------*\n"
                f"Usuario: {usuario}\nNúmero de teléfono: {numero}\n"
                f"Ciudad: {ciudad}\nPaís: {pais}\nHobby principla: {hobby}\n"
                f"*----------------<***>---------------*")
    return cadena

def crearInstagram():
    print("*-- Usted eligió la opción para crear una cuenta de Instagram --*")
    usuario = input("Ingrese su nombre de usuario\n> ")
    ciudad = input("Ingrese su ciudad\n> ")
    edad = int(input("Ingrese su edad\n> "))
    correo = input("Ingrese su correo electrónico\n> ")
    print(f"*--------- Datos Ingresados ---------*\n"
            f"Usuario: {usuario}\nCiudad: {ciudad}\ndad: {edad}\n"
            f"Correo Electrónico: {correo}\n"
            f"*----------------<***>---------------*")

def crearFlickr():
    print("*-- Usted eligió la opción para crear una cuenta de Flickr --*")
    usuario = input("Ingrese su nombre de usuario\n> ")
    correo = input("Ingrese su correo electrónico\n> ")
    cadena = (f"*--------- Datos Ingresados ---------*\n"
                f"Usuario: {usuario}\nCorreo Electrónico: {correo}\n"
                f"*----------------<***>---------------*")
    return cadena

def obtenerMensaje(a):
    mensaje_final = ["Campaña con poca afluencia",
            "Campaña moderada siga adelante", "Excelente campaña"]

    if ((a >= 1) and (a <= 5)):
        cadena = mensaje_final[0]
    else:
        if((a >= 6) and (a <= 15)):
            cadena = mensaje_final[1]
        else:
            if(a >= 16):
                cadena = mensaje_final[2] 
    return cadena                  

if __name__ == "__main__":
    bandera = True
    contador = 0
    while bandera:
        contador += 1
        print("*--------------->Menú de opciones<--------------*")
        opcion = int(input("> Si ingresa 1 se creara una cuenta de Facebook.\n"
                    + "> Si ingresa 2 se creara una cuenta de Twitter.\n"
                    + "> Si ingresa 3 se creara una cuenta de Whatsapp.\n"
                    + "> Si ingresa 4 se creara una cuenta de Telegram.\n"
                    + "> Si ingresa 5 se creara una cuenta de Signal.\n"
                    + "> Si ingresa 6 se creara una cuenta de Instagram.\n"
                    + "> Si ingresa 7 se creara una cuenta de Flickr.\n"
                    + "*------------------\<*>|||<*>/------------------*\n> "))
        if (opcion == 1):
            cuenta_facebook = crearFacebook()
            print(cuenta_facebook)
        else:
            if(opcion == 2):
                crearTwitter()
            else:
                if(opcion == 3):
                    cuenta_whatsapp = crearWhatsapp()
                    print(cuenta_whatsapp)
                else:
                    if(opcion == 4):
                        crearTelegram()                       
                    else:
                        if(opcion == 5):
                            cuenta_signal = crearSignal()
                            print(cuenta_signal)
                        else:
                            if(opcion == 6):
                                crearInstagram()
                            else:
                                if(opcion == 7):
                                    cuenta_flickr = crearFlickr()
                                    print(cuenta_flickr) 
                                else:
                                    print("Opción incorrecta") 
        salida = input("Ingrese 'si' si desea salir del ciclo\n> ")
        if(salida == "si"):
            bandera = False
    print(obtenerMensaje(contador))                                    
                                        

        

                 

