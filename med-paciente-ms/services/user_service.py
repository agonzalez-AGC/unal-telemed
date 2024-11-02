from repositories.user_repository import UserRepository

class UserService:
    
    @staticmethod
    def create_user_service(data):

        paciente_tipo_id = data['paciente_tipo_id']
        paciente_id = data['paciente_id']
        name = data['name']
        email = data['email']
        fecha_nacimiento = data['fecha_nacimiento']
        eps = data['eps']

        return UserRepository.create_user_repository(paciente_tipo_id, paciente_id, name, email, fecha_nacimiento, eps)
