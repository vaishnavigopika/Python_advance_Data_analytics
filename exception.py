try:
    a= int(input("enter a number"))
    b=input("enter a string")
    print("The age of",b,"is",a)
except ValueError:
    print("Invalid input. Please enter a valid integer.")
except TypeError:
    print("Invalid input. Please enter a valid string")
else:
    print("input was valid and code run")
finally:
    print("This block will always execute, regardless of exceptions.")