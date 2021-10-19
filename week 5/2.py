n = int(input("Enter Number : "))

text = ''
newtext = ''
half = ''
k = n-1

if n >= 10:
    print('Error!')
    exit()
elif n <= 0:
    print('Error!')
    exit()

for x in range(0,n+1): 
    for j in range(0,k+1): #เพิ่มช่องว่าง
        text += " "
    k = k-1
    for y in range(0,x):
        text += str(y)

    text += str(x)
    for y in range(x-1,-1,-1):
        text += str(y)
    text += '\n'

newtext = text.split("\n") #เปลี่ยนจาก text ที่เป็น str ให้เป็น list และเพิ่มโดยการลบตัว "\n"
newtext.pop(-1) #ลบตัวด้านหลังสุดของ list
print(*newtext,sep='\n')
half = text.split("\n")  #เปลี่ยนจาก text ที่เป็น str ให้เป็น list และเพิ่มโดยการลบตัว "\n"
half.reverse() #กลับหลัง list 
half.pop(0) # ลบตำแหน่งที่ 0 ใน list 
half.pop(0) # ลบตำแหน่งที่ 0 ใน list 
print(*half,sep='\n')