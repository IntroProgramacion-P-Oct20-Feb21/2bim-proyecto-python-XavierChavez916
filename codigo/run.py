"""
    Proyecto Bimestral
    Segundo Bimestre
    
    Problemática:
    Generar un solución en lenguaje de programación Python

Que permita ingresar nuevas cuentas de diversas plataformas. Las plataformas son:

Facebook (se necesita los siguientes datos: nombre de usuario, edad, ciudad, 
pais, correo electrónico)
Twitter (se necesita los siguientes datos: nombre de usuario, nombres, apellidos, 
edad, ciudad, pais, idioma, correo electrónico)
Whatsapp (se necesita los siguientes datos: nombre de usuario, número de teléfono, 
edad, ciudad, pais)
Telegram (se necesita los siguientes datos: nombre de usuario, número de teléfono, 
ciudad, pais, área de interés)
Signal (se necesita los siguientes datos: nombre de usuario, número de teléfono, 
ciudad, pais, hobby principal)
Instagram (se necesita los siguientes datos: nombre de usuario, ciudad, edad, 
correo electrónico)
Flickr (se necesita los siguientes datos: nombre de usuario, correo electrónico)
La aplicación debe tener los siguientes procedimientos:

método principal - main
método crearFacebook - (método que devuelve un valor)
método crearTwitter - (método que no devuelve un valor)
método crearWhatsapp - - (método que devuelve un valor)
método crearTelegram - (método que no devuelve un valor)
método crearSignal- (método que devuelve un valor)
método crearInstagram - (método que no devuelve un valor)
método crearFlickr - (método que devuelve un valor)
En la función principal se presenta un ciclo repetitivo que presenta un menú 
de opciones:

Si se ingresa 1 se llamará a crearFacebook
Si se ingresa 2 se llamará a crearTwitter
Si se ingresa 3 se llamará a crearWhatsapp
Si se ingresa 4 se llamará a crearTelegram
Si se ingresa 5 se llamará a crearSignal
Si se ingresa 6 se llamará a crearInstagram
Si se ingresa 7 se llamará a crearFlickr
En cada iteración del ciclo; se pregunta al usuario si se desea salir del ciclo.

Cada método que no devuelva valores debe imprimir un resumen de la cuenta creada 
con todos los valores ingresados

Cada método que devuelva valores debe hacer un return con un resumen de la cuenta 
creada con todos los valores ingresados

Cuando el usuario termina el ciclo repetitivo se debe presentar un mensaje con base 
al número total de cuentas creadas. Se debe usar el número total de cuentas como 
argumento (entero) de una función llamada obtenerMensaje

En la función obtenerMensaje existe un parámetro. El mensaje se forma de la 
siguiente manera:
Se usa el siguiente arreglo unidimensional:  

(mensajeFinal(3),x(300)[{a-z}, {A-Z}, {BS}])

Los datos asignados al arreglo son:

mensajeFinal <-- {"Campaña con poca afluencia", "Campaña moderada siga adelante", 
"Excelente campaña"}
a. Si el número de cuentas creadas está en el rango de 1 a 5 el mensaje será: 
Campaña con poca afluencia

b. Si el número de cuentas creadas está en el rango de 6 a 15 el mensaje será: 
Campaña moderada siga adelante

c. Si el número de cuentas creadas está en el rango de 16 en adelante, el 
mensaje será: Excelente campaña

Presentación del trabajo final
En la carpeta código: use el archivo run.py
Se solicita usar como base las líneas de código del archivo
    
"""
# Se crea la funcion crearFacebook 
def crearFacebook():
    # Se pide los datos solicitados
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

# Se crea el procedimiento crearTwitter
def crearTwitter():
    # Se pide los datos solicitados
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

# Se crea la funcion crearWhatsapp
def crearWhatsapp():
    # Se pide los datos solicitados
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
    
# Se crea el procedimiento crearTelegram
def crearTelegram():
    # Se pide los datos solicitados
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

# Se crea la funcion crearSignal  
def crearSignal():
    # Se pide los datos solicitados
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

# Se crea el procedimiento crearInstagram
def crearInstagram():
    # Se pide los datos solicitados
    print("*-- Usted eligió la opción para crear una cuenta de Instagram --*")
    usuario = input("Ingrese su nombre de usuario\n> ")
    ciudad = input("Ingrese su ciudad\n> ")
    edad = int(input("Ingrese su edad\n> "))
    correo = input("Ingrese su correo electrónico\n> ")
    print(f"*--------- Datos Ingresados ---------*\n"
            f"Usuario: {usuario}\nCiudad: {ciudad}\ndad: {edad}\n"
            f"Correo Electrónico: {correo}\n"
            f"*----------------<***>---------------*")

# Se crea la funcion crearFlickr
def crearFlickr():
    # Se pide los datos solicitados
    print("*-- Usted eligió la opción para crear una cuenta de Flickr --*")
    usuario = input("Ingrese su nombre de usuario\n> ")
    correo = input("Ingrese su correo electrónico\n> ")
    cadena = (f"*--------- Datos Ingresados ---------*\n"
                f"Usuario: {usuario}\nCorreo Electrónico: {correo}\n"
                f"*----------------<***>---------------*")
    return cadena

# Se crea la funcion obtenerMensaje
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
    while bandera: # Se hace un ciclo repetitivo while 
        contador += 1 # Se inicia un contador 
        print("*--------------->Menú de opciones<--------------*")
        opcion = int(input("> Si ingresa 1 se creara una cuenta de Facebook.\n"
                    + "> Si ingresa 2 se creara una cuenta de Twitter.\n"
                    + "> Si ingresa 3 se creara una cuenta de Whatsapp.\n"
                    + "> Si ingresa 4 se creara una cuenta de Telegram.\n"
                    + "> Si ingresa 5 se creara una cuenta de Signal.\n"
                    + "> Si ingresa 6 se creara una cuenta de Instagram.\n"
                    + "> Si ingresa 7 se creara una cuenta de Flickr.\n"
                    + "*------------------\<*>|||<*>/------------------*\n> "))
        # Iniciamos una condicional if para comparar la opcion ingresada            
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
        # Se pregunta al usuario si desea salir del ciclo           
        salida = input("Ingrese 'si' para salir del ciclo\n> ")
        salida = salida.lower() # Convertimos lo que el usuario introduce a minúscula
        # Comparamos si salida es igual a "si" 
        if(salida == "si"):
            bandera = False
    print(f"*------->*Resultado de Campaña*<--------*\n"
            f"{obtenerMensaje(contador)}\n" 
            f"*--------------<*><^><*>---------------*")