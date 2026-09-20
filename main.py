# Press Start: Find Your Gamer Type 
# Author: Kenzie Davis 
# A quiz/questionnaire program built for CS 104 Project 1

# TODO: Define your variables here.

name = ""
competitive = ""
friends = ""
exploring = ""
winning = ""
daily = ""
gamer_type = ""
# TODO: Print a welcome message introducing your program. 

print(" Press Start: Find Your Gamer Type ")
print("Answer the following questions to find out what type of gamer you are!")

# TODO: Write your questions and conditional logic here.
# Follow the outline you planned in your README.
# Ask the user for their name.
name = input("What is your name? ")
print()
print("Welcome, " + name + "!")
print()

# Question 1
competitive = input("Do you enjoy competitive games? (yes/no): ")

if competitive == "yes":
    print("You enjoy competition!")
else:
    print("You prefer a more relaxed gaming experience.")

print()

# Question 2
friends = input("Do you prefer playing video games with friends? (yes/no): ")

if friends == "yes":
    print("You enjoy gaming with other people!")
else:
    print("You enjoy gaming on your own!")

print()

# Question 3
exploring = input("Do you enjoy exploring large game worlds? (yes/no): ")

if exploring == "yes":
    print("You enjoy discovering new places in games!")
else:
    print("You prefer staying focused on the main game.")

print()

# Question 4
winning = input("Do you care more about winning than the story? (yes/no): ")

if winning == "yes":
    print("Winning is important to you!")
else:
    print("You care about more than just winning!")

print()

# Question 5
daily = input("Do you play video games almost every day? (yes/no): ")

if daily == "yes":
    print("You are a frequent gamer!")
else:
    print("You enjoy gaming when you have the time!")

print()

# Determine the final gamer type.
if competitive == "yes" and winning == "yes":
    gamer_type = "Competitive Gamer"
elif exploring == "yes":
    gamer_type = "Explorer Gamer"
elif friends == "yes":
    gamer_type = "Social Gamer"
else:
    gamer_type = "Casual Gamer"
# TODO: Display the final results to the user.
print("===================================")
print("Your Gamer Type")
print("===================================")
print(name + ", you are a " + gamer_type + "!")
print("Thanks for taking the quiz!")