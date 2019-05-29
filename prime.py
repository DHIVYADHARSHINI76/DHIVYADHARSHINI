x = int(input(""))
if x > 1:
    for i in range(2, x):
        if (x % i) == 0:
            print("no")
            break
    else:
        print("yes")
elif x == 0 or 1:
    print(x, "is a neither prime NOR composite number")
else:
    print(x, "is NOT a prime number it is a COMPOSITE number")
