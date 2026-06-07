ip = input("Enter a string: ")

ip_rev = ip[::-1]

if ip.lower() == ip_rev.lower():
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")