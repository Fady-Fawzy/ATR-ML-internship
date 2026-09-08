import numpy as np

numbers = list(map(float, input("Enter numbers separated by spaces: ").split()))
NpArray = np.array(numbers)
n = int(input("Enter the value you want to multiply with: "))
i = -1
for number in numbers:
    i += 1
    numbers[i] = number * n
NpArray = NpArray * n

print(f"Loop Handeld:{numbers}")
print(f"NumPy Handeld:{NpArray}")
