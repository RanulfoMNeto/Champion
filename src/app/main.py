from utils import send_to_server
from parser import extract_champions
import requests

if __name__ == '__main__':

    # Define the path to the HTML file containing the champion data
    file_path = 'champions.html'
    base_url = 'https://u.gg/lol/champions'
    
    champions = extract_champions(file_path, base_url)
    
    # Define the URL of the server endpoint where data will be sent
    server_url = 'http://localhost:3000/api/champions'
    try:
        response = send_to_server(champions, server_url)
        # Response content for further inspection
        print(f"Server response: {response.text}")
    except requests.exceptions.RequestException:
        print("Failed to send data.")
