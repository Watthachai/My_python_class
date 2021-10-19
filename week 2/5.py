a = int(input("Enter A:"))
b = int(input("Enter B:"))
c = int(input("Enter C:"))


if a == b and a == c or b == a and b==c or c==a and c==b :
 print("ERROR")
else:
    if a > b and a < c or a < b and a > c:
     print(f"center number is : a : {a}")
    elif b > a and b < c or b < a and b >c :
     print(f"center number is : b : : {b}")
    elif c > a and c < b or c < a and b > c :
     print(f"center number is : c : {c}")