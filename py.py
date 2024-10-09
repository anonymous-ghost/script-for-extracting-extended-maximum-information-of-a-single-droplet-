import os
import requests
import csv
#Напишіть скрипт для отримання розгорнутої максимальної інформації  існуючого дроплета

api_token = ('api_token')  
if not api_token:
    print("Error: API token is missing.")
    exit(1)

headers = {'Authorization': f'Bearer {api_token}'}


response = requests.get('https://api.digitalocean.com/v2/droplets', headers=headers)

if response.status_code == 200:
    droplets = response.json().get('droplets', [])
    if droplets:
        print("Available Droplets:")
        
        with open('droplets_info.csv', mode='w', newline='') as csv_file:
            fieldnames = ['ID', 'Name', 'IP Address', 'Status', 'Region', 'CPU', 'RAM', 'Disk', 'Size']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            
            writer.writeheader()  
            
            for droplet in droplets:
                ip_address = droplet['networks']['v4'][0]['ip_address'] if droplet['networks'].get('v4') else "Not Assigned"
                droplet_info = {
                    'ID': droplet['id'],
                    'Name': droplet['name'],
                    'IP Address': ip_address,
                    'Status': droplet['status'],
                    'Region': droplet['region']['name'],
                    'CPU': droplet['vcpus'],
                    'RAM': droplet['memory'],
                    'Disk': droplet['disk'],
                    'Size': droplet['size']['slug'],
                }
                writer.writerow(droplet_info)  
                
                
                print(f"ID: {droplet['id']} Name: {droplet['name']} IP: {ip_address}")
        
        print("Droplet information exported to droplets_info.csv.")
    else:
        print("No droplets found.")
else:
    print(f"Error: {response.status_code}")
    print(response.text)
