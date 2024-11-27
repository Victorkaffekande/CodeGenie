def calculate_average(numbers):
    if not numbers:
        return None  # Return None if the list is empty
    return sum(numbers) / len(numbers)

# Scenario 1: Empty List
numbers = []
average = calculate_average(numbers)
print(f"Scenario 1 - The average is: {average}")

# Scenario 2: Single Element List
numbers = [10]
average = calculate_average(numbers)
print(f"Scenario 2 - The average is: {average}")

# Scenario 3: Negative Numbers
numbers = [-10, -20, -30]
average = calculate_average(numbers)
print(f"Scenario 3 - The average is: {average}")

# Scenario 4: Mixed Positive and Negative Numbers
numbers = [10, -20, 30]
average = calculate_average(numbers)
print(f"Scenario 4 - The average is: {average}")