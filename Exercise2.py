students_list = []
students_dict = {}
#add std information
print("wlc to college")
name=input("Enter the name of the student:")
age=input("enter the age of the student:")
grade=input("enter the grade of the student:")
students_list.append(name)
students_dict[name] = {"age":age, "grade":grade}
print("information successfully added")

#function display the student search
search_student=input("Enter the name of student search:")
if search_student in students_dict:
    print(f"student found:{name}, Age: {students_dict[name]['age']}, Grade: {students_dict[name]['grade']}")
else:
    print("information not found")

remove_student = input("Enter the name of student to be removed or enter skip")
if remove_student in students_dict:
    students_list.remove(name)
    del students_dict[name]
    print("remove successful")

else:
    print("student not founded")