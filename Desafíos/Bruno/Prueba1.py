import pandas as pd

# Creamos un diccionario con los datos iniciales
data = {
    'Día': ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado','Domingo'],
    'Comida': ['Hamburguesa', 'Pollo asado', 'Pasta', 'Sopa de verduras','Pizza', 'Pasta', 'Asado'],
    'Plato Principal': ['Carne', 'Pollo', 'Pasta', 'Verduras','Pizza', 'Pasta', 'Carne'],
    'Acompañamiento': ['Papas fritas', 'Ensalada', 'Pan', 'Crutones','', 'Frutas', 'Papas'],
    'Bebida': ['Agua', 'Agua', 'Agua', 'Agua', 'Agua', 'Refresco', 'Refresco']
}

# Creamos un DataFrame con los datos y lo mostramos
df = pd.DataFrame(data)
print(df)

# Pedimos al usuario que ingrese los datos adicionales
dia = input("Ingrese el día de la semana: ")
comida = input("Ingrese la comida que se servirá: ")
plato_principal = input("Ingrese el plato principal que se servirá: ")
acompañamiento = input("Ingrese el acompañamiento que se servirá: ")
bebida = input("Ingrese la bebida que se servirá: ")

nuevo_dato = {
    'Día': dia,
    'Comida': comida,
    'Plato Principal': plato_principal,
    'Acompañamiento' : acompañamiento,
    'Bebida' : bebida,
}

# Agregamos el nuevo dato al DataFrame
df = df.append(nuevo_dato, ignore_index=True)

# Mostramos el DataFrame actualizado
print(df)
