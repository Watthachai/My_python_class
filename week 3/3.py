c= []
sum = 0
n = int(input('Enter Number : '))
for i in range(1,n+1):
    if(i %2)==0 and (i %3)==0:
        c.append(i)
    if(i % 2)!=0 and (i %3)!=0:
        c.append(i)
    elif(i %2)==1 or (i %3)==1:
        pass
print(*c,sep=',')