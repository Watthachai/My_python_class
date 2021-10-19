money = [10000,15000,20000,25000,30000,35000,40000]


rate = int(input('Enter interest rate: '))
rate_per = rate/100

print(f"year        1            2           3        4")
for m in money:
    mylist = []
    
    for y in range(0,5):
        result = m*(1+rate_per)**y
        mylist.append("{:.2f}".format(result))


    print(*mylist,sep=' | ')