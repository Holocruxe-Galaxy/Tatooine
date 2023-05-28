# import src/db.sqlite3 as db
import sqlite3

# insertar tipos de comida en la tabla Tipo_Comida


def insertar_tipos_comida():
    conn = sqlite3.connect("db.sqlite3")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO gustos_tipo_comida (nombre) VALUES ('Desayuno')")
    cursor.execute(
        "INSERT INTO gustos_tipo_comida (nombre) VALUES ('Almuerzo')")
    cursor.execute("INSERT INTO gustos_tipo_comida (nombre) VALUES ('Cena')")
    cursor.execute("INSERT INTO gustos_tipo_comida (nombre) VALUES ('Postre')")
    cursor.execute("INSERT INTO gustos_tipo_comida (nombre) VALUES ('Snack')")
    conn.commit()
    conn.close()


# si la tabla Tipo_Comida esta vacia, insertar los tipos de comida


def insertar_tipos_comida_if_empty():
    conn = sqlite3.connect("db.sqlite3")
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM gustos_tipo_comida")
    if cursor.fetchone()[0] == 0:
        insertar_tipos_comida()
    conn.close()


comidas = [
    ("2020-01-01", "Huevos revueltos", 1),
    ("2020-01-01", "Milanesa con pure", 2),
    ("2020-01-01", "Tarta de jamon y queso", 3),
    ("2020-01-01", "Helado", 4),
    ("2020-01-01", "Galletitas", 5),
    ("2020-01-02", "Cafe con leche", 1),
    ("2020-01-02", "Pollo al horno", 2),
    ("2020-01-02", "Pizza", 3),
    ("2020-01-02", "Flan", 4),
    ("2020-01-02", "Galletitas", 5),
    ("2020-01-03", "Cafe con leche", 1),
    ("2020-01-03", "Milanesa con pure", 2),
    ("2020-01-03", "Tarta de jamon y queso", 3),
    ("2020-01-03", "Helado", 4),
    ("2020-01-03", "Galletitas", 5),
    ("2020-01-04", "Cafe con leche", 1),
    ("2020-01-04", "Pollo al horno", 2),
    ("2020-01-04", "Pizza", 3),
    ("2020-01-04", "Flan", 4),
    ("2020-01-04", "Galletitas", 5),
    ("2020-01-05", "Huevos revueltos", 1),
    ("2020-01-05", "Milanesa con pure", 2),
    ("2020-01-05", "Tarta de jamon y queso", 3),
    ("2020-01-05", "Helado", 4),
    ("2020-01-05", "Galletitas", 5),
    ("2020-01-06", "Cafe con leche", 1),
    ("2020-01-06", "Pollo al horno", 2),
    ("2020-01-06", "Pizza", 3),
    ("2020-01-06", "Flan", 4),
    ("2020-01-06", "Galletitas", 5),
    ("2020-01-07", "Cafe con leche", 1),
    ("2020-01-07", "Milanesa con pure", 2),
    ("2020-01-07", "Tarta de jamon y queso", 3),
    ("2020-01-07", "Helado", 4),
    ("2020-01-07", "Galletitas", 5),
    ("2020-01-08", "Cafe con leche", 1),
    ("2020-01-08", "Pollo al horno", 2),
    ("2020-01-08", "Pizza", 3),
    ("2020-01-08", "Flan", 4),
    ("2020-01-08", "Galletitas", 5),
    ("2020-01-09", "Huevos revueltos", 1),
    ("2020-01-09", "Milanesa con pure", 2),
    ("2020-01-09", "Tarta de jamon y queso", 3),
    ("2020-01-09", "Helado", 4),
    ("2020-01-09", "Galletitas", 5),
    ("2020-01-10", "Cafe con leche", 1),
    ("2020-01-10", "Pollo al horno", 2),
    ("2020-01-10", "Pizza", 3),
    ("2020-01-10", "Flan", 4),
    ("2020-01-10", "Galletitas", 5),
    ("2020-01-11", "Cafe con leche", 1),
    ("2020-01-11", "Milanesa con pure", 2),
    ("2020-01-11", "Tarta de jamon y queso", 3),
    ("2020-01-11", "Helado", 4),
    ("2020-01-11", "Galletitas", 5),
    ("2020-01-12", "Cafe con leche", 1),
    ("2020-01-12", "Pollo al horno", 2),
    ("2020-01-12", "Pizza", 3),
    ("2020-01-12", "Flan", 4),
    ("2020-01-12", "Galletitas", 5),
    ("2020-01-13", "Huevos revueltos", 1),
    ("2020-01-13", "Milanesa con pure", 2),
    ("2020-01-13", "Tarta de jamon y queso", 3),
    ("2020-01-13", "Helado", 4),
    ("2020-01-13", "Galletitas", 5),
    ("2020-01-14", "Cafe con leche", 1),
    ("2020-01-14", "Pollo al horno", 2),
    ("2020-01-14", "Pizza", 3),
    ("2020-01-14", "Flan", 4),
    ("2020-01-14", "Galletitas", 5),
    ("2020-01-15", "Cafe con leche", 1),
    ("2020-01-15", "Milanesa con pure", 2),
    ("2020-01-15", "Tarta de jamon y queso", 3),
    ("2020-01-15", "Helado", 4),
    ("2020-01-15", "Galletitas", 5),
    ("2020-01-16", "Cafe con leche", 1),
    ("2020-01-16", "Pollo al horno", 2),
    ("2020-01-16", "Pizza", 3),
    ("2020-01-16", "Flan", 4),
    ("2020-01-16", "Galletitas", 5),
    ("2020-01-17", "Huevos revueltos", 1),
    ("2020-01-17", "Milanesa con pure", 2),
    ("2020-01-17", "Tarta de jamon y queso", 3),
    ("2020-01-17", "Helado", 4),
    ("2020-01-17", "Galletitas", 5),
    ("2020-01-18", "Cafe con leche", 1),
    ("2020-01-18", "Pollo al horno", 2),
    ("2020-01-18", "Pizza", 3),
    ("2020-01-18", "Flan", 4),
    ("2020-01-18", "Galletitas", 5),
    ("2020-01-19", "Cafe con leche", 1),
    ("2020-01-19", "Milanesa con pure", 2),
    ("2020-01-19", "Tarta de jamon y queso", 3),
    ("2020-01-19", "Helado", 4),
    ("2020-01-19", "Galletitas", 5),
    ("2020-01-20", "Cafe con leche", 1),
    ("2020-01-20", "Pollo al horno", 2),
    ("2020-01-20", "Pizza", 3),
    ("2020-01-20", "Flan", 4),
    ("2020-01-20", "Galletitas", 5),
    ("2020-01-21", "Huevos revueltos", 1),
    ("2020-01-21", "Milanesa con pure", 2),
    ("2020-01-21", "Tarta de jamon y queso", 3),
    ("2020-01-21", "Helado", 4),
    ("2020-01-21", "Galletitas", 5),
    ("2020-01-22", "Cafe con leche", 1),
    ("2020-01-22", "Pollo al horno", 2),
    ("2020-01-22", "Pizza", 3),
    ("2020-01-22", "Flan", 4),
    ("2020-01-22", "Galletitas", 5),
    ("2020-01-23", "Cafe con leche", 1),
    ("2020-01-23", "Milanesa con pure", 2),
    ("2020-01-23", "Tarta de jamon y queso", 3),
    ("2020-01-23", "Helado", 4),
    ("2020-01-23", "Galletitas", 5),
    ("2020-01-24", "Cafe con leche", 1),
    ("2020-01-24", "Pollo al horno", 2),
    ("2020-01-24", "Pizza", 3),
    ("2020-01-24", "Flan", 4),
    ("2020-01-24", "Galletitas", 5),
    ("2020-01-25", "Huevos revueltos", 1),
    ("2020-01-25", "Milanesa con pure", 2),
    ("2020-01-25", "Tarta de jamon y queso", 3),
    ("2020-01-25", "Helado", 4),
    ("2020-01-25", "Galletitas", 5),
    ("2020-01-26", "Cafe con leche", 1),
    ("2020-01-26", "Pollo al horno", 2),
    ("2020-01-26", "Pizza", 3),
    ("2020-01-26", "Flan", 4),
    ("2020-01-26", "Galletitas", 5),
    ("2020-01-27", "Cafe con leche", 1),
    ("2020-01-27", "Milanesa con pure", 2),
    ("2020-01-27", "Tarta de jamon y queso", 3),
    ("2020-01-27", "Helado", 4),
    ("2020-01-27", "Galletitas", 5),
    ("2020-01-28", "Cafe con leche", 1),
    ("2020-01-28", "Pollo al horno", 2),
    ("2020-01-28", "Pizza", 3),
    ("2020-01-28", "Flan", 4),
    ("2020-01-28", "Galletitas", 5),
    ("2020-01-29", "Huevos revueltos", 1),
    ("2020-01-29", "Milanesa con pure", 2),
    ("2020-01-29", "Tarta de jamon y queso", 3),
    ("2020-01-29", "Helado", 4),
    ("2020-01-29", "Galletitas", 5),
    ("2020-01-30", "Cafe con leche", 1),
    ("2020-01-30", "Pollo al horno", 2),
    ("2020-01-30", "Pizza", 3),
    ("2020-01-30", "Flan", 4),
    ("2020-01-30", "Galletitas", 5),
    ("2020-01-31", "Cafe con leche", 1),
    ("2020-01-31", "Milanesa con pure", 2),
    ("2020-01-31", "Tarta de jamon y queso", 3),
    ("2020-01-31", "Helado", 4),
    ("2020-01-31", "Galletitas", 5),
]


# insertar datos en la tabla de comidas
def insertar_comidas():
    conn = sqlite3.connect("db.sqlite3")
    cursor = conn.cursor()
    for comida in comidas:
        fecha = comida[0]
        nombre = comida[1]
        tipo = comida[2]
        cursor.execute(
            "INSERT INTO gustos_comida (fecha, nombre, tipo_id) VALUES (?, ?, ?)", (fecha, nombre, tipo))
        conn.commit()
    conn.close()


def insertar_comidas_if_empty():
    conn = sqlite3.connect("db.sqlite3")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM gustos_comida")
    if cursor.fetchone() is None:
        insertar_comidas()
    conn.close()


def debug():
    # print id de los tipos de comida insertados
    print("Tipos de comida insertados:")
    conn = sqlite3.connect("db.sqlite3")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM gustos_tipo_comida")
    for row in cursor.fetchall():
        print(row)
    conn.close()


insertar_tipos_comida_if_empty()
insertar_comidas_if_empty()
debug()
