#studant Management System  

from file_handler import save_students, load_students

from student import Student
students=load_students()
while True:
    print("\n==== STUDENT MANAGMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View Student")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Studet")
    print("6. Exit")

    choice=input("Enter your choice: ")

    if choice=="1":
        print("\n===== ADD STUDENT =====")
        student_id = input("Enter student ID:")
        if not student_id.strip():
            print("Student ID cannot be empty!")
            continue

        dublicate=False

        for student in students:
            if student.student_id == student_id:
                dublicate=True
                break
        if dublicate:
            print("Student ID already exists! Please try again.")
        else:
            name = input("Enter student Name: ")
            if not name.strip():
                print("Name cannot be empty!")
                continue
            age = input("Enter student Age:")
            if not age.isdigit() or int(age) <=0:
                print("plese enter a valid age!")
                continue
            course = input("Enter student Course:")
            if not course.strip():
                print("Course can not be empty!")
                continue
            s1=Student(student_id,name,age,course)
            students.append(s1)
            save_students(students) 

            print("\nstudent added successfully!")


    elif choice=="2": 
        print("\n===== VIEW STUDENT =====")
         
        if len(students)==0:
            print("No student reccord found")
        else:
            for student in students:
                student.display_details()
        print("-----------")    

    elif choice=="3":
        print("\n===== SEARCH STUDENT=====")
        search_id =input("student ID:")

        if not search_id.strip():
            print("Student ID cannot be empty!")
            continue
        found = False

        for student in students:
            if student.student_id == search_id:
                print("\nstudent Found!")
                student.display_details()
                
                found = True
                break
        if found == False:
            print("Student not found")    


    elif choice=="4":
        print("\n====UPDATE STUDENT====")
        search_id = input("Enter student ID:")
        found = False

        for student in students:
            if student.student_id == search_id:

                print("\nstudent Found!")

                print("Enter new Details:")

                #Name validation
                new_name = input("Enter new Name: ")

                if not new_name.strip():
                    print("Name can be empty!")
                    break

                #Age validation
                new_age = input("Enter new age!: ")

                if not new_age.isdigit() or int(new_age) <=0:
                    print("Please enter a valid age: ")
                    break

                #course validation
                new_course = input("Enter new course:")

                if not new_course.strip():
                    print("course cannot be empty!")
                    break
                # Update only after all validations pass
                student.name = new_name.strip()
                student.age = new_age
                student.course = new_course.strip()

                save_students(students) 

                print("\nstudent information update successfully!")

                found=True
                break
            if not found:
                print("student not found and update cancelled")


        
    elif choice=="5":
        print("\n====DELETE STUDENT====")
        delete_id=input("Enter student ID to delete:")

        if not delete_id.strip():
            print("Student ID cannot be empty!")
            continue

        found=False

        for student in students:
            if student.student_id == delete_id:
                students.remove(student)
                save_students(students)
                print("Student Deleted successfully!")

                found=True

                break
        if not found:
            print("Student not found!")    


    elif choice=="6":
        print("Thank you for using Student Mangment student")
        break
    else:
        print("Invalid choice! please try again.")





