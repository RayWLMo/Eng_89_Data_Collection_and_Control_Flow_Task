# Version 1
name = "name"
name = input("Please enter your first name:    ")
print("Hello " + name.capitalize().strip() + "!")

# Version 2

full_name = "full name"
full_name = input("Please enter your full name using a comma to separate your first and last name:  ")
first_name = (full_name.split())[0]
last_name = (full_name.split())[1]
print(f"Hi {name.capitalize().strip()}! Your full name is {first_name.capitalize().strip()} {last_name.capitalize().strip()}. Welcome to PyCharm!")
