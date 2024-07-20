# Function to add employees to the dictionary
def add_employee(employees, name, personal_number):
    if len(str(personal_number)) == 8:
        employees[name] = personal_number
    else:
        print("Error: The personal number must be 8 digits long.")