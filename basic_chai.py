# starting basic
print('My name is Jawad')

for c in "Jawad":
    print(c)

# choto loop txt format (in txt)
txt = "The best things in life are free!"
if "Go" in txt:
    print("Yes, 'Free' is present.")
else:
    print("Don't do it")

# print list to string
Sports_name = ["Cricket", "football", "hockey", "Golf"]
print("".join(Sports_name))
print("-".join(Sports_name))
print(", ".join(Sports_name)) 

# length measurement
Girl_friend = "Ahona, Aysha, mredula"
print(len(Girl_friend))

# Uses of f-string
Father_name = "Juyel"
sentence = f"Jawad's Father Name is {Father_name}"

print(sentence)


# Number Conversion

'''decimal_num = int(input("Enter a decimal number: "))

binary_num = bin(decimal_num)
octal_num = oct(decimal_num)
hexadecimal_num = hex(decimal_num)

print("Binary:", binary_num)
print("Octal:", octal_num)
print("Hexadecimal:", hexadecimal_num)'''

# weird syntax

Cubic_number = [y**3 for y in range(0, 5)]
print("Cubic number is:", Cubic_number)

# end weird one

'''y = int(input("Enter a number: "))
Cubic_num = y**3
print("Cube of this number is: ", Cubic_num)'''

# Dictionary data type 

number = {z:z**2 for z in range(5, 8)}
print(number)

# problem-1: Age catagorization => solution

age = int(input("What is your age: "))

if age < 13:
    print("You are child")
elif age < 20:
    print("You are Teenager")
elif age < 60:
    print("You are Adult")
else:
    print("You are backdated")

# problem-2: Movie Ticket Pricing => Solution

Age = int(input("Enter your Age: "))
day = "Friday"

price = 15 if Age > 18 else 10
if day == "Friday":
    price = price - 4
    #price -= 4

    print("Ticket price: $", price)

# problem-3: Grade Calculator => solution

marks = float(input("your marks: "))

if marks > 100:
    print("Please Verify again")
    exit()

if marks >= 80:
    grade = "A+"
elif marks >= 70:
    grade = "A"
elif marks >= 60:
    grade = "A-"
elif marks >= 50:
    grade = "B"
elif marks >= 40:
    grade = "C"
elif marks >= 33:
    grade = "D"
else:
    grade = "F"

print("your grade is: ",grade)

# problem-4: Fruits ripeness checker => solution

Fruit = "Mango" 
color = input("Color of my mango is: ")

if Fruit == "Mango":
    if color == "green":
        print("unripe")
    elif color == "yellow":
        print("ripe")
    elif color == "red":
        print("over-ripe")
else:
    print("invalid color")


# problem-5: Weather Activity Suggestion => solution

weather = input("Weather is: ")

if weather == "Sunny":
    # print("Go for a walk")
    activity = "Go for a walk"
elif weather == "Rainy":
    # print("Read a book")
    activity = "Read a book"
elif weather == "Snowy":
    # print("Build a snowman")
    activity = "Build a snowman"
else:
    activity = "Invalid, Enter Again"

print(activity)

# problem-6: Transportation Mode Selection => solution

distance = int(((input("Distance: "))))

if distance < 3:
    transport = "walk"
elif distance <= 15:
    transport = "bike"
else:
    transport = "car"

print(transport)


# problem-7: Coffee Customization => solution

Order_size = input("small, medium or large: ")
extra_shot = True

if extra_shot:
    Coffee = Order_size + " Coffee with extra shot"
else:
    Coffee = Order_size + " Coffee"

print(Coffee)

# Problem-8: Password Strength Checker => solution

password = input("Enter Your Password: ")

if len(password) < 6:
    Strength = "Weak"
elif len(password) < 10:
    Strength = "Medium"
else:
    Strength = "Strong"

print(Strength)

# problem-9: Leap Year Checker => solution

year = int(input("Enter a Year: "))

if (year % 100 == 0):
    if (year % 400 == 0):
        leap = "Hurrah, it is a Leap Year"
    else:
        leap = "it's not a leap year"
elif (year % 4 == 0):
    leap = "Hurrah, it is a Leap Year"
else:
    leap = "it's not a leap year"

print(leap)



# problem-10: Pet Food Recommendation => solution

Pet = input("Enter pet's species: ")
pet_age = int(input("Enter your Pet's Age: "))

if Pet == "Dog":
    if pet_age < 2:
        Food = "Puppy food"
    else:
        Food = "Others"
elif Pet == "Cat":
    if pet_age > 5:
        Food = "Senior cat food"
    else:
        Food = "Others"

print(Food)

