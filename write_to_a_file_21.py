content = input("Write a sentence: ")
name = input("Enter the name of the file you want to create: ")

with open(f"{name}.txt", 'w') as open_file:
    open_file.write(content)
