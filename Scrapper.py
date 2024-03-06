import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import json
import os

def scrape_webpage(url):
    # Fetch the HTML content of the webpage
    response = requests.get(url)
    scraped_urls = []  # Initialize a list to store scraped URLs
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content using Beautiful Soup
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Example: Find all <a> tags and append their href attribute to the list
        for link in soup.find_all('a'):
            href = link.get('href')
            if href and 'watch' in href:  # Check if 'watch' is in the URL
                # Join the given URL and scraped URL
                absolute_url = urljoin(url, href)
                scraped_urls.append(absolute_url)
    else:
        print("Failed to fetch webpage:", response.status_code)
    
    return scraped_urls

# Example usage
url = 'https://aniwave.to/home'
scraped_urls = scrape_webpage(url)

# Save the scraped URLs to a JSON file in the same directory
json_file_path = 'scraped_urls.json'
with open(json_file_path, 'w') as json_file:
    json.dump(scraped_urls, json_file)

print("Scraped URLs saved to:", json_file_path)
