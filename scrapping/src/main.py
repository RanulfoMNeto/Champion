import sched
import time
import requests
from utils import send_to_server
from parser import extract_champions

def periodically(scheduler, interval, file_path, base_url, server_url):
    """Extract champions and send them to the server."""
    champions = extract_champions(file_path, base_url)
    print(champions)
    try:
        response = send_to_server(champions, server_url)
        print(f"Server response: {response.text}")
    except requests.exceptions.RequestException:
        print("Failed to send data.")
    
    # Schedule the next call to this function
    scheduler.enter(interval, 1, periodically, (scheduler, interval, file_path, base_url, server_url))

if __name__ == '__main__':
    # Define the path to the HTML file containing the champion data
    file_path = 'champions.html'
    base_url = 'https://u.gg/lol/champions'
    
    # Define the URL of the server endpoint where data will be sent
    server_url = 'http://node:3000/api/champions'

    # Create a scheduler instance
    scheduler = sched.scheduler(time.time, time.sleep)

    # Define the interval in seconds at which you want to run the task
    interval = 1

    # Schedule the first call to the task
    scheduler.enter(0, 1, periodically, (scheduler, interval, file_path, base_url, server_url))
    
    # Start the scheduler
    scheduler.run()
