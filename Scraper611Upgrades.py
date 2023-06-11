import requests
from bs4 import BeautifulSoup
import threading
import csv

class ScraperThread(threading.Thread):
    def __init__(self, url, results):
        threading.Thread.__init__(self)
        self.url = url
        self.results = results

    def run(self):
        response = requests.get(self.url)
        content = response.text
        soup = BeautifulSoup(content, 'html.parser')
        title = soup.find('title').text.strip()

        # Here you'll need to adjust based on each website's structure
        if 'shipwreckbeads' in self.url:
            products = soup.find_all('a', {'class': 'facets-item-cell-list-name'})
            price = soup.find_all('div', {'class': 'product-views-price'})

        data = []

        # Extract the desired information from each element
        for product, price_elem in zip(products, price):
            product_title = None
            for tag in ['span', 'div', 'h4', 'h3', 'h2', 'a']:
                product_title = product.find(tag)
                if product_title:
                    break
            price = None
            for tag in ['span', 'div', 'h4', 'h3', 'h2']:
                price = price_elem.find(tag, recursive=False)
                if price:
                    break
            if product_title is not None and price is not None:
                product_name = product_title.text.strip()
                price_text = price.text.strip()
                data.append((product_name, price_text))

        self.results.append((self.url, title, data))

#root_url = ['https://www.shipwreckbeads.com/Beads/seed-beads']
#results = []

root_url = 'https://www.shipwreckbeads.com/Beads/seed-beads'
#root_url = 'https://powwowsupply.com/seed-beads/11-0-seed-beads/?limit=100&mode=bo'
#root_url = 'https://powwowsupply.com/seed-beads/11-0-seed-beads/?limit=100&page=2&mode=bo'
results = []

# Determine the number of pages or use a condition to stop
num_pages = 5  # Example: Scrape the first 5 pages
urls = [f'{root_url}?page={page}&show=96&display=list' for page in range(1, num_pages + 1)]

threads = []
for url in urls:
    thread = ScraperThread(url, results)
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

for url, title, data in results:
    print(f'{url}: {title}')
    for product_title, price in data:
        print(f'Product: {product_title}')
        print(f'Price: {price}')
        print()

# Save results to CSV file
with open(r'C:\Users\texho\Documents\output.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['URL', 'Title', 'Product', 'Price'])
    for url, title, data in results:
        for product_title, price in data:
            writer.writerow([url, title, product_title, price])
