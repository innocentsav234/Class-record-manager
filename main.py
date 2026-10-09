import json, csv


def load_students():
    with open("students.json", "r") as file:
        load = json.load(file)
        return load


students = load_students()


def add_student():
    student_id = input("Enter Student ID: ")
    name = input("Enter Student Name: ")
    course = input("Enter Student Course: ")
    score = int(input("Enter Student Score: "))
    student = {
        "student id": student_id,
        "name": name,
        "course": course,
        "score": score
    }

    for student in students:
        if student["student id"] == student_id:
            print("Student ID Already Exists!")
            return False
    return student

def save_students():
    new_students = add_student()
    if new_students:
        students.append(new_students)
    with open("students.json", 'w') as file:
        json.dump(students, file)

def view_students():
    students = load_students()
    if not students:
        print("No Students Available")
        return
    for student in students:
        print(f"Student ID: {student['student id']}")
        print(f"Name: {student["name"]}")
        print(f"Course: {student["course"]}")
        print(f"Score: {student["score"]}")
while True:
    print("===== CLASSROOM RECORD MANAGER =====")
    print("1. Add Student")
    print("2. View All Student")
    print("3. Search Student")
    print("4. Update Student Score")
    print("5. Remove Student")
    print("6. Show Class Statistics")
    print("7. Expot Records to CSV")
    print("8. Exit")
    choice = input("Choose An Option: ")
    if choice == "1":
        save_students()
    elif choice == "2":
        view_students()
    elif choice == "3":
        pass
    elif choice == "4":
        pass
    elif choice == "5":
        pass
    elif choice == "6":
        pass
    elif choice == "7":
        pass
    elif choice == "8":
        break