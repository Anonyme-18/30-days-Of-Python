import requests
from collections import Counter
import statistics
from bs4 import BeautifulSoup

#Romeo and Juliet Analysis
def get_text_from_url(url):
    """Download text content from a given URL."""
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return ""

def find_most_frequent_words(text, top_n=10):
    """Return the top N most frequent words from a given text."""
    words = [word.lower().strip('.,;:!?()"') for word in text.split()]
    word_counts = Counter(words)
    return word_counts.most_common(top_n)

print("Analyzing Romeo and Juliet...")
# Updated URL to working Project Gutenberg link
romeo_url = "https://www.gutenberg.org/ebooks/1513.txt.utf-8"
romeo_text = get_text_from_url(romeo_url)
if romeo_text:
    top_10_words_romeo = find_most_frequent_words(romeo_text, 10)
    print("Top 10 words in Romeo and Juliet:", top_10_words_romeo)
else:
    print("Could not retrieve Romeo and Juliet text.")

#Cats API Analysis
def fetch_cats_data():
    """Fetch all breeds data from the Cat API."""
    try:
        url = "https://api.thecatapi.com/v1/breeds"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"❌ Error fetching cats API: {e}")
        return []

def extract_metric_values(cats_data, key):
    """Extract numeric values from a weight or lifespan metric string."""
    values = []
    for breed in cats_data:
        if key in breed and breed[key]:
            try:
                range_values = breed[key]['metric'] if isinstance(breed[key], dict) else breed[key]
                range_parts = range_values.split(" - ")
                values.extend([float(r) for r in range_parts])
            except:
                pass
    return values

def extract_lifespan_values(cats_data):
    """Extract numeric lifespan values from cats API data."""
    values = []
    for breed in cats_data:
        if 'life_span' in breed and breed['life_span']:
            try:
                parts = breed['life_span'].split(" - ")
                values.extend([float(p) for p in parts])
            except:
                pass
    return values

def print_statistics(values, label):
    """Print min, max, mean, median, and standard deviation."""
    if not values:
        print(f" No data for {label}")
        return
    print(f" {label}:")
    print("  Min:", min(values))
    print("  Max:", max(values))
    print("  Mean:", statistics.mean(values))
    print("  Median:", statistics.median(values))
    print("  Std Dev:", statistics.stdev(values))

print("\nAnalyzing Cats API...")
cats_data = fetch_cats_data()

# Weight analysis
cats_weights_metric = extract_metric_values(cats_data, 'weight')
print_statistics(cats_weights_metric, "Cats weight (kg)")

# Lifespan analysis
cats_lifespans = extract_lifespan_values(cats_data)
print_statistics(cats_lifespans, "Cats lifespan (years)")

# Frequency table of country and breed
country_breed_table = Counter(breed.get('origin', 'Unknown') for breed in cats_data)
print("\nFrequency of cat breeds by country of origin:")
for country, count in country_breed_table.most_common():
    print(f"{country}: {count}")

#Countries API Analysis
def fetch_countries_data():
    """Fetch all country data from REST Countries API."""
    try:
        url = "https://restcountries.com/v3.1/all"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching countries API: {e}")
        return []

print("\nAnalyzing Countries API...")
countries_data = fetch_countries_data()

# 10 largest countries by area
largest_countries = sorted(
    ((country['name']['common'], country.get('area', 0)) for country in countries_data),
    key=lambda x: x[1],
    reverse=True
)[:10]
print("\nTop 10 largest countries by area:")
for name, area in largest_countries:
    print(f"{name}: {area} km²")

# 10 most spoken languages
languages_count = Counter()
for country in countries_data:
    langs = country.get('languages', {})
    for lang in langs.values():
        languages_count[lang] += 1
most_spoken_languages = languages_count.most_common(10)
print("\nTop 10 most spoken languages:")
for lang, count in most_spoken_languages:
    print(f"{lang}: spoken in {count} countries")

# Total number of languages
total_languages = len(languages_count)
print("\n Total number of distinct languages:", total_languages)

#UCI Datasets Page Analysis
def fetch_uci_datasets():
    """Fetch and parse dataset names from UCI Machine Learning Repository."""
    try:
        url = "https://archive.ics.uci.edu/ml/datasets.php"
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        dataset_links = soup.find_all('p')
        datasets = [link.get_text(strip=True) for link in dataset_links if link.get_text(strip=True)]
        return datasets
    except requests.exceptions.RequestException as e:
        print(f"Error fetching UCI datasets: {e}")
        return []

print("\n Fetching UCI datasets list (may be partial due to HTML structure)...")
uci_datasets = fetch_uci_datasets()
print(f"Found approximately {len(uci_datasets)} dataset entries.")
print("First 10 datasets:")
for dataset in uci_datasets[:10]:
    print("-", dataset)
