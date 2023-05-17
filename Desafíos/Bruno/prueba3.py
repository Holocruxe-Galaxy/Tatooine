import pymysql

# Establecer conexión
connection = pymysql.connect(
    host='holocruxe-ai-test-v1.cirkyideh48r.us-east-1.rds.amazonaws.com',
    user='admin_holocruxe',
    password='95900133',
    database='holocruxe_test_ai'
)

# Crear cursor
cursor = connection.cursor()

# Ejecutar consulta
cursor.execute("SELECT VERSION();")

# Obtener resultado
result = cursor.fetchone()

# Imprimir resultado
print(result)

# Cerrar cursor y conexión
cursor.close()
connection.close()