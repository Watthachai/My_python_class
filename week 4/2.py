count = 1
list_hour = []
list_minute = []
while count <= 2:

    hour = int(input("Enter Hour : "))
    minute = int(input("Enter Min: "))
    
    if hour < 7:
        print('Park is Close!')
        exit() 
    elif hour >= 23:
        print('Park is Close!')
        exit()
    list_hour.append(hour)
    list_minute.append(minute)
    count +=1

covert1 = (list_hour[0]*60)+list_minute[0]
covert2 = (list_hour[1]*60)+list_minute[1]

result = covert1 - covert2
new_min = abs(result)

if new_min <= 15:
    total = 0
elif 15 < new_min < 180:
    total = (new_min//60)+10
elif new_min < 240 and new_min < 360:
    total = (new_min//60)*10+20
elif new_min <600:
    total = 200
    
print(f'Total : {total}')
