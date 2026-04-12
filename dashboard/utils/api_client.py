import requests

def scan_file(file):

    return requests.post("http://localhost:8000/scan", files=file)