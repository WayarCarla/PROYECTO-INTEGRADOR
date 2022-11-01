import mysql.connector

class Conectar():

    def __init__(self) -> None:
        try:
            self.conexion = mysql.connector.connect(
                host = 'localhost',
                port = 3306,
                user = 'root',
                password = 'PASSWORD',
                db = 'db_inm_brf'

            )
        except mysql.connector.Error as  descripcionError:
            print("¡ No se conecto a la Base de Datos",descripcionError)

# Listado de propiedades TOTALES, sin distinción de estados
            
    def ListarPropiedades(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute("SELECT * FROM propiedad")
                resultados = cursor.fetchall()
                self.conexion.close()
                print("MySQL connection is closed")
                return resultados
            except mysql.connector.Error as  descripcionError:
                print("¡ No se conecto a la Base de Datos",descripcionError)

                
con = Conectar()
print(con.ListarPropiedades())

con = Conectar()
for propiedad in con.ListarPropiedades():
    print(propiedad)

con = Conectar()
for propiedad in con.ListarPropiedades():
    print("Id_Propiedad: " ,propiedad[0], "Id_Tipo: " ,propiedad[1], "Id_Estado: " ,propiedad[2], "Id_Operacion_Comercial: " ,propiedad[3], "Id_Propietario: " ,propiedad[4], "Localidad: " ,propiedad[5], "Provincia: " ,propiedad[6])