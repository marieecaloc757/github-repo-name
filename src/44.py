import requests
from bs4 import BeautifulSoup

def fetch_and_parse_html(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Example: Extracting all text from a specific element (replace with your desired HTML element)
    extracted_text = soup.find('div', {'class': 'example-class'}).text
    
    return extracted_text

url = "https://www.example.com"  # Replace with the actual URL you want to scrape
html_content = fetch_and_parse_html(url)

print(html_content)
