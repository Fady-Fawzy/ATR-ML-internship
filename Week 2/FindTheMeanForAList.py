def FindMean(numbers):
    if len(numbers) == 0:
        raise ValueError("The list is empty, cannot compute mean.")
    else:
        return sum(numbers) / len(numbers)


for i in range(5):
    try:
        numbers = list(map(float, input("Enter numbers separated by spaces: ").split()))
        mean = FindMean(numbers)
        print(f"The mean of the entered numbers is: {mean}")
    except ValueError as e:
        print(e)
