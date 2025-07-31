empty_list = []

items = ['pen', 'notebook', 'charger', 'phone', 'bag', 'laptop']

print(len(items))

print(items[0])
print(items[len(items) // 2])
print(items[-1])

mixed_data_types = ['Cédric', 19, 1.82, 'Single', 'My Address']

it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

print(it_companies)

print(len(it_companies))

print(it_companies[0])
print(it_companies[len(it_companies) // 2])
print(it_companies[-1])

it_companies[1] = 'Anonyme'
print(it_companies)

it_companies.append('Flexitech')
print(it_companies)

it_companies.insert(len(it_companies) // 2, 'Samsung')
print(it_companies)

it_companies[0] = it_companies[0].upper()
print(it_companies)

joined_companies = '#; '.join(it_companies)
print(joined_companies)

print('Amazon' in it_companies)

it_companies.sort()
print(it_companies)

it_companies.reverse()
print(it_companies)

print(it_companies[0:3])
print(it_companies[-3:])
mid_it = len(it_companies) // 2
print(it_companies[mid_it])

del it_companies[0]
print(it_companies)

del it_companies[mid_it]
print(it_companies)

del it_companies[-1]
print(it_companies)

it_companies.clear()
print(it_companies)

del it_companies

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
full_stack = front_end + back_end

full_stack.insert(full_stack.index('Redux') + 1, 'Python')
full_stack.insert(full_stack.index('Python') + 1, 'SQL')
print(full_stack)


ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

ages.sort()
print(ages)

min_age = min(ages)
max_age = max(ages)
print(min_age)
print(max_age)

ages.append(min_age)
ages.append(max_age)
print(ages)

ages.sort()
length = len(ages)
if length % 2 == 0:
    median_age = (ages[length//2 - 1] + ages[length//2]) / 2
else:
    median_age = ages[length//2]
print(median_age)

average_age = sum(ages) / len(ages)
print(average_age)

age_range = max(ages) - min(ages)
print(age_range)

print(abs(min_age - average_age))
print(abs(max_age - average_age))

countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']

length_country = len(countries)
mid_index = length_country // 2
if length_country % 2 == 0:
    print(countries[mid_index - 1:mid_index + 1])
else:
    print(countries[mid_index])

if length_country % 2 == 0:
    first_half = countries[:mid_index]
    second_half = countries[mid_index:]
else:
    first_half = countries[:mid_index + 1]
    second_half = countries[mid_index + 1:]
print(first_half)
print(second_half)

country1 = countries[0]
country2 = countries[1]
country3 = countries[2]
scandic_countries = countries[3:]
print(country1)
print(country2)
print(country3)
print(scandic_countries)




