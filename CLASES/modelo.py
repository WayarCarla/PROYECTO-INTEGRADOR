class Propiedad:


    id_propietario = ""
    LOCALIDAD = ""
    PROVINCIA = ""

    def __init__(self, id_propietario, LOCALIDAD, PROVINCIA):
        self.id_propietario = id_propietario,
        self.LOCALIDAD= LOCALIDAD,
        self.PROVINCIA = PROVINCIA

    def get_id_propietario(self):
        return id_propietario

    def set_id_propietario(self, Nombre):
        self.id_propietario = id_propietario

    def get_LOCALIDAD(self):
        return LOCALIDAD

    def set_LOCALIDAD(self, Direccion):
        self.LOCALIDAD = LOCALIDAD

    def get_PROVINCIA(self):
        return PROVINCIA

    def set_PROVINCIA(self, Contacto):
        self.PROVINCIA = PROVINCIA
        

    def _str(self):
        print('ID DEL PROPIETARIO'+self.Propiedad)
        print('LOCALIDAD'+self.Propiedad)
        print ('PROVINCIA'+self.Propiedad)