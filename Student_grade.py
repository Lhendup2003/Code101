num_students = int(input("Enter the number of student"))
i = 1
while i <= num_students:
    total_grade = 0
    num_subjects = int(input(f"Enter the number of subject of student {i}:"))  
    for j in range(1, num_students +1):
        grade = float(input(f"Enter subject{j} grade for student {i}:"))
        total_grade += grade
    average_grade = total_grade / num_subjects
    print(f"Average grade for student {i}: {average_grade:.2f}")
    i=+1
