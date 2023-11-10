import requests
from time import sleep
import json


ip_details = {}
def get_location():
    ip_address = "" 
    api_key = "API_KEY_HERE"
    response = requests.get(f'https://geo.ipify.org/api/v2/country?apiKey={api_key}&ipAddress={ip_address}').json()
    with open('t2.txt', 'r') as infile:
        fil = infile.readlines()
    for f in range(len(fil)):
        ip_address =  str(fil[f].strip())
        print(f"{f+1} - Getting IP {ip_address}")
        location_data = {
            "ip": ip_address,
            "location": response.get("location") 
        }
        
        ip_details.update({f+1 : location_data})
        sleep(1.5)
    
    with open('ips_detail.json', 'w', encoding='utf-8') as infil:
        json.dump(ip_details, infil)
        



get_location()
print(ip_details)
