**Componente DB NoSQL - Registro Citas**

* Tipo de componente: Base de Datos
* Nombre: citas-medicas-db
* Paradigma: NoSQL (Orientado a Documentos)
* Sistema de Gestión de Base de Datos: Firestore
* Descripción: Base de datos NoSQL para guardar el registro de las citas médicas programadas.

Ejemplo Registro:

```json
{
    "id": "cita-123",
    "details": {
        "nombre_medico": "Luis",
        "nombre_paciente": "Lina",
        "id_medico":"202",
        "id_paciente":"5089",
        "fecha":"31/10/2024",
        "hora":"5:00 pm",
        "especialidad":"cardiologia"
    }
}
```
Ejemplo registro en GCP Firestore
![image](https://github.com/user-attachments/assets/31bf2915-a795-49ba-9ebe-f5945737f023)

**Componente Microservicio - Registro Citas Médicas**

* Tipo de componente: Lógico (microservicio) - FaaS (Function as a Service)
* Nombre: citas-medicas-ms
* Lenguaje de Programación: Python
* Descripción: Microservicio (POST) para generar registro de citas médicas en la db NoSQL citas-medicas-db.

  URL: https://us-east4-cbse-2024ii-438603.cloudfunctions.net/citas-medicas-ms

![image](https://github.com/user-attachments/assets/b952cbe1-dcca-4e2f-86d6-84d95225816d)

**Componente DB SQL - Registro Usuarios**

* Tipo de componente: Base de Datos
* Nombre: med-users-db
* Paradigma: SQL (relacional)
* Sistema de Gestión de Base de Datos: GCP SQL
* Descripción: Base de datos SQL para guardar la información de identificación de los pacientes.

Ejemplo Registro:

```json
{
    "paciente_tipo_id" : "1",
    "paciente_id" : "52123",
    "name": "Adriana",
    "email": "agonzalez@unal.edu.co@unal.edu.co",
    "fecha_nacimiento" : "1979/01/01",
    "eps" : "2"
}
```
Ejemplo registro en GCP SQL

![image](https://github.com/user-attachments/assets/4f34567e-712f-4d53-935f-edd9f44eff26)

**Componente Imagen de microservicio en Registry - Registro Pacientes**

* Repositorio: telemed
* Microservicio : med-paciente-ms
* Descripción: Repositorio con la imagen del microservicio para guardar los datos del paciente

  us-east4-docker.pkg.dev/cbse-2024ii-438404/telemed
  
![image](https://github.com/user-attachments/assets/22d77bd0-8a68-4254-a8d5-cc497fa79ce9)

**Componente Servicio en Cloud Run**
* Servicio: med-paciente-ms
* url: https://med-paciente-ms-222710232023.us-east4.run.app
* Descripción: Servicio para ejecutar el contenedor del microservicio que guarda los datos del paciente
  
![image](https://github.com/user-attachments/assets/5c344b02-3cff-4fbf-8c28-325fdcb119e9)




