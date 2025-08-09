import re
from collections import Counter

# Most frequent word in paragraph
paragraph = """I love teaching. If you do not love teaching
what else can you love. I love Python if you do not love
something which can give you all the capabilities to develop
an application what else can you love."""

# Remove punctuation and split into words
words = re.findall(r'\b\w+\b', paragraph)
word_counts = Counter(words)
most_common_words = word_counts.most_common()

print("Word frequency in paragraph:", most_common_words)
print("Most frequent word:", most_common_words[0])  # ('love', 6)


# Distance between furthest particles
points_text = "-12, -4, -3, -1, 0, 4, 8"
points = list(map(int, re.findall(r'-?\d+', points_text)))
distance = max(points) - min(points)

print("Points extracted from text:", points)
print("Distance between furthest particles:", distance)  # 20

# Valid Python variable name checker
def is_valid_variable(name):
    return re.match(r'^[a-zA-Z_]\w*$', name) is not None

print("Is 'first_name' valid?:", is_valid_variable('first_name'))
print("Is 'first-name' valid?:", is_valid_variable('first-name'))
print("Is '1first_name' valid?:", is_valid_variable('1first_name'))
print("Is 'firstname' valid?:", is_valid_variable('firstname'))


#Clean text and find 3 most frequent words
sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve
%tea@ching%;. There $is nothing; &as& mo@re rewarding as
educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching
m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s
mo@tivate yo@u to be a tea@cher!?'''

def clean_text(text):
    return re.sub(r'[^A-Za-z\s]', '', text)

cleaned_text = clean_text(sentence)
three_most_common = Counter(cleaned_text.split()).most_common(3)

print("Cleaned sentence:", cleaned_text)
print("Three most frequent words in cleaned text:", three_most_common)
