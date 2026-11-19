numbers = []

for i in range(10):
    num = int(input("Enter number: "))
    numbers.append(num)

even_numbers = []

for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)

print("Original List:", numbers)
print("Even Numbers:", even_numbers)
