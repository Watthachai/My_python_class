mylist = ['0:Zero','1:One','2:Two','3:Three','4:Four','5:Five','6:Six','7:Seven','8:Eigth','9:Nine']
num = int(input("Enter Number : "))
if num < 0:
    num = num * (-1)
n = num%10
print(mylist[n])