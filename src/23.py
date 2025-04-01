import requests
from bs4 import BeautifulSoup

def fetch_page(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        return None

def parse_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    for link in soup.find_all('a'):
        href = link.get('href')
        title = link.string.strip()
        print(f"Title: {title} | Link: {href}")

url = "https://example.com"
fetch_page(url)
parse_html(fetch_page(url))
