# Initialize empty lists and dictionary
students_list = []
students_dict = {}

# Function to add student information
def add_student():
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    grade = input("Enter student grade: ")

    students_list.append(name)
    students_dict[name] = {'age': age, 'grade': grade}
    print("Student information added successfully.")

# Function to search for a student
def search_student(name):
    if name in students_dict:
        print(f"Name: {name}, Age: {students_dict[name]['age']}, Grade: {students_dict[name]['grade']}")
    else:
        print("Student not found.")

# Function to remove a student
def remove_student(name):
    if name in students_dict:
        students_list.remove(name)
        del students_dict[name]
        print("Student removed successfully.")
    else:
        print("Student not found.")

# Main function
def main():
    while True:
        print("\nStudent Information Management System")
        print("1. Add Student")
        print("2. Search Student")
        print("3. Remove Student")
        print("4. View All Students")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_student()
        elif choice == '2':
            name = input("Enter student name to search: ")
            search_student(name)
        elif choice == '3':
            name = input("Enter student name to remove: ")
            remove_student(name)
        elif choice == '4':
            print("\nAll Students:")
            for name, info in students_dict.items():
                print(f"Name: {name}, Age: {info['age']}, Grade: {info['grade']}")
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
