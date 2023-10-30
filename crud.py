from bd import Conexion


print("""
    Que deseas hacer
    1. Agregar registro
    2. Eliminar registro
    3. Mostrar registro
    4. Actualizar
""")
opcion = int(input('Ingresa la opcion: '))

if opcion == 1:
    print('Se va agregar un registro')
    nombre = input("Ingrese el nombre: ")
    apellido = input("Ingrese el apellido: ")
    edad = int(input("Ingrese la edad: "))  
    pais = input("Ingrese el país: ")
    direccion = input("Ingrese la dirección: ")
    email = input("Ingrese el correo electrónico: ")
    datos_registro = (
        nombre,
        apellido,
        edad,
        pais,
        direccion,
        email
    )
    conexion = Conexion()
    conexion.agregarRegistro(datos_registro)
elif opcion == 2:
    print('Se va eliminar un registro')
    registro_eliminar = int(input('ID del registro a eliminar: '))
    conexion = Conexion()
    conexion.eliminarRegistro(registro_eliminar)
elif opcion == 3:
    print('Se van a mostrar todos los registros: ')
    conexion = Conexion()
    conexion.mostrarRegistros()
elif opcion == 4:
    print('Se va actualizar un registro')
    nombre = input("Ingrese el nombre: ")
    apellido = input("Ingrese el apellido: ")
    edad = int(input("Ingrese la edad: "))  
    pais = input("Ingrese el país: ")
    direccion = input("Ingrese la dirección: ")
    email = input('Ingresa el email: ')
    id_registro = int(input('Ingrese el Numero de registro a actualizar: '))
    registro_actualizar = (
        nombre,
        apellido,
        edad,
        pais,
        direccion,
        email,
    )
    id_registro = (id_registro,)
    conexion = Conexion()
    conexion.actualizarRegistros(registro_actualizar, id_registro)
