from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Paciente(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    paciente_tipo_id = db.Column(db.String(2), nullable=False)
    paciente_id = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    fecha_nacimiento = db.Column(db.Date  , nullable=False)
    eps = db.Column(db.String(100), nullable=False)
