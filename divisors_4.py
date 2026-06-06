ip = int(input("Enter a number: "))
print([x for x in range(1, ip+1) if ip%x == 0])