import pyzxing as pyx
import requests
import json

def file_to_barcode(file):
    read = pyx.BarCodeReader()
    result = read.decode(file)
    if "parsed" in result[0].keys():
        encoded = result[0]["parsed"]
        barcode = encoded.decode('utf-8')
        print(f"Got barcode {barcode}")
        return barcode
    else:
        return "Failed to read barcode"

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