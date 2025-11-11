from scrapers.site1_scraper import Site1Scraper
from scrapers.dynamic_scraper import DynamicScraper
from storage.csv_storage import CSVStorage
from storage.db_storage import DBStorage

def main():
    # Initialize storage
    csv_storage = CSVStorage("data/site1_data.csv")
    db_storage = DBStorage("data/scraper.db")

    # Scrape static site
    site1_scraper = Site1Scraper()
    site1_data = site1_scraper.scrape()
    csv_storage.save(site1_data)
    db_storage.save(site1_data)

    # Scrape dynamic site
    dynamic_scraper = DynamicScraper()
    dynamic_data = dynamic_scraper.scrape()
    csv_storage.save(dynamic_data)
    db_storage.save(dynamic_data)

if __name__ == "__main__":
    main()
