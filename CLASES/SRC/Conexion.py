from multiprocessing import connection
import mysql.connector

try:
   connection=mysql.connector.connect(
    host='localhost',
    user='root',
    password='Michingo2022',
    db='electronics',
)
   if connection.is_connected():
       print("Conexion exitosa")
       info_server=connection.get_server_info()
       print(info_server)
except Exception as ex:
    print(ex)    

