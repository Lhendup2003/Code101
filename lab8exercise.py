def find_first_repeating_character(s):
    # Dictionary to store the count of each character encountered
    char_count = {}
    
    # Iterate through the characters in the string
    for char in s:
        # Update the count of the character
        if char in char_count:
            # If the character is already in the dictionary, it's a repeat
            # Print the character and its memory address and return it
            print(f"First repeating character: {char}, Memory Address: {id(char)}")
            return char, id(char)
        else:
            # If the character is encountered for the first time, store its count
            char_count[char] = 1
    
    # If no repeating character is found, return None
    return None

# Take input from the user
user_input = input("Enter a string: ")

# Call the function with user input
result = find_first_repeating_character(user_input)

# If no repeating character is found, inform the user
if result is None:
    print("No repeating character found in the input string.")

