from utils import send_to_server, read_file
from parser import Champion, extract_data

if __name__ == '__main__':

    # Define the path to the HTML file containing the champion data
    file_path = 'index.html'
    
    # Read the content of the HTML file
    content = read_file(file_path)

    # Extract champion data from the HTML content
    name, role, tier, win_rate, pick_rate, ban_rate, matches = extract_data(content)
    
    # Create a Champion object using the extracted data
    champion = Champion(name, role, tier, win_rate, pick_rate, ban_rate, matches)
    
    # Print the Champion object to the console
    print(champion)

    # Prepare the data to be sent to the server
    data = {
        'name': champion.name,
        'role': champion.role,
        'tier': champion.tier,
        'win_rate': champion.win_rate,
        'pick_rate': champion.pick_rate,
        'ban_rate': champion.ban_rate,
        'matches': champion.matches
    }

    # Send the data to the server using the send_to_server function
    # send_to_server(data)
