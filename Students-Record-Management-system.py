import csv
import json
import os

# Choose storage format
print("Choose Storage Format:")
print("1. CSV")
print("2. JSON")

choice = input("Enter your choice: ")

if choice == "1":
    FILE = "students.csv"
    FORMAT = "csv"
elif choice == "2":
    FILE = "students.json"
    FORMAT = "json"
else:
    print("Invalid choice!")
    exit()


# Load student records
def load_records():
    if not os.path.exists(FILE):
        return []

    try:
        if FORMAT == "json":
            with open(FILE, "r") as f:
                return json.load(f)

        else:
            with open(FILE, "r", newline="") as f:
                return list(csv.DictReader(f))

    except (json.JSONDecodeError, UnicodeDecodeError):
        print("Invalid data file. Starting with empty records.")
        return []


# Save student records
def save_records():
    if FORMAT == "json":
        with open(FILE, "w") as f:
            json.dump(students, f, indent=4)

    else:
        with open(FILE, "w", newline="") as f:
            fields = ["ID", "Name", "Age", "Course", "Email"]
            writer = csv.DictWriter(f, fieldnames=fields)
            writer.writeheader()
            writer.writerows(students)


students = load_records()


# CREATE
def add_student():
    sid = input("Enter Student ID: ")

    if any(s["ID"] == sid for s in students):
        print("Student ID already exists!")
        return

    name = input("Enter Name: ")
    age = input("Enter Age: ")

    if not age.isdigit() or int(age) <= 0:
        print("Invalid age!")
        return

    course = input("Enter Course: ")
    email = input("Enter Email: ")

    student = {
        "ID": sid,
        "Name": name,
        "Age": age,
        "Course": course,
        "Email": email
    }

    students.append(student)
    save_records()
    print("Student added successfully!")


# READ
def view_students():
    if not students:
        print("No student records found!")
        return

    for s in students:
        print("----------------------")
        print("ID:", s["ID"])
        print("Name:", s["Name"])
        print("Age:", s["Age"])
        print("Course:", s["Course"])
        print("Email:", s["Email"])


# UPDATE
def update_student():
    sid = input("Enter Student ID to update: ")

    for s in students:
        if s["ID"] == sid:
            print("1. Update Name")
            print("2. Update Age")
            print("3. Update Course")
            print("4. Update Email")

            ch = input("Enter choice: ")

            if ch == "1":
                s["Name"] = input("Enter new name: ")

            elif ch == "2":
                age = input("Enter new age: ")
                if not age.isdigit() or int(age) <= 0:
                    print("Invalid age!")
                    return
                s["Age"] = age

            elif ch == "3":
                s["Course"] = input("Enter new course: ")

            elif ch == "4":
                s["Email"] = input("Enter new email: ")

            else:
                print("Invalid choice!")
                return

            save_records()
            print("Record updated successfully!")
            return

    print("Student not found!")


# DELETE
def delete_student():
    sid = input("Enter Student ID to delete: ")

    for s in students:
        if s["ID"] == sid:
            students.remove(s)
            save_records()
            print("Record deleted successfully!")
            return

    print("Student not found!")


# MAIN MENU
while True:
    print("\n===== STUDENT RECORD MANAGEMENT =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")

    option = input("Enter your choice: ")

    if option == "1":
        add_student()

    elif option == "2":
        view_students()

    elif option == "3":
        update_student()

    elif option == "4":
        delete_student()

    elif option == "5":
        print("Thank you for using the system!")
        break

    else:
        print("Invalid option! Try again.")