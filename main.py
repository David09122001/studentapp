import studentcontroller as sc
controllerStudent = sc.StudentController()

students = {}

while True:
    print("STUDENT CRUD")
    print("----------------------------")
    print("1.- Add a student")
    print("2.- Delete a student")
    print("3.- Modify a student")
    print("4.- Search a student")
    print("5.- Exit")
    choice = input("Choose option: ")

    if choice == "1":
        try:
            dni = input("Enter DNI: ")
            if dni in students:
                print("Student with the same DNI already exists.")
            else:
                name = input("Enter Name: ")
                surnames = input("Enter Surnames: ")
                age = int(input("Enter Age: "))
                city = input("Enter City: ")
                province = input("Enter Province: ")
                email = input("Enter Email: ")
            if controllerStudent.add_student(dni, name, surnames, age, city, province, email):
                print("Student added successfully!")
            else: 
                print("Student with the same DNI already exists.")
        except ValueError:
            print("Invalid age. Please enter a valid integer for age.")
        except Exception:
            print("Error")
            
    elif choice == "2":
        dni = input("Enter DNI to delete: ")
        deleted_student = controllerStudent.delete_student(dni)
        if deleted_student:
            print("Student with DNI", dni, "has been deleted.")
        else:
            print("Student not found.")
        
    elif choice == "3":
        dni = input("Enter DNI to modify: ")
        print("Modification of student with DNI:", dni)
        print("1.- Modify Name")
        print("2.- Modify Surname")
        print("3.- Modify Age")
        print("4.- Modify City")
        print("5.- Modify Province")
        print("6.- Modify Email")
        choice = input("What do you want to modify (1-6): ")
        new_value = input("Enter the new value: ")
        student = controllerStudent.modify_student(dni, choice, new_value)
        if student:
            print("Student information updated.")
        else:
            print("Student not found.")


    elif choice == "4":
        dni = input("Enter the DNI to find: ")
        found_student = controllerStudent.search_student(dni)
        if found_student:
            print("Student found:")
            print("DNI:", dni)
            print("Name:", found_student.get_name())
            print("Surnames:", found_student.get_surnames())
            print("Age:", found_student.get_age())
            print("City:", found_student.get_city())
            print("Province:", found_student.get_province())
            print("Email:", found_student.get_email())
        else:
            print("Student not found.")

    elif choice == "5":
        break
    else:
        print("Invalid option. Please select a valid option.")

