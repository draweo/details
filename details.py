# Details task on Bootcamp. 
# Gather varied details from a user and output as a single sentence.

# request user input their first name
user_first_name = input("Enter your first name: ")
# request user input their surname
user_surname = input("Enter your surname: ")
# request user input their age
user_age = input("Enter your age: ")

# request user input their house number
user_house_no = input("Enter your house number: ")
# request user input their street name
user_street = input("Enter your street name: ")

# print single sentence containing all of the above information
# attempting to convert first letters of all names to capital letters

# Note: avoid reference to he/she in this sentence as gender of user is unknown

print(f"This is {str.title(user_first_name)} {str.title(user_surname)} who is {user_age} years of age and lives at {user_house_no} {str.title(user_street)}.")