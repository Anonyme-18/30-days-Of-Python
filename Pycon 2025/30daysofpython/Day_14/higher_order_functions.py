from functools import reduce

# Explanation part
print("Difference between map, filter, and reduce:")
print("- map() applies a function to each item in a list and returns a new iterable with the transformed items.")
print("- filter() applies a function to each item and keeps only those for which the function returns True.")
print("- reduce() applies a function cumulatively to the items of a list, reducing it to a single value.\n")

print("Difference between higher order function, closure, and decorator:")
print("- Higher-order function: A function that takes another function as an argument or returns a function.")
print("- Closure: A nested function that captures variables from its enclosing scope.")
print("- Decorator: A function that modifies another function’s behavior without changing its code.\n")

# Sample function to use before map, filter, reduce
def square(x):
    return x * x

def is_even(x):
    return x % 2 == 0

print("Sample function call before using map, filter, or reduce:")
print("Square of 4 is:", square(4))
print("Is 4 even?", is_even(4), "\n")

# Example lists
countries = ["Finland", "Sweden", "Norway", "Estonia", "Denmark", "Iceland"]
names = ["Asabeneh", "David", "Donald", "Bill"]
numbers = [1, 2, 3, 4, 5]

# Loop examples
print("Countries in the list:")
for country in countries:
    print(" -", country)
print()

print("Names in the list:")
for name in names:
    print(" -", name)
print()

print("Numbers in the list:")
for num in numbers:
    print(" -", num)
print()

#Level 2 - map examples
countries_upper = list(map(str.upper, countries))
print("Countries in uppercase:", countries_upper)

numbers_squared = list(map(lambda x: x ** 2, numbers))
print("Numbers squared:", numbers_squared)

names_upper = list(map(str.upper, names))
print("Names in uppercase:", names_upper)
print()

# Level 2 - filter examples
countries_with_land = list(filter(lambda x: "land" in x.lower(), countries))
print("Countries containing 'land':", countries_with_land)

countries_with_six_chars = list(filter(lambda x: len(x) == 6, countries))
print("Countries with exactly 6 characters:", countries_with_six_chars)

countries_with_six_or_more_chars = list(filter(lambda x: len(x) >= 6, countries))
print("Countries with 6 or more characters:", countries_with_six_or_more_chars)

countries_starting_with_E = list(filter(lambda x: x.startswith("E"), countries))
print("Countries starting with 'E':", countries_starting_with_E)
print()

# Chaining iterators
chained_result = reduce(lambda x, y: x + y,
                        map(lambda n: n * 2,
                            filter(lambda n: n % 2 == 0, numbers)))
print("Chained operation result (double even numbers and sum):", chained_result)
print()

#Custom function to get only strings
def get_string_lists(lst):
    return [i for i in lst if isinstance(i, str)]

mixed_list = ["apple", 3, "banana", True, "cherry"]
print("String items from mixed list:", get_string_lists(mixed_list))

# Reduce examples
sum_numbers = reduce(lambda a, b: a + b, numbers)
print("Sum of all numbers:", sum_numbers)

sentence_countries = reduce(lambda a, b: f"{a}, {b}", countries[:-1]) + f", and {countries[-1]} are north European countries"
print(sentence_countries)
print()

# Categorize countries by pattern
def categorize_countries(pattern):
    return [country for country in countries if pattern.lower() in country.lower()]

print("Countries containing 'land':", categorize_countries("land"))
print()

# Dictionary of starting letters
def countries_by_first_letter(countries_list):
    result = {}
    for country in countries_list:
        first_letter = country[0]
        result[first_letter] = result.get(first_letter, 0) + 1
    return result

print("Countries count by first letter:", countries_by_first_letter(countries))
print()

# First and last 10 countries
def get_first_ten_countries(countries_list):
    return countries_list[:10]

def get_last_ten_countries(countries_list):
    return countries_list[-10:]

print("First 10 countries:", get_first_ten_countries(countries))
print("Last 10 countries:", get_last_ten_countries(countries))
