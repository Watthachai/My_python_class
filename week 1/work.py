#----------------------------
#speed = int(input("Enter speed:"))
#if speed < 45:
#    print("slow speed")
#elif 45 <= speed <90:
#    print("moderate speed")
#elif speed >= 90:
#    print("fast speed")
#-----------------------------

#|Ex. 2.4 จากโปรแกรม BMI Calcularor 
#|       = weight(kg) / height(m)^2 
#| Input:
#|      Enter weight : 80
#|      Enter height : 1.75
#| Output:
#|      BMI = 26
#| นอกจากจะบอกค่า BMI แล้ว ยังให้คำแนะนำดังนี้

#|    Under 18.5 they are underweight
#|    Over 18.5 but below 25 they have a normal weight
#|    Over 25 but below 30 they are slightly overweight
#|    Over 30 but below 35 they are obese
#|    Above 35 they are clinically obese.

#| Ex. 2.6 มีตัวแปร 3 ตัว คือ a,b,c (เขียนได้ 2 แบบ)
#| ให้เขียนโปรแกรมหาตัวแปรใดที่เก็บค่ามากที่สุด โดยใช้ if

a=100
b=5
c=40

if a>b and a>c:
    print("a")
elif b>a and b>c:
    print("b")
elif c>a and c>b:
    print("c")