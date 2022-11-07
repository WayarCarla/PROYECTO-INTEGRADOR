import Modelo

def ListarPropiedades():
    con = Modelo.Conectar()
    listado = con.ListarPropiedades()
    print("\n LISTADO TOTAL DE INMUEBLES ")
    print("\n|Prop|Direccion Propiedad|       Localidad      |Provincia|Tipo Propiedad|")
    tot = 0
    for propiedad in listado:
        tot += 1
        print(" " ,propiedad[0]," " ,propiedad[1], "         " ,propiedad[2], "     " ,propiedad[3], " " ,propiedad[4])
    print("")
    input("Presione ENTER para continuar")
    print("")
    print("\n TOTAL DE INMUEBLES: ", tot)

def ListarPropiedadesDisponiblesVenta():
    con = Modelo.Conectar()
    listado = con.ListarPropiedadesDisponiblesVenta()
    print("\n LISTADO INMUEBLES DISPONIBLES PARA VENTA ")
    print("\n|Prop|Direccion Propiedad       | Estado   | Operatoria Comercial |")
    tot = 0
    for propiedad in listado:
        tot += 1
        print(" ",propiedad[0]," " ,propiedad[1], "       " ,propiedad[2], "   " ,propiedad[3])
        print("")
    print("")
    
    input("Presione ENTER para continuar")
    print("")
    print("\n TOTAL DE INMUEBLES PARA VENTA: ", tot)

def ListarPropiedadesDisponiblesAlquiler():
    con = Modelo.Conectar()
    listado = con.ListarPropiedadesDisponiblesAlquiler()
    print("\n LISTADO INMUEBLES DISPONIBLES PARA ALQUILAR ")
    print("\n|Prop|Direccion Propiedad| Estado   | Operatoria Comercial |")
    tot = 0
    for propiedad in listado:
        tot += 1
        print(" ",propiedad[0]," " ,propiedad[1], "       " ,propiedad[2], "   " ,propiedad[3])
    print("")
    input("Presione ENTER para continuar")
    print("")
    print("\n TOTAL DE INMUEBLES PARA ALQUILAR: ", tot)

def ListarPropiedadesVendidas():
    con = Modelo.Conectar()
    listado = con.ListarPropiedadesVendidas()
    print("\n LISTADO INMUEBLES VENDIDOS ")
    print("\n|Prop|Direccion Propiedad| Estado   | Operatoria Comercial |")
    tot = 0
    for propiedad in listado:
        tot += 1
        print(" ",propiedad[0]," " ,propiedad[1], "       " ,propiedad[2], "   " ,propiedad[3])
    print("")
    input("Presione ENTER para continuar")
    print("")
    print("\n TOTAL DE INMUEBLES VENDIDOS: ", tot)

def ListarPropiedadesAlquiladas():
    con = Modelo.Conectar()
    listado = con.ListarPropiedadesAlquiladas()
    print("\n LISTADO INMUEBLES ALQUILADOS ")
    print("\n|Prop|Direccion Propiedad       | Estado   | Operatoria Comercial |")
    tot = 0
    for propiedad in listado:
        tot += 1
        print(" ",propiedad[0]," " ,propiedad[1], "       " ,propiedad[2], "   " ,propiedad[3])
    print("")
    input("Presione ENTER para continuar")
    print("")
    print("\n TOTAL DE INMUEBLES ALQUILADOS: ", tot)
    
def ListarTipoPropiedad():
    con = Modelo.Conectar()
    listado = con.ListarTipoPropiedad
    print("\n LISTADO TIPOS DE PROPIEDADES ")
    print("\n| Tipo Propiedad |Descripcion Tipo       |")
    for propiedad in listado:
        print(" " ,propiedad[0],"   " ,propiedad[1])
    print("")
    input("Presione ENTER para continuar")

#def ListarOperatoriaComercial():
#    con = Modelo.Conectar()
#    listado = con.ListarOperatoriaComercial
#    print("\n LISTADO OPERATORIAS COMERCIALES ")
#    print("\n| Id Oper Comer | Descripcion Operatoria       |")
#    for propiedad in listado:
#        print(" " ,propiedad[0],"   " ,propiedad[1])
#    print("")
#    input("Presione ENTER para continuar")

def ListarPropietarios():
    con = Modelo.Conectar()
    listado = con.ListarPropietarios
    print("\n LISTADO DE PROPIETARIOS ")
    print("\n| Id Propietario | Nombre de Popietario       |")
    for propiedad in listado:
        print(" " ,propiedad[0],"   " ,propiedad[1])
    print("")
    input("Presione ENTER para continuar")
        
    
def InsertarPropiedad():
    con = Modelo.Conectar()

    print("\nTipo de Propiedades:")

    for i in con.ListarTipoPropiedad():
        print(i)    
    Id_Tipo = int(input("\nIngrese el Tipo de Propiedad: "))

    Id_Estado = int(input("\nIngrese Estado entre 1 y 2: "))

    print("\nTipo de Operaciones Comerciales:")
#               for i in con.ListarOperatoriaComercial():
#                   print(i)    
    Id_Operacion_Comercial = int(input("\nIngrese el Tipo de Operatoria Comercial 1 o 2: "))

    print("\nListado de Propietarios :")
#               for f in con.ListarPropietarios():
#                   print(f)    
    Id_Propietario = int(input("\nIngrese el Id. de Propietario entre 1 y 4: "))

    Direccion_Propiedad = input("\nIngrese Direccion de la Propiedad: ")

    Localidad = input("\nIngrese Localidad de la Propiedad: ")
    Provincia = input("\nIngrese Provincia de la Propiedad: ")
    
    print()
    input("Presione EL ENTER1 para continuar")
    print()

    
    nuevaPropiedad = Modelo.propiedad(0,Id_Tipo, Id_Estado, Id_Operacion_Comercial, Id_Propietario, Direccion_Propiedad, Localidad, Provincia)
    print(nuevaPropiedad)
    con.InsertarPropiedad(nuevaPropiedad)    

    print()
    input("Presione EL ENTER2 para continuar")
    print(" ")

       
def EliminarPropiedad():
    ListarPropiedades()
    Id_Propiedad = int(input("\nIngrese el Id de Propiedad a ELIMINAR: "))
    
    Modelo.Conectar.EliminarPropiedad(Id_Propiedad)
    input("Presione ENTER para continuar")
    print(" ")

    
def ActualizarPropiedad():
    ListarPropiedades()
    Id_Propiedad = int(input("\nIngrese el Id de Propiedad a Actualizar: "))
    
#    Modelo.Conectar.ActualizarPropiedad(Id_Propiedad)
#    input("Presione ENTER para continuar")
    print(" ")