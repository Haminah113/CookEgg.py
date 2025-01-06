# Input the number of eggs
eggs = int(input("Enter the number of eggs: "))

# Choose cooking type
print("Choose cooking type:")
print("1. Half-cooked (3 minutes per batch)")
print("2. Fully cooked (5 minutes per batch)")
choice = int(input("Enter 1 or 2: "))

# Set cooking time per batch
if choice == 1:
    time_per_batch = 3
elif choice == 2:
    time_per_batch = 5
else:
    print("Invalid choice. Defaulting to fully cooked.")
    time_per_batch = 5

# Max eggs per batch
max_eggs_per_batch = 6

# Calculate total time
batches = (eggs + max_eggs_per_batch - 1) // max_eggs_per_batch
total_time = batches * time_per_batch

# Print the result
if choice == 1:
    cook_type = "half-cooked"
else:
    cook_type = "fully cooked"

print("To make", cook_type, "eggs for", eggs, "eggs, total boiling time is:", total_time, "minutes.")
