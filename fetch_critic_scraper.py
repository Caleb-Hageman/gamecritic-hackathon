import requests
import re

def get_metacritic_page(game_name):
    base_url = "http://www.metacritic.com/game/"
    
    # Sanitize and format the game name
    game_name = game_name.strip().replace(' ', '-').replace('& ', '').lower()
    game_name = re.sub(r'[^a-z\d\?!\-]', '', game_name)
    
    url = f"{base_url}/{game_name}"

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }

    response = requests.get(url, headers=headers)
    print(response)
    if response.status_code == 200:
        return response.text
    else:
        return None

game_title = "F1 Manager 2024"
html_content = get_metacritic_page(game_title)

if html_content:
    with open("sample.html", "w", encoding="utf-8") as file:
        file.write(html_content)
    print("Page fetched successfully and saved to sample.html.")
else:
    print("Failed to fetch the page.")
