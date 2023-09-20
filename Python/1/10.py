while True:
    num1 = input("Please enter a number: ")
    if num1 == "#":
        break
    num2 = input("Please enter another number: ")
    if num2 == "#":
        break
    if num1 == num2:
        print("You have entered the same number twice!")
    else:
        print("The numbers you have entered are different.")