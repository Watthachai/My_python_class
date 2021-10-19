mylist=[]

for i in range (0,8000):
    if i > 1:
        for n in range(2, i):
            if (i % n) ==0:
                break
        else:
            mylist.append(i)

print(mylist[1000])