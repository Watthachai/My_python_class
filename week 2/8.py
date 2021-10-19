
month = ['Jan','Feb','Mar','Arp','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
num = int(input("Enter a number : "))
if num > 12 or num <= 0 :
 print("ERROR")
else:
 cal = num-1
 print(f"{num}:"+month[cal])