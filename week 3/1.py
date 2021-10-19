#1
n = int(input('Enter Number : '))
sum = 0

if n < 0:
    print('ERROR!')
    exit()

for i in range(0,n+1,5):
    sum = sum+i
print(sum)

