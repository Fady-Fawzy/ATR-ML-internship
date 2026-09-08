import numpy as np


def FindMean(numbers):
    if len(numbers) == 0:
        raise ValueError("The list is empty, cannot compute mean.")
    else:
        return sum(numbers) / len(numbers)

numbers = list(map(float, input("Enter numbers separated by spaces: ").split()))
try:
    mean = FindMean(numbers)
    print(f"The mean of the entered numbers (from the function) is: {mean}")
except ValueError as e:
    print(e)

NpArray = np.array(numbers)
mean = np.mean(NpArray)
print(f"The mean of the entered numbers (from NP) is: {mean}")

