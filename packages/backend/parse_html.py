from bs4 import BeautifulSoup
import json

# Load the saved HTML content
with open("sample.html", "r", encoding="utf-8") as file:
    html_content = file.read()

# Parse the HTML content using BeautifulSoup
html = BeautifulSoup(html_content, 'html.parser')

json_output = {}

# Find the <script> tag with type="application/ld+json"
script_tag = html.find('script', type='application/ld+json')
if script_tag:
    # Parse the JSON content from the script tag
    script_json = json.loads(script_tag.string)
    
    # Extract the data from the parsed JSON
    json_output['name'] = script_json.get('name', '')
    # json_output['description'] = script_json.get('description', '')
    json_output['contentRating'] = script_json.get('contentRating', '')
    # json_output['image'] = script_json.get('image', '')
    json_output['url'] = script_json.get('url', '')
    
    aggregate_rating = script_json.get('aggregateRating', {})
    json_output['ratingValue'] = aggregate_rating.get('ratingValue', 0)
    json_output['reviewCount'] = aggregate_rating.get('reviewCount', 0)
    
    json_output['genre'] = script_json.get('genre', '')
    
    # screenshots = script_json.get('screenshot', [])
    # json_output['screenshot'] = [s.get('contentUrl', '') for s in screenshots]
    
    json_output['gamePlatform'] = script_json.get('gamePlatform', [])
    # json_output['publisher'] = [p.get('name', '') for p in script_json.get('publisher', [])]

else:
    print("Script tag with type='application/ld+json' not found.")
    json_output['error'] = "Script tag with type='application/ld+json' not found."

# Print the extracted JSON data
print(json.dumps(json_output, indent=4))
