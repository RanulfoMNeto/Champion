from bs4 import BeautifulSoup

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

def extract_data(content):
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
