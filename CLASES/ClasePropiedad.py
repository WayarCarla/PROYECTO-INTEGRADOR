class Propiedad():
    def __init__(self, Id_Propiedad, Id_Tipo, Id_Estado, Id_Operacion_Comercial, Id_Propietario, Direccion_Propiedad, Localidad, Provincia):
        self.Id_Propiedad = Id_Propiedad
        self.Id_Tipo = Id_Tipo
        self.Id_Estado = Id_Estado
        self.Id_Operacion_Comercial = Id_Operacion_Comercial
        self.Id_Propietario = Id_Propietario
        self.Direccion_Propiedad = Direccion_Propiedad        
        self.Localidad = Localidad
        self.Provincia = Provincia

    def get_Id_Propiedad(self):
        return self.Id_Propiedad
    def get_Id_Tipo(self):
        return self.Id_Tipo
    def get_Id_Estado(self):
        return self.Id_Estado
    def get_Id_Operacion_Comercial(self):
        return self.Id_Operacion_Comercial
    def get_Id_Propietario(self):
        return self.Id_Propietario
    def get_Direccion_Propiedad(self):
        return self.Direccion_Propiedad
    def get_Localidad(self):
        return self.Localidad
    def get_Provincia(self):
        return self.Provincia

    def set_Id_Propiedad(self,Id_Propiedad):
        self.Id_Propiedad = Id_Propiedad
    def set_Id_Tipo(self, Id_Tipo):
        self.Id_Tipo = Id_Tipo
    def set_Id_Estado(self, Id_Estado):
        self.Id_Estado = Id_Estado
    def set_Id_Operacion_Comercial(self, Id_Operacion_Comercial):
        self.Id_Operacion_Comercial = Id_Operacion_Comercial
    def set_Id_Propietario(self, Id_Propietario):
        self.Id_Propietario = Id_Propietario
    def set_Direccion_Propiedad(self, Direccion_Propiedad):
        self.Direccion_Propiedad = Direccion_Propiedad
    def set_Localidad(self, Localidad):
        self.Localidad = Localidad
    def set_Provincia(self, Provincia):
        self.Provincia = Provincia

    def __str__(self) -> str:
        return str(self.get_Id_Propiedad) + ' ' + str(self.Id_Tipo) +' ' + str(self.Id_Estado) +' ' + str(self.Id_Operacion_Comercial) +' ' + str(self.Id_Propietario) +' ' + str(self.Direccion_Propiedad) +' ' + str(self.Localidad) +' ' + str(self.Provincia)
