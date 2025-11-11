from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

class DynamicScraper:
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(options=chrome_options)
        self.url = "https://dynamic.example.com"

    def scrape(self):
        self.driver.get(self.url)
        self.driver.implicitly_wait(5)
        html = self.driver.page_source
        soup = BeautifulSoup(html, "html.parser")
        self.driver.quit()
        return self.extract_data(soup)

    def extract_data(self, soup):
        data = []
        for item in soup.select(".dynamic-item"):
            title = item.select_one(".title").text.strip()
            description = item.select_one(".description").text.strip()
            data.append({"title": title, "description": description})
        return data
