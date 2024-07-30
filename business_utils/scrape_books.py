import asyncio
import aiohttp
from bs4 import BeautifulSoup

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

async def scrape_books(url):
    async with aiohttp.ClientSession() as session:
        html_content = await fetch(session, url)
        soup = BeautifulSoup(html_content, 'html.parser')
        
        books = soup.find_all('article', class_='product_pod')
        for book in books:
            try:
                title = book.find('h3').find('a')['title']
                price = book.find('p', class_='price_color').text.strip()
                availability = book.find('p', class_='instock availability').text.strip()
                print(f"Title: {title}, Price: {price}, Availability: {availability}")
            except AttributeError:
                # Handle missing elements
                continue

# Example usage
url = "http://books.toscrape.com/"
asyncio.run(scrape_books(url))
