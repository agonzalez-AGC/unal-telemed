import functions_framework

from google.cloud import firestore

db = firestore.Client(project="cbse-2024ii-438603", database="citas-medicas-db")

@functions_framework.http
def tasks_api(request):

    if request.method == 'POST':

        data = request.get_json()

        doc = db.collection("citas").document(data['id'])
        doc.set(data['details'])

    return 'Task with id={} created!'.format(data['id']), 201