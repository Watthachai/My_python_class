print("---Pizza Menu---")
print("1.Small Pizza")
print("2.Medium Pizza")
print("3.Large Pizza")
menu = str(input("Enter Number for order pizza : "))
#defind Variable
s_pizza = 99
m_pizza = 199
l_pizza = 299
total = 0
#--------------------------------------
if menu == '1':
    print("******************************")
    print("You order small pizza")
    chess = str(input("Do you want more chess : Y/N\n"))
    if chess == 'y' or chess=='Y':
        total = s_pizza+20
        extra = str(input("Do you want extra : Y/N\n"))
        if extra =='y' or extra == 'Y':
            print(f"total is {total+20}")
        elif extra =='n' or extra == 'N':
            print(f"total is {total}")
        else:
            print("ERROR!")
    elif chess == 'n':
        total = s_pizza
        extra = str(input("Do you want extra : Y/N\n"))
        if extra =='y' or extra == 'Y':
            print(f"total is {total+20}")
        elif extra =='n' or extra == 'N':
            print(f"total is {total}")
        else:
            print("ERROR!")
    else:
        print("ERROR!!")
#---------------------------------------------------------------------
elif menu == '2':
    print("******************************")
    print("You order medium pizza")
    chess = str(input("Do you want more chess : Y/N\n"))
    if chess == 'y' or chess=='Y':
        total = m_pizza+30
        extra = str(input("Do you want extra : Y/N\n"))
        if extra =='y' or extra == 'Y':
            print(f"total is {total+20}")
        elif extra =='n' or extra == 'N':
            print(f"total is {total}")
        else:
            print("ERROR!")
    elif chess == 'n':
        total = m_pizza
        extra = str(input("Do you want extra : Y/N\n"))
        if extra =='y' or extra == 'Y':
            print(f"total is {total+20}")
        elif extra =='n' or extra == 'N':
            print(f"total is {total}")
        else:
            print("ERROR!")
    else:
        print("ERROR!!")
#---------------------------------------------------------------------
elif menu == '3':
    print("******************************")
    print("You order large pizza")
    chess = str(input("Do you want more chess : Y/N\n"))
    if chess == 'y' or chess=='Y':
        total = l_pizza+40
        extra = str(input("Do you want extra : Y/N\n"))
        if extra =='y' or extra == 'Y':
            print(f"total is {total+20}")
        elif extra =='n' or extra == 'N':
            print(f"total is {total}")
        else:
            print("ERROR!")
    elif chess == 'n' or chess=='N':
        total = l_pizza
        extra = str(input("Do you want extra : Y/N\n"))
        if extra =='y' or extra == 'Y':
            print(f"total is {total+20}")
        elif extra =='n' or extra == 'N':
            print(f"total is {total}")
        else:
            print("ERROR!")
    else:
        print("ERROR!!")
else:
    print("ERROR!")