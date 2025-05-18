while True:  # Start an infinite loop to keep asking for input
    user_input = input("Please enter an even integer: ")

    if user_input.isdigit():  # Check if the input consists of digits only (positive integers)
        number = int(user_input)
        if number % 2 == 0:
            print(f"You entered the even integer: {number}")
            break  # Exit the loop if it's a valid even integer
        else:
            print("Invalid input: Not an even integer. Please try again.")
    else:
        print("Invalid input: Not an integer. Please try again.")

