import controlador

while True:
    print("===============================================")
    print("|                INMOBILIARIA                 |") 
    print("|            BIENES RAICES FUTURE             |")
    print("===============================================")
    print("")
    print("============== MENÚ PRINCIPAL =================")
    print("|  1 - INGRESAR PROPIEDAD                     |")
    print("|  2 - MODIFICAR PROPIEDAD                    |")
    print("|  3 - ELIMINAR PROPIEDAD                     |")
    print("|  4 - LISTADO DE PROPIEDADES                 |")
    print("|  5 - PROPIEDADES DISPONIBLES PARA VENTA     |")
    print("|  6 - PROPIEDADES DISPONIBLES PARA ALQUILER| |")
    print("|  7 - PROPIEDADES VENDIDAS                   |")
    print("|  8 - PROPIEDADES ALQUILADAS                 |")
    print("|  9 - SALIR                                  |")
    print("===============================================")

    print("")
    opcion = int(input("Seleccione una opción: "))
    
    if opcion == 1:
       controlador.InsertarPropiedad()
       
    elif opcion == 2:  
        controlador.ActualizarPropiedad()

    elif opcion == 3:
        controlador.EliminarPropiedad()

    elif opcion == 4:  
        controlador.ListarPropiedades()

    elif opcion == 5:
        controlador.ListarPropiedadesDisponiblesVenta()

    elif opcion == 6:
        controlador.ListarPropiedadesDisponiblesAlquiler()

    elif opcion == 7:
        controlador.ListarPropiedadesVendidas()

    elif opcion == 8:
        controlador.ListarPropiedadesAlquiladas()
 
    elif opcion == 9:
        print("")
        print("===============================================")
        print("===== ¡GRACIAS POR USAR NUESTRO SISTEMA! ======")
        print("===============================================")
        print("")
        break

    else:
            print("Opcion incorrecta, seleccionar entre 1 y 9.")
            print("")
            print("Ingrese nuevamente...")
            print("")