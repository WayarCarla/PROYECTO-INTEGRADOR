class Propietario:
    
    Id_Propietario =""
    Nombre =""
    Apellido =""
    Direccion =""
    Telefono =""
    Email =""
    
    
    def __init__(self, Id_Propietario, Nombre, Apellido ,Direccion, Telefono, Email):
        self.Id_Propietario = Id_Propietario,
        self.Nombre = Nombre,
        self.Apellido = Apellido,
        self.Direccion = Direccion,
        self.Telefono = Telefono,
        self.Email = Email,
                
    def get_Id_Propietario(self):
        return Id_Propietario    

    def set_Id_Propietario(self):
        self.Id_Propietario= Id_Propietario
        
    def get_Nombre(self):
        return Nombre
    
    def set_Nombre(self):
        self.Nombre= Nombre
        
    def get_Apellido(self):
        return Apellido

    def set_Apellido(self):
        self.Apellido = Apellido

    def get_Direccion(self):
        return Direccion

    def set_Direccion(self):
        self.Direccion = Direccion

    def get_Telefono(self):
        return Telefono

    def set_Telefono(self):
        self.Telefono = Telefono
        

    def get_Email(self):
        return Email

    def set_Email(self):
        self.Email = Email    
