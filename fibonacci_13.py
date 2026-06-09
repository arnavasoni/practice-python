ip = int(input("Enter the number of numbers: "))

a = 1
b = 0
c = 0

i = 0
print(a)
while i < ip:
    c = a + b
    print(c)
    b = a
    a = c

    i += 1  