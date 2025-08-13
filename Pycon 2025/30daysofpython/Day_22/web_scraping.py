import requests
from bs4 import BeautifulSoup
import json

# -----------------------------
# 1. Scrape BU Facts & Stats
# -----------------------------
def scrape_bu_facts_stats():
    url = 'https://www.bu.edu/president/boston-university-facts-stats/'
    resp = requests.get(url)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, 'html.parser')

    stats_section = soup.find('div', text='BU Facts & Stats')
    stats = {}
    if stats_section:
        stats_items = stats_section.find_next('div').find_all(['li', 'p'])
        for item in stats_items:
            if ':' in item.text:
                key, val = item.text.split(':', 1)
                stats[key.strip()] = val.strip()
    return stats

bu_stats = scrape_bu_facts_stats()
print("BU Facts & Stats:", bu_stats)
with open('bu_facts_stats.json', 'w', encoding='utf-8') as f:
    json.dump(bu_stats, f, indent=2)

# -----------------------------
# 2. Scrape UCI Dataset Names
# -----------------------------
def scrape_uci_dataset_names():
    url = 'https://archive.ics.uci.edu/'
    resp = requests.get(url)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, 'html.parser')

    table = soup.find('table', {'border': '1'})
    dataset_names = []
    if table:
        for row in table.find_all('tr')[1:]:
            first_cell = row.find('td')
            if first_cell:
                link = first_cell.find('a')
                if link:
                    dataset_names.append(link.text.strip())
    return dataset_names

uci_names = scrape_uci_dataset_names()
print("UCI Dataset Names (first 10):", uci_names[:10])
with open('uci_dataset_names.json', 'w', encoding='utf-8') as f:
    json.dump(uci_names, f, indent=2)

# -----------------------------
# 3. Scrape U.S. Presidents from Wikipedia
# -----------------------------
def scrape_us_presidents():
    url = 'https://simple.wikipedia.org/wiki/List_of_presidents_of_the_United_States'
    resp = requests.get(url)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, 'html.parser')

    pres_table = soup.find('table', {'class': 'wikitable'})
    presidents = []
    if pres_table:
        for row in pres_table.find_all('tr')[1:]:
            cols = row.find_all('td')
            if len(cols) >= 2:
                name = cols[0].text.strip()
                term = cols[1].text.strip()
                presidents.append({'name': name, 'term': term})
    return presidents

us_presidents = scrape_us_presidents()
print("First few U.S. Presidents:", us_presidents[:5])
with open('us_presidents.json', 'w', encoding='utf-8') as f:
    json.dump(us_presidents, f, indent=2)
