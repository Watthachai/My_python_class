mylist = []


num = input('Entrer Number : ').split()

if len(num) > 10 :
    print('ERROR')
    exit()


for i in num:
    mylist.append(int(i))
n = len(mylist)
for i in range(n):
    for j  in range(0, n-i-1):
        if mylist[j] > mylist[j+1]:
            mylist[j], mylist[j+1] = mylist[j+1], mylist[j]

for check in range(len(mylist)):
    if mylist[check] == 0 :
        pass
    elif mylist[check] != 0 :
        len1 = mylist[check]

        for index in range(len(mylist)):
            if mylist[index] <= len1:
                pass
            else:
                while mylist[0]==0:

                    mylist.insert(index ,0)
                    mylist.remove(0)

print(*mylist,sep=',')