import json
import re
from collections import Counter

#Count number of lines and words in a file
def count_lines_and_words(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    words = [word for line in lines for word in line.split()]
    return len(lines), len(words)

files = [
    "data/obama_speech.txt",
    "data/michelle_obama_speech.txt",
    "data/donald_speech.txt",
    "data/melina_trump_speech.txt"
]

for file in files:
    line_count, word_count = count_lines_and_words(file)
    print(f"{file}: {line_count} lines, {word_count} words")

#Ten most spoken languages
def most_spoken_languages(filename, top_n):
    with open(filename, 'r', encoding='utf-8') as f:
        countries = json.load(f)

    lang_counter = Counter()
    for country in countries:
        for lang in country.get('languages', []):
            lang_counter[lang] += 1

    return lang_counter.most_common(top_n)

print("Top 10 most spoken languages:",
      most_spoken_languages('data/countries_data.json', 10))
print("Top 3 most spoken languages:",
      most_spoken_languages('data/countries_data.json', 3))

#Ten most populated countries
def most_populated_countries(filename, top_n):
    with open(filename, 'r', encoding='utf-8') as f:
        countries = json.load(f)

    sorted_countries = sorted(
        countries, key=lambda x: x.get('population', 0), reverse=True
    )
    return [{"country": c["name"], "population": c["population"]}
            for c in sorted_countries[:top_n]]

print("Top 10 most populated countries:",
      most_populated_countries('data/countries_data.json', 10))
print("Top 3 most populated countries:",
      most_populated_countries('data/countries_data.json', 3))

#Extract all incoming email addresses from file
def extract_emails(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    return re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', content)

emails = extract_emails('data/email_exchange_big.txt')
print("Extracted emails:", emails)

#Find the most common words in a text or file
def find_most_common_words(source, top_n):
    # Read from file if it's a filepath
    if isinstance(source, str) and source.endswith(".txt"):
        with open(source, 'r', encoding='utf-8') as f:
            text = f.read()
    else:
        text = source

    words = re.findall(r'\b\w+\b', text.lower())
    return Counter(words).most_common(top_n)

print("Top 10 words in sample.txt:",
      find_most_common_words('data/sample.txt', 10))
print("Top 5 words in sample.txt:",
      find_most_common_words('data/sample.txt', 5))
