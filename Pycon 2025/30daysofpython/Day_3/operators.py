age= 19
height= 1.82
complex_number=(1+6j)

#script to calculate area of triangle with user input
print("Hello we will calculate the area of a triangle. So We need your help\n")

triangle_base= float(input("Enter the base of the traingle: "))
triangle_height= float(input("Enter the height of the the triangle: "))

area= 0.5*triangle_base*triangle_height

print("The area of this triangle is:", area, "m². THANK YOU\n")

#script to calculate the perimetre of triangle with user input
print("Now we will calculate the perimetre of a triangle. Your help is needed\n")
side_a= float(input("Enter the first side: "))
side_b= float(input("Enter the second side: "))
side_c= float(input("Enter the third side: "))

perimetre= side_a + side_b + side_c

print("The perimetre of this triangle is ", perimetre, "m. THANK YOU!, You've done a good job \n")

#geting lenght and width of a rectangle to calculate the area and the perimetre 
print("Are tired? We will calculate the area and the perimetre of the same rectangle. Give the needed informations")

length= float(input("Enter the length of the rectangle: "))
width= float(input("Enter the width of the rectangle: "))

rectangle_area= length * width
rectangle_perimetre= (length + width)*2

print("The perimetre of the rectangle is ", rectangle_perimetre, "m and his area is ",rectangle_area, "m². Fine Job!!\n")

#Calculate the area of circle
print("I know you like mathematics, let calculate the area and circircumference of a circle.")

pi= 3.14
raduis= float(input("Enter the raduis of the circle: "))
circle_area= pi*raduis**2
circle_circumference= 2*pi*raduis

print("The area of this circle is ", circle_area,"m² and the circumference is ",circle_circumference,"m. Come on!\n")

#calculate slote, x-intercept and y-intercept
slope_1 = 2
b = -2
x_intercept = -b / slope_1
y_intercept = b

print("The Slope is :", slope_1)
print("The x-intercept is :", x_intercept)
print("the y-intercept is :", y_intercept, "\n")

# Slope and Euclidean distance between
x1,y1,x2,y2 = 2, 2, 6, 10

slope_2 = (y2 - y1) / (x2 - x1)
e_distance = ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5

print("The slope between points is :", slope_2)
print("The euclidean distance is :", e_distance, "\n")

#Comparing the slopes in tasks 8 and 9
print("Slope in Task 8:", slope_1)
print("Slope in Task 9:", slope_2, "\n")

#Calculate values
x = -3
y = x**2 + 6*x + 9
print("x:", x, "y:", y, "\n")

x = -2
y = x**2 + 6*x + 9
print("x:", x, "y:", y, "\n")

x = -1
y = x**2 + 6*x + 9
print("x:", x, "y:", y, "\n")

x = 0
y = x**2 + 6*x + 9
print("x:", x, "y:", y, "\n")

#Length of 'python' and 'dragon' and a falsy comparison
length_python = len("python")
length_dragon = len("dragon")

falsy_comparison = length_python < length_dragon and False

print("Length of 'python':", length_python)
print("Length of 'dragon':", length_dragon)
print("Falsy comparison result:", falsy_comparison, "\n")

#Checking of 'on' in both 'python' and 'dragon'

result_on = 'on' in 'python' and 'on' in 'dragon'
print("Is 'on' in both 'python' and 'dragon'?", result_on, "\n")

#Check if 'jargon' is in the sentence

sentence = "I hope this course is not full of jargon."
contains_jargon = 'jargon' in sentence

print("Does the sentence contain 'jargon'?", contains_jargon, "\n")

#There is no 'on' in both dragon and python
no_on = 'on' not in 'dragon' and 'on' not in 'python'
print("No 'on' in both dragon and python?", no_on, "\n")

#Converting length of 'python' to float and string

python_length = len("python")
length_float = float(python_length)
length_string = str(length_float)
print("Float convert:", length_float)
print("String convert:", length_string, "\n")

#Check if a number is even (remainder is zero when divisible by 2)
number = 8
remainder = number % 2
print("Number:", number)
print("Remainder when divided by 2:", remainder, "\n")

#Checking
print(7 // 3 == int(2.7))
print(type('10') == type(10))
print(int(float('9.8')) == 10, "\n")


#Calculate the pay of the person
print("You want to knwo your weekly earning?")

hours=int(input("Enter your working hours: "))
rate_per_hour=int(input("Enter how many dollars you earn per hour: "))
weekly_earing= hours * rate_per_hour

print("Your Weekly earning is: ", weekly_earing, "$.\n")


#calculate number of year
second_per_year= 24 * 3600 * 365

user_age= int(input("Enter your âge to know how many second you've alived: "))
alived_seconds= user_age * second_per_year

print("Congratulations you have lived for: ", alived_seconds, " seconds. May God bless you!", "\n")

for i in range(1, 6):
    print(i, i * 1, i**2, i**3,"")













