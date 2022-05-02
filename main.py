def personal_details(name,age):
    print("your name is",name,"and your age is",age)
   
name = input("enter your name : ")
age = int(input("enter your age : "))

details = personal_details(name,age)
print(details)