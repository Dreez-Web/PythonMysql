import mysql.connector

class CConexion:
    
    def ConexionBaseDeDatos():
        try:
            conexion = mysql.connector.connect(
                user='root',
                password='andres',
                host='localhost',
                database='clientesdb',
                port='3306'
            )
            print("Conexion exitosa")
            return conexion
        
        except mysql.connector.Error as error:
            print("Error al conectarse a la base de datos {}".format(error))
            return conexion
        
    ConexionBaseDeDatos()