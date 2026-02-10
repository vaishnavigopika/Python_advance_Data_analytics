import csv
while True:
    
    print("1.Register/n2.Login/n3.Exit")
    ch=int(input("enter your choice"))
    if ch==1:
        name=input("enter your name")
        password=input("enter your password")
        with open("user.csv ","a") as f:
            f.write(name+","+password+"\n")
        print("Registration successful")
    if ch==2:
        name=input("enter your name")
        passs= input("enter your passwrd")
        data={}
        with open("user.csv",r) as f1:
            csvFile = csv.reader(file)
            headers = next(csvFile) 
            for h in headers:
                data[h] = []
            for row in csvFile: 
                for i in range(len(headers)):
                    data[headers[i]].append(row[i])
        print(data)
        for key,value in data.items():
            if name in value and passs in value:
                print("Login successful")
                break
        
            