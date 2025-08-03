# Function to add two numbers
def add_two_numbers(number_one, number_two):
    result = number_one + number_two
    return result

print(f"The sum of 50 and 60 is: {add_two_numbers(50, 60)}")


# Function to calculate area of a circle
def area_of_circle(radius):
    pi = 3.14
    area = pi * radius ** 2
    return area

print(f"The area of the circle with radius 7 is: {area_of_circle(7)}")


# Function to add all numbers with type checking
def add_all_nums(*args):
    total = 0
    for num in args:
        if not isinstance(num, (int, float)):
            return "All arguments must be numbers"
        total += num
    return total

print(f"The sum of (1, 2, 3, 4) is: {add_all_nums(1, 2, 3, 4)}")
print(f"Trying to sum (1, 'two', 3) gives: {add_all_nums(1, 'two', 3)}")


# Function to convert Celsius to Fahrenheit
def convert_celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

print(f"0°C in Fahrenheit is: {convert_celsius_to_fahrenheit(0)}°F")
print(f"30°C in Fahrenheit is: {convert_celsius_to_fahrenheit(30)}°F")


# Function to check the season from month name
def check_season(month):
    month = month.lower()
    if month in ["september", "october", "november"]:
        return "Autumn"
    elif month in ["december", "january", "february"]:
        return "Winter"
    elif month in ["march", "april", "may"]:
        return "Spring"
    elif month in ["june", "july", "august"]:
        return "Summer"
    else:
        return "Invalid month"

print(f"The season in March is: {check_season('March')}")
print(f"The season in August is: {check_season('August')}")


# Function to calculate slope between two points
def calculate_slope(x1, y1, x2, y2):
    if x2 - x1 == 0:
        return "Slope is undefined"
    return (y2 - y1) / (x2 - x1)

print(f"The slope between points (1, 2) and (3, 6) is: {calculate_slope(1, 2, 3, 6)}")


