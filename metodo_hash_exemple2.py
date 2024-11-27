
tabla_hash = {}


def funcion_hash(user_id):
    return user_id % 10 


def agregar_al_carrito(user_id, item):
    clave = funcion_hash(user_id)
    if clave not in tabla_hash:
        tabla_hash[clave] = []
    tabla_hash[clave].append((user_id, item))
    print(f"Artículo '{item}' agregado al carrito del usuario {user_id}.")

def mostrar_carrito(user_id):
    clave = funcion_hash(user_id)
    carrito = [item for uid, item in tabla_hash.get(clave, []) if uid == user_id]
    print(f"Carrito del usuario {user_id}: {carrito}")


agregar_al_carrito(123, "Laptop")
agregar_al_carrito(124, "Teléfono")
agregar_al_carrito(123, "Mouse")

mostrar_carrito(123)  
mostrar_carrito(124) 
