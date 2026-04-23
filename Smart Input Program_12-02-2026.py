# Smart Input Program

name = input("Enter your name: ")
age = int(input("Enter your age: "))
hobby = input("Enter your hobby: ")

# Age category using conditionals
if age < 13:
    category = "Child"
elif age < 20:
    category = "Teenager"
elif age < 60:
    category = "Adult"
else:
    category = "Senior Citizen"

# Personalized message
print("Hello", name + "!")
print("You are a", category + ".")
print("Your hobby is", hobby + ". That's great!")