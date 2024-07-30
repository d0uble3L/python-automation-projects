import requests
from bs4 import BeautifulSoup

def scrape_product_prices(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    products = soup.find_all('div', class_='product')
    for product in products:
        name = product.find('h2', class_='product-title').text.strip()
        price = product.find('span', class_='product-price').text.strip()
        print(f"Product: {name}, Price: {price}")

# Example usage
url = int(input("Enter the product site:"))
scrape_product_prices(url)
