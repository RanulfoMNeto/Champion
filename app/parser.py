from bs4 import BeautifulSoup

class Champion:
    def __init__(self, name, role, tier, win_rate, pick_rate, ban_rate, matches):
        self.name = name
        self.role = role
        self.tier = tier
        self.win_rate = win_rate
        self.pick_rate = pick_rate
        self.ban_rate = ban_rate
        self.matches = matches

    def __repr__(self):
        return (f"Champion(name={self.name!r}, role={self.role!r}, tier={self.tier!r}, "
                f"win_rate={self.win_rate!r}, pick_rate={self.pick_rate!r}, "
                f"ban_rate={self.ban_rate!r}, matches={self.matches!r})")

def extract_data(content):
    soup = BeautifulSoup(content, 'html.parser')

    # Extract data
    name = soup.find('span', class_='champion-name').get_text(strip=True)
    role_div = soup.find('div', class_='role-value')
    role = role_div.find('div', style=True).get_text(strip=True)
    
    tier = soup.find('div', class_='champion-tier').find('div', class_='tier').get_text(strip=True)
    win_rate = soup.find('div', class_='win-rate').find('div', class_='value').get_text(strip=True)
    pick_rate = soup.find('div', class_='pick-rate').find('div', class_='value').get_text(strip=True)
    ban_rate = soup.find('div', class_='ban-rate').find('div', class_='value').get_text(strip=True)
    matches = soup.find('div', class_='matches').find('div', class_='value').get_text(strip=True)

    return name, role, tier, win_rate, pick_rate, ban_rate, matches

def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

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
