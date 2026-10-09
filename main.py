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
    a_student = {
        "student id": student_id,
        "name": name,
        "course": course,
        "score": score
    }

    for student in students:
        if student["student id"] == student_id:
            print("Student ID Already Exists!")
            return False
    return a_student

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


def search_students():
    student_id = input("Enter Student ID: ")
    find = False
    for student in students:
        if student["student id"] == student_id:
            find = True
            print("Student Found")
            print(f"Student ID: {student['student id']}")
            print(f"Name: {student["name"]}")
            print(f"Course: {student["course"]}")
            print(f"Score: {student["score"]}")
    if not find:
        print("Student Not Found")

def update_score():
    student_id = input("Enter student ID: ")
    find = False
    for student in students:
        if student["student id"] == student_id:
            find = True
            updated_score = int(input("Enter New Score: "))
            student["score"] = updated_score
            print("Score Updated")
    if not find:
        print("Student not found")
    with open("students.json", "w") as file:
        json.dump(students, file)

def remove_student():
    student_id = input("Enter student ID: ")
    find = False
    for student in students: 
        if student["student id"] == student_id:
            find = True
            students.remove(student)
            print("Student Deleted")
    if not find:
        print("student not found")
    with open("students.json", "w") as file:
        json.dump(students, file)  

def class_statistics():
    print("==== CLASS STATISTICS ====")
    total_students = len(students)
    print(f"Total Students: {total_students}")

    total_scores = 0
    for student in students:
        total_scores = total_scores + student["score"]
    average_score = total_scores / total_students
    print(f"Average Score: {average_score}")

    scores = []
    for student in students:
        scores.append(student["score"])
    highest_score = max(scores)
    loowest_score = min(scores)
    print(f"Highest Score: {highest_score}")
    print(f"Lowest Score: {loowest_score}")

    for student in students:
        if student["score"] == highest_score:
            print(f"Student with highest score: {student['name']}")


  
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
        search_students()
    elif choice == "4":
        update_score()
    elif choice == "5":
        remove_student()
    elif choice == "6":
        class_statistics()
    elif choice == "7":
        pass
    elif choice == "8":
        break