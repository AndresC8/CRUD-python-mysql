import pymysql

class Conexion:
    def __init__(self):
        try:
            self.conexion = pymysql.connect(
            host='localhost',
            db='test_db',
            passwd='admin',
            port=3306,
            user='root'
            )
            self.cursor = self.conexion.cursor()
        except Exception as e:
            print(f'Ha habido un error: {e}')
    def agregarRegistro(self, datos_registro):
        query = 'INSERT INTO persona (nombre, apellido, edad, pais, direccion, email) VALUES (%s, %s, %s, %s, %s, %s)'
        self.cursor.execute(query, datos_registro)
        self.conexion.commit()

    def eliminarRegistro(self, registro_eliminar):
        query = 'DELETE FROM persona WHERE id_persona = %s'
        self.cursor.execute(query, (registro_eliminar,))
        self.conexion.commit()

    def mostrarRegistros(self):
        query = 'SELECT * FROM persona'
        self.cursor.execute(query)
        resultados = self.cursor.fetchall()
        for fila in resultados:
            id_persona, nombre, apellido, edad, pais, direccion, email = fila
            print(f'ID: {id_persona}, Nombre: {nombre}, Apellido: {apellido}, Edad: {edad}, Pais: {pais}, Direccion: {direccion}, Email: {email}')

    def actualizarRegistros(self, registro_actualizar, id_registro):
        query = 'UPDATE persona SET nombre = %s, apellido = %s, edad = %s, pais = %s, direccion = %s, email = %s WHERE id_persona = %s'
        valores_actualizar = (registro_actualizar + id_registro)
        self.cursor.execute(query, valores_actualizar)
        self.conexion.commit()

conexion = Conexion()
conexion.conexion.close()
