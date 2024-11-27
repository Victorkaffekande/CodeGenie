def calculate_average(numbers):
    if not numbers:
        return None  # Return None if the list is empty
    return sum(numbers) / len(numbers)

# Example usage:
numbers = [10, 20, 30, 40, 50]
average = calculate_average(numbers)
print(f"The average is: {average}")