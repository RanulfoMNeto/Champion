from bs4 import BeautifulSoup
from utils import read_file, fetch_content
from urllib.parse import urljoin
import re

class Champion:
    def __init__(self, name, code, role, tier, win_rate, pick_rate, ban_rate, matches):
        """
        Initialize a Champion object with the provided attributes.

        Args:
            name (str): The name of the champion.
            code (str): The code of the champion.
            role (str): The role of the champion.
            tier (str): The tier of the champion.
            win_rate (str): The win rate of the champion.
            pick_rate (str): The pick rate of the champion.
            ban_rate (str): The ban rate of the champion.
            matches (str): The number of matches played with the champion.
        """
        self.name = name
        self.code = code
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
        return (f"Champion(name={self.name!r}, code={self.code!r}, role={self.role!r}, tier={self.tier!r}, "
                f"win_rate={self.win_rate!r}, pick_rate={self.pick_rate!r}, "
                f"ban_rate={self.ban_rate!r}, matches={self.matches!r})")

# Constants for CSS class names
CHAMPION_LINK_CLASS = 'group w-full mx-auto'
CHAMPION_NAME_CLASS = 'champion-name'
ROLE_VALUE_CLASS = 'role-value'
CHAMPION_TIER_CLASS = 'champion-tier'
WIN_RATE_CLASS = 'win-rate'
PICK_RATE_CLASS = 'pick-rate'
BAN_RATE_CLASS = 'ban-rate'
MATCHES_CLASS = 'matches'
VALUE_CLASS = 'value'

def extract_champion_code(url):
    """
    Extract the champion's code from the given URL.
    
    Args:
        url (str): The URL containing the champion's code.
    
    Returns:
        str: The code of the champion.
    """
    pattern = r'https://u\.gg/lol/champions/([^/]+)'
    match = re.search(pattern, url)
    return match.group(1) if match else None

def extract_champions(file_path, base_url):
    """
    Extract champion data from an HTML file and return a list of Champion objects.
    
    Args:
        file_path (str): Path to the HTML file.
        base_url (str): Base URL for constructing champion links.
    
    Returns:
        list: A list of Champion objects.
    """
    # Read the content of the HTML file
    content = read_file(file_path)

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(content, 'html.parser')

    # Extract all URLs for champions
    urls = [urljoin(base_url, a['href']) for a in soup.find_all('a', class_=CHAMPION_LINK_CLASS) if a.get("href")]
    
    champions = []
    for url in urls:
        try:
            # Extract champion data from the URL
            champion_data = extract_champion(url)
            # Create a Champion object using the extracted data
            champion = Champion(*champion_data)
            champions.append(champion)
        except Exception as e:
            print(f"Failed to extract champion from {url}: {e}")

    return champions

def extract_champion(url):
    """
    Extract champion data from the given URL.

    Args:
        url (str): The URL of the champion's page.

    Returns:
        tuple: A tuple containing the champion's name, code, role, tier, win rate, pick rate, ban rate, and number of matches.
    """
    content = fetch_content(url)
    soup = BeautifulSoup(content, 'html.parser')
    # Extract the champion's name
    name_element = soup.find('h1')
    name = name_element.find('span').get_text(strip=True) if name_element else "Unknown"

    # Extract the champion's code
    code = extract_champion_code(url)

    # Extract the champion's role
    role_div = soup.find('div', class_='role-value')
    role = role_div.get_text(strip=True) if role_div else "Unknown"

    # Extract the champion's tier
    tier_element = soup.find('div', class_='font-extrabold')
    tier = tier_element.get_text(strip=True) if tier_element else "N/A"

    # Extract champion statistics
    stat_blocks = soup.find_all('div', class_='font-extrabold')
    if len(stat_blocks) >= 6:
        win_rate = stat_blocks[1].get_text(strip=True)
        pick_rate = stat_blocks[3].get_text(strip=True)
        ban_rate = stat_blocks[4].get_text(strip=True)
        matches = stat_blocks[5].get_text(strip=True)
    else:
        win_rate, pick_rate, ban_rate, matches = ["N/A"] * 4

    # Return the extracted data as a tuple
    return name, code, role, tier, win_rate, pick_rate, ban_rate, matches