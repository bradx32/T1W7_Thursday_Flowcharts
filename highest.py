# Take three numbers a, b and c as input
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

# If a > b
if a > b:
    # If a > c
    if a > c:
        # display a
        print(a)
    # else
    else:
        # display c
        print(c)

# else
else:
    # If b > c
    if b > c:
        # display b
        print(b)
    # else
    else:
        # display c
        print(c)