# Function to solve quadratic equation ax² + bx + c = 0
def solve_quadratic_eqn(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return "No real solution"
    elif discriminant == 0:
        x = -b / (2*a)
        return (x,)
    else:
        sqrt_d = discriminant ** 0.5
        x1 = (-b + sqrt_d) / (2*a)
        x2 = (-b - sqrt_d) / (2*a)
        return (x1, x2)

print(f"The solutions of equation x² - 3x + 2 = 0 are: {solve_quadratic_eqn(1, -3, 2)}")


# Function to print each item in a list
def print_list(items):
    print("The list contains:")
    for item in items:
        print(f"- {item}")

print_list(["Apple", "Banana", "Cherry"])


# Function to reverse a list using a loop
def reverse_list(lst):
    reversed_lst = []
    for i in range(len(lst)-1, -1, -1):
        reversed_lst.append(lst[i])
    return reversed_lst

print(f"Reversing [1, 2, 3, 4, 5] gives: {reverse_list([1, 2, 3, 4, 5])}")
print(f"Reversing ['A', 'B', 'C'] gives: {reverse_list(['A', 'B', 'C'])}")


# Function to capitalize each string in a list
def capitalize_list_items(lst):
    return [str(item).capitalize() for item in lst]

print(f"Capitalizing ['apple', 'banana', 'cherry'] gives: {capitalize_list_items(['apple', 'banana', 'cherry'])}")


# Function to add an item to the end of a list
def add_item(lst, item):
    lst.append(item)
    return lst

food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(f"Adding 'Meat' to {food_staff} gives: {add_item(food_staff, 'Meat')}")
numbers = [2, 3, 7, 9]
print(f"Adding 5 to {numbers} gives: {add_item(numbers, 5)}")


# Function to remove an item from a list
def remove_item(lst, item):
    if item in lst:
        lst.remove(item)
    return lst

food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(f"Removing 'Mango' from list gives: {remove_item(food_staff, 'Mango')}")
numbers = [2, 3, 7, 9]
print(f"Removing 3 from list gives: {remove_item(numbers, 3)}")


# Function to sum numbers from 0 to n
def sum_of_numbers(n):
    return sum(range(n+1))

print(f"The sum of numbers from 0 to 5 is: {sum_of_numbers(5)}")
print(f"The sum of numbers from 0 to 10 is: {sum_of_numbers(10)}")
print(f"The sum of numbers from 0 to 100 is: {sum_of_numbers(100)}")


# Function to sum odd numbers from 0 to n
def sum_of_odds(n):
    return sum(i for i in range(n+1) if i % 2 != 0)

print(f"The sum of odd numbers from 0 to 10 is: {sum_of_odds(10)}")


# Function to sum even numbers from 0 to n
def sum_of_even(n):
    return sum(i for i in range(n+1) if i % 2 == 0)

print(f"The sum of even numbers from 0 to 10 is: {sum_of_even(10)}")


# Function to count evens and odds from 0 to n
def evens_and_odds(n):
    even_count = 0
    odd_count = 0
    for i in range(n+1):
        if i % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return f"The number of odds are {odd_count}. The number of evens are {even_count}."

print(evens_and_odds(100))


# Function to calculate factorial of a number
def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

print(f"The factorial of 5 is: {factorial(5)}")

# Function to check if a value is empty
def is_empty(value):
    if value:
        return False
    else:
        return True

print(f"Is [] empty? {is_empty([])}")
print(f"Is 'Hello' empty? {is_empty('Hello')}")


# Function to calculate mean of a list
def calculate_mean(lst):
    if len(lst) == 0:
        return "List is empty"
    return sum(lst) / len(lst)

print(f"The mean of [1, 2, 3, 4, 5] is: {calculate_mean([1, 2, 3, 4, 5])}")


# Function to calculate median of a list
def calculate_median(lst):
    if len(lst) == 0:
        return "List is empty"
    sorted_lst = sorted(lst)
    mid = len(sorted_lst) // 2
    if len(sorted_lst) % 2 == 0:
        return (sorted_lst[mid - 1] + sorted_lst[mid]) / 2
    else:
        return sorted_lst[mid]

print(f"The median of [1, 3, 5, 7, 9] is: {calculate_median([1, 3, 5, 7, 9])}")


# Function to calculate mode of a list
def calculate_mode(lst):
    if len(lst) == 0:
        return "List is empty"
    frequency = {}
    for num in lst:
        frequency[num] = frequency.get(num, 0) + 1
    max_freq = max(frequency.values())
    modes = [key for key, val in frequency.items() if val == max_freq]
    if len(modes) == len(lst):
        return "No mode"
    return modes

print(f"The mode(s) of [1, 2, 2, 3, 4, 4, 4] is/are: {calculate_mode([1, 2, 2, 3, 4, 4, 4])}")


# Function to calculate range of a list
def calculate_range(lst):
    if len(lst) == 0:
        return "List is empty"
    return max(lst) - min(lst)

print(f"The range of [10, 2, 8, 4, 6] is: {calculate_range([10, 2, 8, 4, 6])}")


# Function to calculate variance of a list
def calculate_variance(lst):
    if len(lst) == 0:
        return "List is empty"
    mean = calculate_mean(lst)
    return sum((x - mean) ** 2 for x in lst) / len(lst)

print(f"The variance of [1, 2, 3, 4, 5] is: {calculate_variance([1, 2, 3, 4, 5])}")


# Function to calculate standard deviation of a list
def calculate_std(lst):
    if len(lst) == 0:
        return "List is empty"
    variance = calculate_variance(lst)
    return variance ** 0.5

print(f"The standard deviation of [1, 2, 3, 4, 5] is: {calculate_std([1, 2, 3, 4, 5])}")


# Function to check if a number is prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

print(f"Is 7 a prime number? {is_prime(7)}")
print(f"Is 10 a prime number? {is_prime(10)}")


# Function to check if all items in a list are unique
def all_unique(lst):
    return len(lst) == len(set(lst))

print(f"Are all items in [1, 2, 3, 4] unique? {all_unique([1, 2, 3, 4])}")
print(f"Are all items in [1, 2, 2, 3] unique? {all_unique([1, 2, 2, 3])}")


# Function to check if all items in a list are of the same data type
def same_data_type(lst):
    if not lst:
        return True
    first_type = type(lst[0])
    for item in lst:
        if type(item) != first_type:
            return False
    return True

print(f"Do all items in [1, 2, 3] have the same type? {same_data_type([1, 2, 3])}")
print(f"Do all items in [1, 'two', 3] have the same type? {same_data_type([1, 'two', 3])}")


# Function to check if a variable name is a valid Python identifier
def is_valid_variable(name):
    if not name.isidentifier():
        return False
    keywords = [
        "False", "None", "True", "and", "as", "assert", "async", "await",
        "break", "class", "continue", "def", "del", "elif", "else", "except",
        "finally", "for", "from", "global", "if", "import", "in", "is",
        "lambda", "nonlocal", "not", "or", "pass", "raise", "return",
        "try", "while", "with", "yield"
    ]
    return name not in keywords

print(f"Is 'my_var' a valid variable name? {is_valid_variable('my_var')}")
print(f"Is 'for' a valid variable name? {is_valid_variable('for')}")


# Example data from countries-data.py
countries_data = [
    {"country": "China", "languages": ["Chinese"], "population": 1444216107},
    {"country": "India", "languages": ["Hindi", "English"], "population": 1393409038},
    {"country": "USA", "languages": ["English"], "population": 331893745},
    {"country": "Nigeria", "languages": ["English", "Hausa", "Yoruba", "Igbo"], "population": 206139589},
    {"country": "Brazil", "languages": ["Portuguese"], "population": 212559417},
    {"country": "Russia", "languages": ["Russian"], "population": 145934462},
    {"country": "Japan", "languages": ["Japanese"], "population": 125960000},
    {"country": "Mexico", "languages": ["Spanish"], "population": 128932753},
    {"country": "Ethiopia", "languages": ["Amharic"], "population": 114963588},
    {"country": "Egypt", "languages": ["Arabic"], "population": 102334404}
]


# Function to find most spoken languages
def most_spoken_languages(data, top_n=10):
    language_count = {}
    for country in data:
        for language in country["languages"]:
            language_count[language] = language_count.get(language, 0) + 1
    sorted_languages = sorted(language_count.items(), key=lambda x: x[1], reverse=True)
    return sorted_languages[:top_n]

languages_top5 = most_spoken_languages(countries_data, 5)
print("Top 5 most spoken languages:")
for lang, count in languages_top5:
    print(f"- {lang} spoken in {count} countries")


# Function to find most populated countries
def most_populated_countries(data, top_n=10):
    sorted_countries = sorted(data, key=lambda x: x["population"], reverse=True)
    return sorted_countries[:top_n]

countries_top5 = most_populated_countries(countries_data, 5)
print("Top 5 most populated countries:")
for country in countries_top5:
    print(f"- {country['country']}: {country['population']:,} people")
