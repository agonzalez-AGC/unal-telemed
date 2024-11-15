from flask import Blueprint, render_template, request, jsonify, redirect, url_for
from services.record_service import RecordService

record_api = Blueprint('record_api', __name__)

@record_api.route('/record', methods=['POST'])
def create_record():

    data = request.form
    paciente_tipo_id = data.get('paciente_tipo_id')
    paciente_id = data.get('paciente_id')
    paciente_name = data.get('paciente_name')
    paciente_email = data.get('paciente_email')
    paciente_fecha_nacimiento = data.get('paciente_fecha_nacimiento')
    paciente_eps = data.get('paciente_eps')
    cita_id = data.get('cita_id')
    cita_fecha = data.get('cita_fecha')
    cita_hora = data.get('cita_hora')
    cita_paciente_id = data.get('paciente_id')
    cita_paciente_nombre = data.get('paciente_name')
    cita_medico_id = data.get('cita_medico_id')
    cita_medico_nombre = data.get('cita_medico_nombre')
    cita_especialidad_id = data.get('cita_especialidad_id')
    cita_especialidad_des = data.get('cita_especialidad_des')

    if not paciente_name:
        return jsonify({'error': 'Nombre del paciente es obligatorio'}), 400

    if not cita_medico_nombre:
        return jsonify({'error': 'Nombre del médico es obligatorio'}), 400

    RecordService.create_record(paciente_tipo_id, paciente_id, paciente_name, paciente_email, paciente_fecha_nacimiento, 
                      paciente_eps, cita_id, cita_fecha, cita_hora, cita_paciente_id, cita_paciente_nombre,
                      cita_medico_id, cita_medico_nombre, cita_especialidad_id, cita_especialidad_des)
    return redirect(url_for('record_api.index'))

@record_api.route('/')
def index():
    return render_template('index.html')