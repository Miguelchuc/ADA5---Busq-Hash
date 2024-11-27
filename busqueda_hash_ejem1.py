import hashlib


def generar_hash(password):
    return hashlib.sha256(password.encode()).hexdigest()


base_de_datos = {}


def registrar_usuario(username, password):
    base_de_datos[username] = generar_hash(password)
    print(f"Usuario {username} registrado exitosamente.")


def iniciar_sesion(username, password):
    if username in base_de_datos:
        if base_de_datos[username] == generar_hash(password):
            print("Inicio de sesión exitoso.")
        else:
            print("Contraseña incorrecta.")
    else:
        print("Usuario no encontrado.")

registrar_usuario("usuario1", "mi_secreta_contraseña")
iniciar_sesion("usuario1", "mi_secreta_contraseña")  
iniciar_sesion("usuario1", "contraseña_errónea")    
