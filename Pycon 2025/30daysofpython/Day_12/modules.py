import random
import string

#Generate a random user ID with 6 characters
def random_user_id():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

print("Generated random user ID (6 characters):", random_user_id())


# 2. Generate multiple user IDs based on user input
def user_id_gen_by_user():
    num_chars = int(input("Enter number of characters per ID: "))
    num_ids = int(input("Enter number of IDs to generate: "))
    print(f"\nGenerating {num_ids} user IDs with {num_chars} characters each:")
    for i in range(1, num_ids + 1):
        user_id = ''.join(random.choices(string.ascii_letters + string.digits, k=num_chars))
        print(f"  ID {i}: {user_id}")

user_id_gen_by_user()


# 3. Generate an RGB color
def rgb_color_gen():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return f"rgb({r},{g},{b})"

print(" Generated RGB color:", rgb_color_gen())

#Generate a list of hexadecimal colors
def list_of_hexa_colors(n):
    colors = []
    for _ in range(n):
        color = "#{:06x}".format(random.randint(0, 0xFFFFFF))
        colors.append(color)
    return colors

#Generate a list of RGB colors
def list_of_rgb_colors(n):
    colors = []
    for _ in range(n):
        colors.append(rgb_color_gen())
    return colors

#Generate any number of hexa or RGB colors
def generate_colors(color_type, n):
    if color_type.lower() == "hexa":
        result = list_of_hexa_colors(n)
        print(f"Generated {n} HEX colors:")
        for i, color in enumerate(result, 1):
            print(f"  HEX {i}: {color}")
        return result
    elif color_type.lower() == "rgb":
        result = list_of_rgb_colors(n)
        print(f" Generated {n} RGB colors:")
        for i, color in enumerate(result, 1):
            print(f"  RGB {i}: {color}")
        return result
    else:
        return "Invalid color type. Use 'hexa' or 'rgb'."

# Examples:
generate_colors('hexa', 3)
generate_colors('rgb', 2)

#Shuffle a list
def shuffle_list(lst):
    shuffled = lst[:]
    random.shuffle(shuffled)
    print("Original list:", lst)
    print("Shuffled list:", shuffled)
    return shuffled

shuffle_list([1, 2, 3, 4, 5])


#Generate 7 unique random numbers between 0 and 9
def unique_random_numbers():
    numbers = random.sample(range(10), 7)
    print("Generated 7 unique random numbers (0-9):", numbers)
    return numbers

unique_random_numbers()
