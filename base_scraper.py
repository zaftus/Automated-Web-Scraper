import requests
from bs4 import BeautifulSoup

class BaseScraper:
    def __init__(self, url):
        self.url = url

    def fetch_page(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            return response.text
        else:
            raise Exception(f"Failed to fetch {self.url} with status code {response.status_code}")

    def parse_html(self, html):
        return BeautifulSoup(html, "html.parser")

    def scrape(self):
        html = self.fetch_page()
        soup = self.parse_html(html)
        return self.extract_data(soup)

    def extract_data(self, soup):
        raise NotImplementedError("Each scraper must implement its own extract_data method")
