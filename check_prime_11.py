def check_prime(num):
    count = 0
    if num == 1:
        return "Neither prime nor composite"
    for i in range(1, int(num**0.5)+1):
        if num % i == 0:
            count += 1
    if count >= 2:
        return False
    else:
        return True

while True:
    num = int(input("Enter a number: "))
    if num < 0:
        break
    else:
        print(check_prime(num))