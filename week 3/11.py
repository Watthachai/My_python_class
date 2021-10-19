num = int(input('Enter Number : '))
n1= 0
n2 = 1
mylist = []


if num <= 0 :
    print('ERROR!')
    exit()
else:   
    print(n1,n2,sep=',',end = ',')
    for i in range(1,num):
        if n2<num:
            n1,n2 = n2,n1 + n2
            sum = n2 
            mylist.append(sum)
            
mylist.pop(-1)
print(*mylist,sep=',')
