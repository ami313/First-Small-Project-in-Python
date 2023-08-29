student_data = []

def display_data():
    print("----- Student Data -----")
    if not student_data:
        print("No data available.")
    else:
        for student in student_data:
            print("Name:", student["name"])
            print("Roll Number:", student["roll_number"])
            print("Department:", student["department"])
            print("CGPA:", student["cgpa"])
            print("Field of Interest:", student["field_of_interest"])
            print("------------------------")

def add_data():
    print("----- Add Student Data -----")
    name = input("Enter Name: ")
    roll_number = input("Enter Roll Number: ")
    department = input("Enter Department: ")
    cgpa = float(input("Enter CGPA: "))
    field_of_interest = input("Enter Field of Interest: ")

    student = {
        "name": name,
        "roll_number": roll_number,
        "department": department,
        "cgpa": cgpa,
        "field_of_interest": field_of_interest
    }

    student_data.append(student)
    print("Data added successfully.")

def remove_data():
    print("----- Remove Student Data -----")
    roll_number = input("Enter Roll Number of the student to remove: ")
    found = False

    for student in student_data:
        if student["roll_number"] == roll_number:
            student_data.remove(student)
            print("Data removed successfully.")
            found = True
            break

    if not found:
        print("Student data not found.")

def menu():
    print("\n----- Menu -----")
    print("1. Display Student Data")
    print("2. Add Student Data")
    print("3. Remove Student Data")
    print("4. Quit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        display_data()
    elif choice == "2":
        add_data()
    elif choice == "3":
        remove_data()
    elif choice == "4":
        print("Thank you. Goodbye!")
        return
    else:
        print("Invalid choice. Please try again.")

    menu()

menu()
