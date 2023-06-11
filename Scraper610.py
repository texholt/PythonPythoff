import requests
from bs4 import BeautifulSoup
import threading

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
        elif 'powwowsupply' in self.url:
            products = soup.find_all('h4', {'class': 'card-title'})
            price = soup.find_all('div', {'class': 'price-section'})
        elif 'prairieedge' in self.url:
            products = soup.find_all('h3', {'class': 'product-item-title'})
            price = soup.find_all('div', {'class': 'product-item-price'})
        elif 'beadededgesupply' in self.url:
            products = soup.find_all('h3', {'class': 'product__title'})
            price = soup.find_all('span', {'class': 'product__price-price'})

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

urls = [
    'https://www.shipwreckbeads.com/Beads/seed-beads?show=96&display=list',
    'https://powwowsupply.com/seed-beads/11-0-seed-beads/?limit=100',
    'https://prairieedge.com/beads/',
    'https://www.beadededgesupply.com/collections/11-0-czech-seed-opaque'
]
results = []

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

