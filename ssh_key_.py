import os
import requests

# Отримуємо токен API з середовища
api_token = ('   ')
headers = {'Authorization': f'Bearer {api_token}', 'Content-Type': 'application/json'}

# Параметри для створення нового дроплета
droplet_data = {
    "name": "NewDroplet",
    "region": "nyc3",
    "size": "s-1vcpu-1gb",
    "image": "ubuntu-20-04-x64",
    "ssh_keys": [ssh_key_],  # Вкажіть ваш SSH-ключ
}

# Запит для створення дроплета
response = requests.post('https://api.digitalocean.com/v2/droplets', headers=headers, json=droplet_data)

if response.status_code == 202:
    droplet = response.json()['droplet']
    print(f"Droplet is being created. ID: {droplet['id']}")
else:
    print(f"Error: {response.status_code}")
    print(response.text)
