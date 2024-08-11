from bs4 import BeautifulSoup
from utils import read_file, fetch_content
from urllib.parse import urljoin

class Champion:
    def __init__(self, name, role, tier, win_rate, pick_rate, ban_rate, matches):
        """
        Initialize a Champion object with the provided attributes.

        Args:
            name (str): The name of the champion.
            role (str): The role of the champion.
            tier (str): The tier of the champion.
            win_rate (str): The win rate of the champion.
            pick_rate (str): The pick rate of the champion.
            ban_rate (str): The ban rate of the champion.
            matches (str): The number of matches played with the champion.
        """
        self.name = name
        self.role = role
        self.tier = tier
        self.win_rate = win_rate
        self.pick_rate = pick_rate
        self.ban_rate = ban_rate
        self.matches = matches

    def __repr__(self):
        """
        Return a string representation of the Champion object.

        Returns:
            str: A formatted string describing the Champion object.
        """
        return (f"Champion(name={self.name!r}, role={self.role!r}, tier={self.tier!r}, "
                f"win_rate={self.win_rate!r}, pick_rate={self.pick_rate!r}, "
                f"ban_rate={self.ban_rate!r}, matches={self.matches!r})")

def extract_champions(file_path, base_url):

    # Read the content of the HTML file
    content = read_file(file_path)

    champions = []

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(content, 'html.parser')
    
    # Extract all URLs for champions
    urls = [urljoin(base_url, a['href']) for a in soup.find_all('a', class_='champion-link')]

    i = 0
    for url in urls:
        # if i == 20:
        #     break
        # Fetch the content of the champion page
        content = fetch_content(url)

        if content:  # Proceed only if content was successfully fetched
            # Extract champion data from the HTML content
            name, role, tier, win_rate, pick_rate, ban_rate, matches = extract_champion(content)
            
            # Create a Champion object using the extracted data
            champion = Champion(name, role, tier, win_rate, pick_rate, ban_rate, matches)

            champions.append(champion)
        i += 1

    return champions

def extract_champion(content):
    """
    Extract champion data from HTML content.

    Args:
        content (str): The HTML content as a string.

    Returns:
        tuple: A tuple containing the champion's name, role, tier, win rate, pick rate, ban rate, and matches.
    """
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(content, 'html.parser')

    # Extract the champion's name
    name = soup.find('span', class_='champion-name').get_text(strip=True)
    
    # Extract the champion's role from a nested div structure
    role_div = soup.find('div', class_='role-value')
    role = role_div.find('div', style=True).get_text(strip=True)
    
    # Extract the champion's tier
    tier = soup.find('div', class_='champion-tier').find('div', class_='tier').get_text(strip=True)
    
    # Extract the champion's win rate
    win_rate = soup.find('div', class_='win-rate').find('div', class_='value').get_text(strip=True)
    
    # Extract the champion's pick rate
    pick_rate = soup.find('div', class_='pick-rate').find('div', class_='value').get_text(strip=True)
    
    # Extract the champion's ban rate
    ban_rate = soup.find('div', class_='ban-rate').find('div', class_='value').get_text(strip=True)
    
    # Extract the number of matches played with the champion
    matches = soup.find('div', class_='matches').find('div', class_='value').get_text(strip=True)

    # Return the extracted data as a tuple
    return name, role, tier, win_rate, pick_rate, ban_rate, matches
