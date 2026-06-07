status = True

while status:
    i1 = input("(P1) R/P/S: ")
    i2 = input("(P2) R/P/S: ")

    if i1.lower() == i2.lower():
        print("Tie!")
    elif i1.lower() == "r" and i2.lower() == "s":
        print("P1 wins!")
    elif i1.lower() == "p" and i2.lower() == "r":
        print("P1 wins!")
    elif i1.lower() == "s" and i2.lower() == "p":
        print("P1 wins!")
    else:
        print("P2 wins!")
    
    check = input("Play again? (Y/N): ")
    if check.lower() == "n":
        status = False
    elif check.lower() == "y":
        continue
    else:
        print("Invalid input. Please enter Y or N.")
