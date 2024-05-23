def main():
    # Ask for age input
    age = int(input("Enter your age: "))

    # Ask for student status input
    student_status = input("Are you a student? (yes/no): ").lower()

    # Determine eligibility for discount
    if age <= 12:
        print("You are eligible for a discount.")
    elif 13 <= age <= 18 and student_status == 'yes':
        print("You are eligible for a discount.")
    else:
        print("You are not eligible for a discount.")

if __name__ == "__main__":
    main()
