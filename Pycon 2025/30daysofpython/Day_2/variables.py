# Day 2: 30 Days of Python Programming


first_name = "Cédric "
last_name = "AMOUZOU-ABLO"
full_name = first_name + last_name
country = "TOGO"
city = "Lomé"
age = ["unknown"]
year = 2025
is_married = False
is_true = True
is_light_on = True
passions, rating_Pycon2025_over_5_stars, message_to_community = ["data", "design", "digital marketing", "cybersecurity"], 4.5, "Hello World"

# Checking type of data
print("Type de first_name:", type(first_name))
print("Type de last_name:", type(last_name))
print("Type de full_name:", type(full_name))
print("Type de country:", type(country))
print("Type de city:", type(city))
print("Type de age:", type(age))
print("Type de year:", type(year))
print("Type de is_married:", type(is_married))
print("Type de is_true:", type(is_true))
print("Type de is_light_on:", type(is_light_on))
print("Type de passions:", type(passions))
print("Type de rating_Pycon2025_over_5_stars:", type(rating_Pycon2025_over_5_stars))
print("Type de message_to_community:", type(message_to_community))

print(len(first_name))
print(min(len(first_name), len(last_name)))
print(max(len(first_name), len(last_name)))

num_one, num_two= 5 , 4
total= num_one + num_two
diff= num_two - num_one
product= num_two * num_one
division= num_one / num_two
remainder=num_two % num_one
floor_division = num_one // num_two

# Circle Datas
radius = 30
pi = 3.1416

#area
area_of_circle = pi * radius ** 2

#circumference
circum_of_circle = 2 * pi * radius

# user input
user_radius = float(input("\nEnter the raduis of the circle : "))
user_area = pi * user_radius ** 2
print("Your circle area is :", user_area, "m²")

#user input informations
print("\n--- Enter  your infomations ---")
first_name = input("Enter your first name : ")
last_name = input("Entez your last name : ")
country = input("What country are you from? : ")
age = int(input("How old are you? : "))

# Screening informations
print("\n---Thanks for your collaboration---")
print("Yours full name :", first_name, last_name)
print("You are from :", country)
print("You are :", age, "years old")







