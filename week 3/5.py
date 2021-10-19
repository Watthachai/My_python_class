#จงเขียนโปรแกรมที่หาตัวเลขระหว่าง 1000 และ 3000 ที่ทุกหลักเป็นเลขคู่ (รวม 1000 และ 3000) โดยแสดงผลในรูปแบบ คั่นด้วย comma

count = []

for i in range(1000,3000):
    char= str(i)
    if char[3] == '1' or char[3] == '3' or char[3]== '5' or char[3]=='7' or char[3]== '9' :
        pass
    elif char[2] == '1' or char[2] == '3' or char[2]== '5' or char[2]=='7' or char[2]== '9' :
        pass
    elif char[1] == '1' or char[1] == '3' or char[1]== '5' or char[1]=='7' or char[1]== '9' :
        pass
    elif char[0] == '1' or char[0] == '3' or char[0]== '5' or char[0]=='7' or char[0]== '9' :
        pass
    else:
        count.append(char)
print(*count,sep=',')