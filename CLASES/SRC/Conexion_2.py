import mysql.connector

class Conectar():

    def _init_(self) -> None:
        try:
            self.conexion = mysql.connector.connect(
                host = 'localhost',
                port = 3306,
                user = 'root',
                password = 'Michingo2022',
                db = 'db_inm_brf'

            )
        except mysql.connector.Error as  descripcionError:
            print("¡ No se conecto a la Base de Datos",descripcionError)

        finally:
            if self.conexion.is_connected():
                self.conexion.close()
    print("MySQL connection is closed")