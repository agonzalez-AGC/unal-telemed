from consumers.ag.record_consumer import *

class RecordService:

    @staticmethod
    def create_record(paciente_tipo_id, paciente_id, paciente_name, paciente_email, paciente_fecha_nacimiento, 
                      paciente_eps, cita_id, cita_fecha, cita_hora, cita_paciente_id, cita_paciente_nombre,
                      cita_medico_id, cita_medico_nombre, cita_especialidad_id, cita_especialidad_des
                     ):

        data = {
            "paciente_tipo_id" : paciente_tipo_id,
            "paciente_id" : paciente_id,
            "paciente_name": paciente_name,
            "paciente_email": paciente_email,
            "paciente_fecha_nacimiento" : paciente_fecha_nacimiento,
            "paciente_eps" : paciente_eps,   "cita_id": cita_id,
            "cita_fecha":cita_fecha,
            "cita_hora":cita_hora,
            "cita_paciente_id" : cita_paciente_id,
            "cita_paciente_nombre": cita_paciente_nombre,
            "cita_medico_id":cita_medico_id,    
            "cita_medico_nombre": cita_medico_nombre,
            "cita_especialidad_id" : cita_especialidad_id,    
            "cita_especialidad_des":cita_especialidad_des
        }

        return create_record(data)