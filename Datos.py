class Datos:
    def __init__(self):
        self.id = ""
        self.nombre = ""
        self.apellido = ""
        self.sexo = ""
        self.contrasena = ""
        self.usuario = ""
        self.id_calificaciones = ""
        self.fk_id_alumnos = ""
        self.primer_examen = ""
        self.segundo_examen = ""
        self.tercer_examen = ""
        self.examen_final = ""
        self.promedio = ""

    # Métodos Getter
    def get_id(self):
        return self.id.get()

    def get_nombre(self):
        return self.nombre.get()

    def get_apellido(self):
        return self.apellido.get()
    
    def get_sexo(self):
        return self.sexo.get()

    def get_contrasena(self):
        return self.contrasena.get()

    def get_usuario(self):
        return self.usuario.get()

    def get_id_calificaciones(self):
        return self.id_calificaciones.get()

    def get_fk_id_alumnos(self):
        return self.fk_id_alumnos.get()

    def get_primer_examen(self):
        return self.primer_examen.get()

    def get_segundo_examen(self):
        return self.segundo_examen.get()

    def get_tercer_examen(self):
        return self.tercer_examen.get()

    def get_examen_final(self):
        return self.examen_final.get()

    def get_promedio(self):
        return self.promedio.get()

    # Métodos Setter
    def set_id(self, value):
        self.id.set(value)

    def set_nombre(self, value):
        self.nombre.set(value)

    def set_apellido(self, value):
        self.apellido.set(value)

    def set_sexo(self, value):
        self.sexo.set(value)

    def set_contrasena(self, value):
        self.contrasena.set(value)

    def set_usuario(self, value):
        self.usuario.set(value)

    def set_id_calificaciones(self, value):
        self.id_calificaciones.set(value)

    def set_fk_id_alumnos(self, value):
        self.fk_id_alumnos.set(value)

    def set_primer_examen(self, value):
        self.primer_examen.set(value)

    def set_segundo_examen(self, value):
        self.segundo_examen.set(value)

    def set_tercer_examen(self, value):
        self.tercer_examen.set(value)

    def set_examen_final(self, value):
        self.examen_final.set(value)

    def set_promedio(self, value):
        self.promedio.set(value)