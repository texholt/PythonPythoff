import requests
from bs4 import BeautifulSoup

# Send a GET request to the Reddit homepage
response = requests.get('https://www.reddit.com')

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find all the link elements using the appropriate selector
link_elements = soup.select('a')

# Extract the URLs from the link elements
links = [link['href'] for link in link_elements if link.get('href')]

# Print the extracted links
for link in links:
    print(link)
