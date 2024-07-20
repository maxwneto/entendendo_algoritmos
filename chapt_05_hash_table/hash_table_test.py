from hash_table import add_employee

employees = {}

while True:
    name = input("Enter the employee's name (or 'exit' to finish): ")
    if name.lower() == 'exit':
        break
        
    try:
        personal_number = int(input("Enter the employee's personal number (8 digits): "))
        add_employee(employees, name, personal_number)
    except ValueError:
        print("Error: The personal  number must be a number.")

print("\nAdded employees:")
for name, personal_number in employees.items():
    print(f"Name: {name}, Personal Number: {personal_number}")