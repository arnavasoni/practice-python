number = int(input("Enter a number: "))
if number % 4 == 0:
    print(f"{number} is divisible by 4.")
else:
    print(f"{number} is an even number." if number % 2 == 0 else f"{number} is an odd number.")