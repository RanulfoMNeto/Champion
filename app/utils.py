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

def send_to_server(data):
    """
    Sends data to a server via a POST request.

    Args:
        data (dict): The data to be sent in the POST request.

    Returns:
        None
    """
    # Define the URL of the server endpoint where data will be sent
    url = 'http://example.com/api/dataset'
    
    # Send a POST request to the server with the data in JSON format
    response = requests.post(url, json=data)
    
    # Print the HTTP status code and reason phrase of the response
    print(response.status_code, response.reason)
