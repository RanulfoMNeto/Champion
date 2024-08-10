import requests

# utils.py
def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def send_to_server(data):
    url = 'http://example.com/api/dataset'
    response = requests.post(url, json=data)
    print(response.status_code, response.reason)