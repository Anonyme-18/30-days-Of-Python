#Filter only negative and zero numbers using list comprehension
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
negatives_and_zero = [n for n in numbers if n <= 0]
print("Negative and zero numbers:", negatives_and_zero)


#Flatten the list_of_lists to a one-dimensional list
list_of_lists = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
flattened_list = [num for sublist1 in list_of_lists for sublist2 in sublist1 for num in sublist2]
print("Flattened list:", flattened_list)


#List comprehension to create tuples with powers
tuple_list = [(i, 1, i, i**2, i**3, i**4, i**5) for i in range(11)]
print("List of tuples with powers:")
for t in tuple_list:
    print("   ", t)


#Flatten countries list to a new list format
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
formatted_countries = [[country.upper(), country[:3].upper(), city.upper()]
                       for sublist in countries for (country, city) in sublist]
print("Countries with abbreviation and capitals:", formatted_countries)


#Change countries list to a list of dictionaries
country_dicts = [{'country': country.upper(), 'city': city.upper()}
                 for sublist in countries for (country, city) in sublist]
print("List of dictionaries:", country_dicts)


#Change names list to a list of concatenated strings
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')],
         [('Donald', 'Trump')], [('Bill', 'Gates')]]
full_names = [' '.join(name) for sublist in names for name in sublist]
print("Full names:", full_names)


#Lambda function for slope and y-intercept
# slope: m = (y2 - y1) / (x2 - x1)
slope = lambda x1, y1, x2, y2: (y2 - y1) / (x2 - x1)
# y-intercept: b = y - m*x
y_intercept = lambda x, y, m: y - m * x

# Example usage:
m = slope(2, 3, 5, 11)
b = y_intercept(2, 3, m)
print(f"Slope: {m}")
print(f"Y-intercept: {b}")
