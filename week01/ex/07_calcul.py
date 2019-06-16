sum = 0
while True:
    n = input("Enter a number: ")
    if len(n) == 0:
        sum += 0
    elif n == "exit":
        break
    else:
        sum += int(n)
    print("TOTAL: " + str(sum))
