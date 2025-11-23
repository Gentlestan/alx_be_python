from datetime import datetime, timedelta

def display_current_datetime():
    # Save current date and time
    current_date = datetime.now()
    # Print in format YYYY-MM-DD HH:MM:SS
    print("Current date and time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))
    return current_date


def calculate_future_date(days):
    # Get current date
    current_date = datetime.now()
    # Calculate future date
    future_date = current_date + timedelta(days=days)
    # Print in format YYYY-MM-DD
    print("Future date:", future_date.strftime("%Y-%m-%d"))
    return future_date


def main():
    # Part 1: Display current date and time
    display_current_datetime()

    # Part 2: Ask user for number of days
    days_input = int(input("Enter the number of days to add to the current date: "))
    
    # Calculate and display future date
    calculate_future_date(days_input)


if __name__ == "__main__":
    main()
