import requests
import json
import subprocess

def file_to_barcode(file):
    try:
        result = subprocess.run(['zbarimg',file], capture_output=True, text=True, check=True)
        
        print(result)
        
        if result.stdout:
            barcode = result.stdout.split(':')[1][:-1]
            print(barcode)
            return barcode
        else:
            return None
    except subprocess.CalledProcessError as e:
        print(f"An error occured {e}")
        return None

def barcode_to_brand(barcode):
    if barcode == "Failed to read barcode":
        return barcode
    headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'Accept-Encoding': 'gzip,deflate',
    }

    resp = requests.get(f'https://api.upcitemdb.com/prod/trial/lookup?upc={barcode}', headers=headers)
    data = json.loads(resp.text)
    if "total" in list(data.keys()):
        if data['total'] == 0:
            return "Barcode read; Failed to find product"
        return data['items'][0]['brand']
    else:
        return "Invalid barcode"

def file_to_brand(file):
    return barcode_to_brand(file_to_barcode(file))