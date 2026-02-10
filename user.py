while True:
    print("1.Register/n2.Login/n3.Exit")
    ch=int(input("enter your choice"))
    if ch==1:
        name=input("enter your name")
        password=input("enter your password")
        with open("user.txt","a") as f:
            f.write(name+","+password+"\n")
        print("Registration successful")
    if ch==2:
        name=input("enter your name")
        