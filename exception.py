try:
    a= int(input("enter a number"))
    b=input("enter a string")
    s=0
    s=b+a
    print(s)
except ValueError:
    print("Invalid input. Please enter a valid integer.")
except TypeError:
    print("Invalid input. Please enter a valid string")