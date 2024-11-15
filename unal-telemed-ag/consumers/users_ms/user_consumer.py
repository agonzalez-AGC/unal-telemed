import requests

from config import ISBN_USERS_MS_API_URL

base_url = ISBN_USERS_MS_API_URL

# Create User
def create_user(data):

    url = base_url + '/api/user'

    # Imprimir la variable base_url en la terminal
    print(f"Base URL: {base_url}")
    
    response = requests.post(url, json=data)

    return response