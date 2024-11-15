from consumers.users_ms.user_consumer import *
from consumers.tasks_ms.task_consumer import *

class RecordService:

    @staticmethod
    def create_record_service(data):

        user_data = {
            "paciente_tipo_id": data['paciente_tipo_id'],
            "paciente_id": data['paciente_id'],
            "name": data['paciente_name'],
            "email": data['paciente_email'],
            "fecha_nacimiento": data['paciente_fecha_nacimiento'],
            "eps": data['paciente_eps']
        }


        user = create_user(user_data)

        if user.status_code == 201:
             
            user_id = user.json().get("user_id")  

            task_data = {
                "id": data['cita_id'],
                "details":{
                    "fecha": data['cita_fecha'],
                    "hora": data['cita_hora'],
                    "paciente_id": data['cita_paciente_id'],
                    "paciente_nombre": data['cita_paciente_nombre'],
                    "medico_id": data['cita_medico_id'],
                    "medico_nombre": data['cita_medico_nombre'],
                    "especialidad_id": data['cita_especialidad_id'],
                    "especialidad_des": data['cita_especialidad_des'],
                    "id": user_id #"1"
                }
            }

            task = create_task(task_data)

            if task.status_code == 201:

                return True

            return False