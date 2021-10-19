
age = int(input("Enter Your age : " ))

if age < 0:
    print("ERROR")
elif age <= 10:
    print('you are Children')
elif age > 10 and age <= 20:
 print("You are Teenager")
elif age > 20 and age <=35:
 print("You are Adult")    
elif age > 35 and age <=55:
 print("You are Middle age")
elif age >=56:
    print("You are Old age")
