home = int(input("Enter Homework score : "))
mid = int(input("Enter Mid Term score : "))
final = int(input("Enter Final score : "))

x = (home)+(mid*(40/100))+(final*(50/100))

print(x)

if x <= 0:
    print("ERROR")
elif x < 50:
 print("F")
elif 50 <= x < 55:
 print("D")
elif 55 <= x < 60:
 print("D+")
elif 60 <= x < 65:
 print("B")
elif 65 <= x < 70:
 print("B+")
elif 70 <= x < 75:
 print("C")
elif 75 <= x < 80:
 print("C+")
elif 80 <= x < 85:
 print("B")
elif 85 <= x < 90:
 print("B+")
elif 90 <= x <= 100:
 print("A")
else:
 print("error")