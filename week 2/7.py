print("******************************************************")
print("1.Rectangle or 2. Traiangle")
menu = int(input("Select : "))
print("******************************************************")
if menu == 1:
 wigth = int(input("Enter wigth : "))
 length = int(input("Enter length : "))
 area1 = wigth*length
 print(f"Area of Rectangle is {area1}")
elif menu ==2:
 base = int(input("Enter base : "))  #(1/2) × ความยาวฐาน × ความสูง
 heigth = int(input("Enter heigth : "))
 area2 = base*heigth*0.5
 print(f"Area of Traiangle is {area2}")
else:
 print("Error")