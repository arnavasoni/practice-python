name = input("Enter your name: ")
age = input("Enter your age: ")

year = 2026 # static as per question instructions
years_to_100 = year - int(age) + 100

message = f'Hi {name}, you will be 100 years old in the year {years_to_100}.'
# to check order of operations
print(message)

number = int(input("Enter a number: "))
print(message * number)

print((message + "\n") * number)