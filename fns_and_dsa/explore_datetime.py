from datetime import datetime, timedelta

# Part 1: Display the Current Date and Time
def display_current_datetime():
    # Get the current date and time
    current_date = datetime.now()
    
    # Format the date and time
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    
    # Print the formatted date and time
    print("Current date and time:", formatted_date)

# Part 2: Calculate a Future Date
def calculate_future_date():
    try:
        # Prompt the user for number of days
        days = int(input("Enter the number of days to add to the current date: "))
        
        # Get today's date
        today = datetime.now()
        
        # Calculate future date
        future_date = today + timedelta(days=days)
        
        # Print the future date in YYYY-MM-DD format
        print("Future date:", future_date.strftime("%Y-%m-%d"))
    
    except ValueError:
        print("Please enter a valid integer for the number of days.")

# Run the program
display_current_datetime()
calculate_future_date()
