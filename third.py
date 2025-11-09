# Unpacking user information into separate variables
user_info = ['alex', 'developer', True]
name, role, is_active = user_info

# Formatting the name and role
formatted_name = name.capitalize()
formatted_role = role.upper()

# Checking if the user is active and printing the appropriate message
if is_active:
    print('''User Profile
-------------
Name: {}
Role: {}
Status: Active'''.format(formatted_name, formatted_role))
else:
    print("This user is inactive.")