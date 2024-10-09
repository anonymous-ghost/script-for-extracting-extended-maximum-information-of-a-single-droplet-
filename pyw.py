import os
import requests
import sys

# Скрипт для виведення інформації про використання ресурсів (CPU, RAM)
api_token = (' ')
headers = {'Authorization': f'Bearer {api_token}'}

# Перевіряємо, чи передано аргумент з ID дроплета
if len(sys.argv) < 2:
    print("Usage: python get_droplet_resources.py <droplet_id>")
    sys.exit(1)

# Задаємо ID дроплета
droplet_id = sys.argv[1]

# Запит для отримання використання ресурсів
response = requests.get(f'https://api.digitalocean.com/v2/droplets/{droplet_id}/metrics', headers=headers)

if response.status_code == 200:
    metrics = response.json()['metrics']
    print(f"CPU Usage: {metrics['cpu_usage']}%")
    print(f"RAM Usage: {metrics['memory_usage']}MB")
else:
    print(f"Error: {response.status_code}")
    print(response.text)
