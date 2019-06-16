n = input("Enter a number: ")
if n.isdigit():
    print(n + " is " + ("EVEN" if int(n) % 2 == 0 else "ODD"))
elif len(n) == 0:
    print("EXIT")
else:
    print(n + " is not a valid number.")

