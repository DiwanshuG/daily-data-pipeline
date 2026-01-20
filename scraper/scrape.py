import requests
import pandas as pd
from bs4 import BeautifulSoup
from utils import get_today_date, ensure_dir

BASE_URL = "https://quotes.toscrape.com/"
DATA_DIR = "data/daily"

def fetch_quotes():
    all_quotes = []

    for page in range(1, 6):  # scrape multiple pages
        url = f"{BASE_URL}page/{page}/"
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")

        quotes = soup.find_all("div", class_="quote")
        for q in quotes:
            text = q.find("span", class_="text").text
            author = q.find("small", class_="author").text
            all_quotes.append({
                "quote": text,
                "author": author
            })

    return all_quotes

def simulate_large_dataset(records, target_size=3000):
    multiplier = target_size // len(records) + 1
    expanded = records * multiplier
    return expanded[:target_size]

def main():
    print("Starting scraping job...")

    records = fetch_quotes()
    print(f"Fetched {len(records)} base records")

    records = simulate_large_dataset(records)
    print(f"Expanded to {len(records)} records")

    df = pd.DataFrame(records)

    ensure_dir(DATA_DIR)
    filename = f"{DATA_DIR}/{get_today_date()}.csv"
    df.to_csv(filename, index=False)

    print(f"Data saved to {filename}")

if __name__ == "__main__":
    main()

