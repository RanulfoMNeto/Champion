from utils import send_to_server, read_file
from parser import Champion, extract_data

if __name__ == '__main__':

    # Path to the HTML file
    file_path = 'index.html'
    
    # Read the content of the HTML file
    content = read_file(file_path)

    # Extract data from HTML content
    name, role, tier, win_rate, pick_rate, ban_rate, matches = extract_data(content)
    
    # Create a Champion instance from the extracted data
    champion = Champion(name, role, tier, win_rate, pick_rate, ban_rate, matches)
    
    # Print the champion details
    print(champion)

    data = {
        'name': champion.name,
        'role': champion.role,
        'tier': champion.tier,
        'win_rate': champion.win_rate,
        'pick_rate': champion.pick_rate,
        'ban_rate': champion.ban_rate,
        'matches': champion.matches
    }

    send_to_server(data)
