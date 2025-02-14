numbers = [10, 25, 37, 45, 89, 5]

largest = numbers[0]


for num in numbers:
    if num > largest:
        largest = num  

print("Largest number:", largest)