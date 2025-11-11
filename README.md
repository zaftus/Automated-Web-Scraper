# Automated Web Scraper

## Overview
Automated Web Scraper is a professional Python project designed to extract structured data from multiple websites. It supports static and dynamic web pages, handles pagination, and saves the scraped data to CSV files or a SQLite database.

## Features
- Modular and extensible architecture
- Scrapes static content using Requests and BeautifulSoup
- Scrapes dynamic content using Selenium
- Stores data in CSV and SQLite for easy access
- Logging for all scraping actions
- Unit tests for scraper and storage modules

## Project Structure
- `main.py` – Entry point for running scrapers
- `scrapers/` – Contains scraper modules for different websites
- `storage/` – Handles saving data in CSV and database
- `utils/` – Utility modules including logging
- `config/` – Configuration for URLs and settings
- `tests/` – Unit tests
- `logs/` – Logging output

## Usage
1. Clone the repository:
```bash
git clone https://github.com/yourusername/automated-web-scraper.git
