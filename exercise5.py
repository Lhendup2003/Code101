def print_right_triangle(height):
    for i in range(1, height + 1):
        print('*' * i)

try:
    height = int(input("Enter the height of the triangle (number of rows): "))
    if height <= 0:
        print("Height must be a positive integer.")
    else:
        print_right_triangle(height)
except ValueError:
    print("Please enter a valid integer for the height.")
