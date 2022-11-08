import mysql.connector
from tkinter import ttk
import tkinter as tk

class propiedad: 
    def __init__(self) -> None:
        try:
            self.conexion = mysql.connector.connect(
                host = 'localhost',
                port = 3306,
                user = 'sqluser',
                password = 'password',
                db = 'db_inm_brf'             
            )
        except mysql.connector.Error as  descripcionError:
            print("¡ No se conecto a la Base de Datos",descripcionError)
    def __str__(self):
        datos=self.consulta_propiedades()
        aux=""
        for row in datos:
            aux = aux + str (row) + "\n"
        return aux
    
    def consulta_propiedades(self):
        cur = self.conexion.cursor()
        cur.execute("SELECT * from propiedad")
        datos = cur.fetchall()
        cur.close()
        return datos
    
    def buscar_propiedades(self, Id_Estado):
        cur = self.conexion.cursor()
        sql = "SELECT * FROM Propiedad WHERE Id_Estado = {}".format(Id_Estado)
        cur.execute(sql)
        datos = cur.fetchone()
        cur.close()
        return datos
    def listarPropiedades(self):
        my_w=tk.Tk()
        my_w.geometry("700x900")
        my_w.title(" PROPIEDADES ")
        trv = ttk.Treeview(my_w,selectmode='browse')
        trv.grid(row=1,column=1)
        trv["columns"] = ("1","2","3","4","5","6","7","8")
        trv['show']='headings'
        trv.column("1",width=30,anchor='c')
        trv.column("2",width=60,anchor='c')
        trv.column("3",width=60,anchor='c')
        trv.column("4",width=70,anchor='c')
        trv.column("5",width=80,anchor='c')
        trv.column("6",width=80,anchor='c')
        trv.column("7",width=80,anchor='c')
        trv.column("8",width=80,anchor='c')
        trv.heading("1",text='ID')
        trv.heading("2",text='TIPO')
        trv.heading("3",text='ESTADO')
        trv.heading("4",text='OP-COMERCIAL')
        trv.heading("5",text='ID-PROPIETARIO')
        trv.heading("6",text='DIRECCION')
        trv.heading("7",text='LOCALIDAD')
        trv.heading("8",text='PROVINCIA')
        cur=self.conexion.cursor()
        sql = ("select pr.Id_Propiedad, pr.Direccion_Propiedad, pr.Localidad, pr.Provincia, ti.Nombre_Tipo from db_inm_brf.`Propiedad` as pr inner join db_inm_brf.`tipo` as ti on  pr.Id_Tipo = ti.Id_Tipo order by pr.Id_Propiedad")
        cur.execute(sql)
        for dt in cur:
            trv.insert("",'end',text=dt[0], values=(dt[0],dt[1],dt[2],dt[3],dt[4],dt[5],dt[6],dt[7]))
        cur.close()

    def listarPropiedadesventa(self):
        my_w=tk.Tk()
        my_w.geometry("600x600")
        my_w.title(" PROPIEDADES PARA LA VENTA")
        trv = ttk.Treeview(my_w,selectmode='browse')
        trv.grid(row=1,column=1)
        trv["columns"] = ("1","2","3","4","5","6","7","8")
        trv['show']='headings'
        trv.column("1",width=30,anchor='c')
        trv.column("2",width=60,anchor='c')
        trv.column("3",width=60,anchor='c')
        trv.column("4",width=70,anchor='c')
        trv.column("5",width=80,anchor='c')
        trv.column("6",width=80,anchor='c')
        trv.column("7",width=80,anchor='c')
        trv.column("8",width=80,anchor='c')
        trv.heading("1",text='ID')
        trv.heading("2",text='TIPO')
        trv.heading("3",text='ESTADO')
        trv.heading("4",text='OP-COMERCIAL')
        trv.heading("5",text='ID-PROPIETARIO')
        trv.heading("6",text='DIRECCION')
        trv.heading("7",text='LOCALIDAD')
        trv.heading("8",text='PROVINCIA')
        cur=self.conexion.cursor()
        cur.execute("SELECT * from Propiedad WHERE Id_Estado = 1 AND Id_Operacion_Comercial = 1")
        for dt in cur:
            trv.insert("",'end',text=dt[0], values=(dt[0],dt[1],dt[2],dt[3],dt[4],dt[5],dt[6],dt[7]))
        cur.close()

    def listarPropiedadesalquiler(self):
        my_w=tk.Tk()
        my_w.geometry("600x600")
        my_w.title("PROPIEDADES DISPONIBLES PARA ALQUILER")
        trv = ttk.Treeview(my_w,selectmode='browse')
        trv.grid(row=1,column=1)
        trv["columns"] = ("1","2","3","4","5","6","7","8")
        trv['show']='headings'
        trv.column("1",width=30,anchor='c')
        trv.column("2",width=60,anchor='c')
        trv.column("3",width=60,anchor='c')
        trv.column("4",width=70,anchor='c')
        trv.column("5",width=80,anchor='c')
        trv.column("6",width=80,anchor='c')
        trv.column("7",width=80,anchor='c')
        trv.column("8",width=80,anchor='c')
        trv.heading("1",text='ID')
        trv.heading("2",text='TIPO')
        trv.heading("3",text='ESTADO')
        trv.heading("4",text='OP-COMERCIAL')
        trv.heading("5",text='ID-PROPIETARIO')
        trv.heading("6",text='DIRECCION')
        trv.heading("7",text='LOCALIDAD')
        trv.heading("8",text='PROVINCIA')
        cur=self.conexion.cursor()
        sql = ("SELECT * from Propiedad WHERE Id_Estado=1 AND Id_Operacion_Comercial = 2")
        cur.execute(sql)
        for dt in cur:
            trv.insert("",'end',text=dt[0], values=(dt[0],dt[1],dt[2],dt[3],dt[4],dt[5],dt[6],dt[7]))
        cur.close()

    def listarPropiedadesvendidas(self):
        my_w=tk.Tk()
        my_w.geometry("600x600")
        my_w.title(" PROPIEDADES VENDIDAS")
        trv = ttk.Treeview(my_w,selectmode='browse')
        trv.grid(row=1,column=1)
        trv["columns"] = ("1","2","3","4","5","6","7","8")
        trv['show']='headings'
        trv.column("1",width=30,anchor='c')
        trv.column("2",width=60,anchor='c')
        trv.column("3",width=60,anchor='c')
        trv.column("4",width=70,anchor='c')
        trv.column("5",width=80,anchor='c')
        trv.column("6",width=80,anchor='c')
        trv.column("7",width=80,anchor='c')
        trv.column("8",width=80,anchor='c')
        trv.heading("1",text='ID')
        trv.heading("2",text='TIPO')
        trv.heading("3",text='ESTADO')
        trv.heading("4",text='OP-COMERCIAL')
        trv.heading("5",text='ID-PROPIETARIO')
        trv.heading("6",text='DIRECCION')
        trv.heading("7",text='LOCALIDAD')
        trv.heading("8",text='PROVINCIA')
        cur=self.conexion.cursor()
        cur.execute("SELECT * from Propiedad WHERE Id_Estado=2 AND Id_Operacion_Comercial = 1")
        for dt in cur:
            trv.insert("",'end',text=dt[0], values=(dt[0],dt[1],dt[2],dt[3],dt[4],dt[5],dt[6],dt[7]))
        cur.close()
    
    def listarPropiedadesalquiladas(self):
        my_w=tk.Tk()
        my_w.geometry("600x600")
        my_w.title(" PROPIEDADES ALQUILADAS")
        trv = ttk.Treeview(my_w,selectmode='browse')
        trv.grid(row=1,column=1)
        trv["columns"] = ("1","2","3","4","5","6","7","8")
        trv['show']='headings'
        trv.column("1",width=30,anchor='c')
        trv.column("2",width=60,anchor='c')
        trv.column("3",width=60,anchor='c')
        trv.column("4",width=70,anchor='c')
        trv.column("5",width=80,anchor='c')
        trv.column("6",width=80,anchor='c')
        trv.column("7",width=80,anchor='c')
        trv.column("8",width=80,anchor='c')
        trv.heading("1",text='ID')
        trv.heading("2",text='TIPO')
        trv.heading("3",text='ESTADO')
        trv.heading("4",text='OP-COMERCIAL')
        trv.heading("5",text='ID-PROPIETARIO')
        trv.heading("6",text='DIRECCION')
        trv.heading("7",text='LOCALIDAD')
        trv.heading("8",text='PROVINCIA')
        cur=self.conexion.cursor()
        cur.execute("SELECT * from Propiedad WHERE Id_Estado=2 AND Id_Operacion_Comercial = 2")
        for dt in cur:
            trv.insert("",'end',text=dt[0], values=(dt[0],dt[1],dt[2],dt[3],dt[4],dt[5],dt[6],dt[7]))
        cur.close()
    
    def inserta_propiedad(self,Id_Tipo,Id_Estado,Id_Operacion_Comercial,Id_Propietario,Direccion_Propiedad, Localidad, Provincia):
        cur = self.conexion.cursor()
        sql = '''INSERT INTO propiedad (Id_Tipo,Id_Estado,Id_Operacion_Comercial,Id_Propietario,Direccion_Propiedad, Localidad,Provincia) VALUES ('{}','{}','{}','{}','{}','{}','{}')'''.format(Id_Tipo,Id_Estado,Id_Operacion_Comercial,Id_Propietario, Direccion_Propiedad, Localidad,Provincia)
        cur.execute(sql)
        n=cur.rowcount
        self.conexion.commit()
        cur.close()
        return n

    def elimina_propiedad(self,Id_Propiedad):
        cur = self.conexion.cursor()
        sql = '''DELETE FROM propiedad WHERE Id_Propiedad = {}'''.format(Id_Propiedad)
        cur.execute(sql)
        n=cur.rowcount
        self.conexion.commit()
        cur.close()
        return n
     
    def modifica_propiedad(self,Id_Propiedad,Id_Tipo,Id_Estado,Id_Operacion_Comercial,Id_Propietario,Direccion_Propiedad, Localidad, Provincia):
        cur = self.conexion.cursor()
        sql = '''UPDATE Propiedad SET Id_Tipo='{}', Id_Estado='{}',Id_Operacion_Comercial='{}',Id_Propietario='{}',Direccion_Propiedad='{}',Localidad='{}',Provincia='{}' WHERE Id_Propiedad={}'''.format(Id_Propiedad,Id_Tipo,Id_Estado,Id_Operacion_Comercial,Id_Propietario, Direccion_Propiedad, Localidad, Provincia)
        cur.execute(sql)
        n=cur.rowcount
        self.conexion.commit()
        cur.close()
        return n




