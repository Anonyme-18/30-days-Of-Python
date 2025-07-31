# Checking the user's age
age = int(input("Please enter your age to check if you can drive: "))

if age >= 18:
    print("You are old enough to drive.\n")
else:
    missing_amount = 18 - age
    print("You need", missing_amount, "more years to learn to drive.\n")

# Comparing my_age and your_age
print("You will check if I'm older than you\n")
my_age = 19
your_age = int(input("Enter your age: "))

if my_age > your_age:
    difference = my_age - your_age
    print("I am", difference, "years older than you.\n")
elif my_age == your_age:
    print("We have the same age.\n")
else:
    difference = your_age - my_age
    print("You are", difference, "years older than me.\n")

# Checking which number is greater
print("We will check which number is greater.\n")

first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))

if first_number > second_number:
    print(first_number, "is greater than", second_number, "\n")
elif first_number == second_number:
    print("Both numbers are the same.\n")
else:
    print(second_number, "is greater than", first_number, "\n")

# Give grade to students according to their score
score = int(input("Enter your score: "))

if score >= 90 and score <= 100 :
    print("Congratulations you have obtained A\n")
elif score >= 70 and score <= 89 :
    print("Good job , you have obtained B\n")
elif score >= 60 and score <= 69 :
    print("Enough good, continue , you have obtained C\n")
elif score >= 50 and score <= 59 :
    print("Just the average, D, you can more. \n")
else :
    print(" F, You are wrong. Word Hard!!!\n")

# Checking the season based on user input
month = input("Enter the month: ").capitalize()

if month in ["September", "October", "November"]:
    print("The season is Autumn.\n")
elif month in ["December", "January", "February"]:
    print("The season is Winter.\n")
elif month in ["March", "April", "May"]:
    print("The season is Spring.\n")
elif month in ["June", "July", "August"]:
    print("The season is Summer.\n")
else:
    print("Invalid month entered.\n")

# Checking if fruit exists in list
fruits = ['banana', 'orange', 'mango', 'lemon']
fruit = input("Enter a fruit: ").lower()

if fruit in fruits:
    print("That fruit already exists in the list.\n")
else:
    fruits.append(fruit)
    print("Updated fruits list:", fruits, "\n")

# Checking if person has 'skills' key and print middle skill

person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

if 'skills' in person:
    skills_list = person['skills']
    middle_index = len(skills_list) // 2
    print("Middle skill:", skills_list[middle_index], "\n")

# Check if person has 'Python' skill
if 'skills' in person:
    print("Has Python skill?:", 'Python' in person['skills'], "\n")

# Determine developer title
if 'skills' in person:
    skills = person['skills']

    if 'JavaScript' in skills and 'React' in skills and len(skills) == 2:
        print("He is a front end developer\n")
    elif 'Node' in skills and 'Python' in skills and 'MongoDB' in skills:
        print("He is a backend developer\n")
    elif 'React' in skills and 'Node' in skills and 'MongoDB' in skills:
        print("He is a fullstack developer\n")
    else:
        print("unknown title\n")

# Print marriage and location info
if person['is_married'] and person['country'] == 'Finland':
    print(f"{person['first_name']} {person['last_name']} lives in {person['country']}. He is married.")
