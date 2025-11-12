
# size = int(input("Enter the size of the pattern: "))

# # Initialize row counter
# row = 0

# # Outer loop controls the rows
# while row < size:
#     # Inner loop prints asterisks in each row
#     for col in range(size):
#         print("*", end="")
#     # Move to the next line after finishing one row
#     print()
#     # Increment row counter
#     row += 1

secret_number = 7

guess_count = 0
guess = 0

while guess != secret_number:
  guess_count += 1
  guess = int(input("Guess a number between 1 and 10: "))

print(f"You guessed it in {guess_count} tries!")