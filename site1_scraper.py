from .base_scraper.py import BaseScraper

class Site1Scraper(BaseScraper):
    def __init__(self):
        super().__init__("https://example.com/products")

    def extract_data(self, soup):
        data = []
        for product in soup.select(".product-item"):
            name = product.select_one(".product-name").text.strip()
            price = product.select_one(".product-price").text.strip()
            data.append({"name": name, "price": price})
        return data
