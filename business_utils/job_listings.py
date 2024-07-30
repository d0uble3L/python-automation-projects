import requests
from bs4 import BeautifulSoup

def scrape_job_listings(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    jobs = soup.find_all('div', class_='job-listing')
    for job in jobs:
        title = job.find('h2', class_='job-title').text.strip()
        company = job.find('div', class_='company-name').text.strip()
        location = job.find('div', class_='job-location').text.strip()
        print(f"Job Title: {title}, Company: {company}, Location: {location}")

# Example usage
url = str(input("Enter the job site:"))
scrape_job_listings(url)
