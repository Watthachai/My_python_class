count = []

for i in range (2001,3201):
    if(i % 5)==0:
        pass
    elif(i% 7)==0:
        count.append(i)

print(*count,sep=',')