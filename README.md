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


