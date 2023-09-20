numbers = []
for i in range(10):
    num = int(input("Enter a number: "))
    numbers.append(num)
numbers.sort()
print("The numbers from smallest to largest area:")
for num in numbers:
    print(num)
numbers.reverse()
print("The numbers from largest to smallest area:")
for num in numbers:
    print(num)