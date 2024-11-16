from Conexion import *

class CCleintes:
    
    def ingresarclientes(nombres,apellidos,sexo):
        
        try:
            cone = CConexion.ConexionBaseDeDatos()
            cursor = cone.cursor()
            sql = "insert into usuarios values(null,%s,%s,%s);"
                #La variable valores tiene que ser una tupla
                #Como minina expresion es: (valor,) La coma hace que sea una tupla
                #Las tuplas son listas inmutables.
                
            valores = (nombres,apellidos,sexo)
            cursor.execute(sql,valores)
            cone.commit()
            print(cursor.rowcount,"Registro ingresado")
            cone.close()
            
        except mysql.connector.Error as error:
            print("Error de ingreso de datos{}".format(error))