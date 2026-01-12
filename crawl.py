import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def extract_links(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise error for bad status codes
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')
    links = []

    for a_tag in soup.find_all('a', href=True):
        full_url = urljoin(url, a_tag['href'])  # Resolve relative URLs
        links.append(full_url)

    return links

# Example usage:
start_url = 'https://youtube.com'
found_links = extract_links(start_url)

for link in found_links:
    print(link)
