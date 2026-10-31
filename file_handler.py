

import json 

from pathlib import Path
DATA_FILE = Path(__file__).parent / "students.json"

from student import Student

def save_students(students):
    data=[]

    for student in students:
        data.append({
            "student_id":student.student_id,
            "name":student.name,
            "age":student.age,
            "course":student.course
        })

    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)

def load_students():
    try:
        with open(DATA_FILE, "r") as file:
            data = json.load(file)

        students =[]

        for item in data:
            student = Student(
                item["student_id"],
                item["name"],
                item["age"],
                item["course"]
            )
            students.append(student)

        return students

    except (FileNotFoundError, json.JSONDecodeError):
        return []


