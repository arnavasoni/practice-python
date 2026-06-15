import random
import string
import time

characters = string.ascii_letters + string.digits + string.punctuation

ip = input("Do you want a strong or weak password?: ")
weak_pwds = [1234567890, "qwerty", "password"]
if ip.lower() == "strong":
    start = time.time()
    password = "".join(random.choices(characters, k = 12))
    print(password)
    end = time.time()
    print(f"It took {end-start} seconds to generate the password.")
else:
    print(random.choice(weak_pwds))