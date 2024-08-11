import requests

def read_file(file_path):
    """
    Reads the content of a file.

    Args:
        file_path (str): The path to the file to be read.

    Returns:
        str: The content of the file.
    """
    # Open the file specified by file_path in read mode with UTF-8 encoding
    with open(file_path, 'r', encoding='utf-8') as file:
        # Read and return the content of the file
        return file.read()
    
def fetch_content(url):
    """
    Fetch the content of the given URL.

    Args:
        url (str): The URL to fetch the content from.

    Returns:
        str: The content of the URL as a string.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None

def send_to_server(champions, server_url):
    """
    Sends a list of Champion objects to a specified server URL and returns the server's response.

    Args:
        champions (list): A list of Champion objects to be sent to the server.
        server_url (str): The URL of the server where the data will be sent.

    Returns:
        requests.Response: The HTTP response from the server.
    """
    # Convert each Champion object into a dictionary and create a list of these dictionaries
    data = [champion.__dict__ for champion in champions]

    try:
        # Send a POST request to the server with the data in JSON format
        response = requests.post(server_url, json=data)

        # Return the HTTP response object
        return response

    except requests.exceptions.RequestException as e:
        # Print an error message if there was a problem sending the data
        print(f"Error sending data to {server_url}: {e}")
        # Re-raise the exception to let the caller handle it
        raise
