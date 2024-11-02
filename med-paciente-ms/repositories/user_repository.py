from models.paciente import Paciente, db

class UserRepository:

    @staticmethod
    def create_user_repository(paciente_tipo_id, paciente_id, name, email, fecha_nacimiento, eps):

        paciente = Paciente(paciente_tipo_id = paciente_tipo_id, paciente_id = paciente_id, name=name, email=email, fecha_nacimiento = fecha_nacimiento, eps=eps)
        
        db.session.add(paciente)
        db.session.commit()

        return paciente