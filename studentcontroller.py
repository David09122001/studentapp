import student as st
class StudentController():

    def __init__(self):
        self.__students = {}

    def add_student(self, dni, name, surname, age, city, province, email):
        if dni not in self.__students:
            student = st.Student(dni, name, surname, age, city, province, email)
            self.__students[dni] = student
            return True
        return False

    def delete_student(self, dni):
        if dni in self.__students:
            student = self.__students.pop(dni)
            return student
        return None

    def modify_student(self, dni, choice, new_value):
        if dni in self.__students:
            student = self.__students[dni]
            if choice == "1":
                student.set_name(new_value)
            elif choice == "2":
                student.set_surnames(new_value)
            elif choice == "3":
                student.set_age(new_value)
            elif choice == "4":
                student.set_city(new_value)
            elif choice == "5":
                student.set_province(new_value)
            elif choice == "6":
                student.set_email(new_value)
            return student
        return None
    
    #Fer com el add
    def modify_studentt(self, student):
        if self.__dni in self.__students:
            student = self.__students[self.__dni]
        

    def search_student(self, dni):
        if dni in self.__students:
            return self.__students[dni]
        return None